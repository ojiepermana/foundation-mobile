import CoreImage
import XCTest

final class GreetingUITests: XCTestCase {
    @MainActor
    func testDisplaysRustGreetingInSystemAppearance() async throws {
        let device = XCUIDevice.shared
        let previousAppearance = device.appearance
        defer { device.appearance = previousAppearance }

        let app = XCUIApplication()
        app.launchArguments = ["-AppleLanguages", "(en)", "-AppleLocale", "en_US"]
        app.launch()
        let greeting = app.staticTexts["greeting"]
        XCTAssertTrue(greeting.waitForExistence(timeout: 10))

        let context = CIContext()
        let requestedMode = ProcessInfo.processInfo.environment["FOUNDATION_APPEARANCE"]
        let appearances: [XCUIDevice.Appearance]
        switch requestedMode {
        case "light": appearances = [.light]
        case "dark": appearances = [.dark]
        case nil: appearances = [.light, .dark]
        default: return XCTFail("Unknown appearance: \(requestedMode ?? "")")
        }
        for appearance in appearances {
            if requestedMode == nil {
                device.appearance = appearance
            } else {
                XCTAssertEqual(device.appearance, appearance, "Expected the configured simulator appearance")
            }
            // XCTest can return before the foreground app has drawn the new appearance.
            let deadline = ContinuousClock.now + .seconds(15)
            var screenshot = app.screenshot()
            var pixel = try backgroundPixel(in: screenshot, context: context)
            let expectedDark = appearance == .dark
            while pixel.prefix(3).allSatisfy({ $0 < 128 }) != expectedDark && ContinuousClock.now < deadline {
                try await Task.sleep(for: .milliseconds(250))
                screenshot = app.screenshot()
                pixel = try backgroundPixel(in: screenshot, context: context)
            }
            XCTAssertEqual(pixel.prefix(3).allSatisfy { $0 < 128 }, expectedDark, "Unexpected background pixel \(pixel)")
            XCTAssertEqual(greeting.label, "Hello, World!")
            let attachment = XCTAttachment(screenshot: screenshot)
            attachment.name = appearance == .light ? "Light greeting" : "Dark greeting"
            attachment.lifetime = .keepAlways
            add(attachment)
        }
    }

    @MainActor
    private func backgroundPixel(in screenshot: XCUIScreenshot, context: CIContext) throws -> [UInt8] {
        let capturedImage = screenshot.image.cgImage
        let image = CIImage(cgImage: try XCTUnwrap(capturedImage))
        let rect = CGRect(x: image.extent.midX, y: image.extent.height / 4, width: 1, height: 1)
        var pixel = [UInt8](repeating: 0, count: 4)
        context.render(image, toBitmap: &pixel, rowBytes: 4, bounds: rect,
                       format: .RGBA8, colorSpace: CGColorSpace(name: CGColorSpace.sRGB))
        return pixel
    }
}
