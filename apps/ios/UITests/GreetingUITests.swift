import CoreImage
import XCTest

final class GreetingUITests: XCTestCase {
    @MainActor
    func testDisplaysRustGreetingInBothAppearances() throws {
        let device = XCUIDevice.shared
        let previousAppearance = device.appearance
        defer { device.appearance = previousAppearance }

        let app = XCUIApplication()
        app.launchArguments = ["-AppleLanguages", "(en)", "-AppleLocale", "en_US"]
        for appearance in [XCUIDevice.Appearance.light, .dark] {
            device.appearance = appearance
            app.launch()

            let greeting = app.staticTexts["greeting"]
            XCTAssertTrue(greeting.waitForExistence(timeout: 10))
            XCTAssertEqual(greeting.label, "Hello, World!")
            let screenshot = app.screenshot()
            // Sample the background clear of text and status bar.
            let image = CIImage(cgImage: try XCTUnwrap(screenshot.image.cgImage))
            let rect = CGRect(x: image.extent.midX, y: image.extent.height / 4, width: 1, height: 1)
            var pixel = [UInt8](repeating: 0, count: 4)
            CIContext().render(image, toBitmap: &pixel, rowBytes: 4, bounds: rect,
                               format: .RGBA8, colorSpace: CGColorSpace(name: CGColorSpace.sRGB))
            let isDark = pixel[0] < 128 && pixel[1] < 128 && pixel[2] < 128
            XCTAssertEqual(isDark, appearance == .dark, "Unexpected background pixel \(pixel)")
            let attachment = XCTAttachment(screenshot: screenshot)
            attachment.name = appearance == .light ? "Light greeting" : "Dark greeting"
            attachment.lifetime = .keepAlways
            add(attachment)
            app.terminate()
        }
    }
}
