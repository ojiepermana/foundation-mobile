plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.plugin.compose")
}

val repository = rootProject.projectDir.resolve("../..").canonicalFile
val nativeLibraries = layout.buildDirectory.dir("generated/rustJniLibs")
val minimumApi = 24
val pinnedNdk = "28.2.13676358"

android {
    namespace = "foundation.mobile"
    compileSdk = 36
    ndkVersion = pinnedNdk

    defaultConfig {
        applicationId = "foundation.mobile"
        minSdk = minimumApi
        targetSdk = 36
        versionCode = 1
        versionName = "0.1.0"
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
        ndk.abiFilters += listOf("arm64-v8a", "x86_64")
    }
    buildFeatures { compose = true }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    sourceSets.named("main") {
        kotlin.directories += listOf(
            "../presentation/src/main/kotlin",
            "../designsystem/src/main/kotlin",
            repository.resolve("bindings/kotlin").path,
        )
        jniLibs.directories += nativeLibraries.get().asFile.path
    }
}

val sdkDirectory = androidComponents.sdkComponents.sdkDirectory
val buildRustLibraries = tasks.register<Exec>("buildRustLibraries") {
    group = "build"
    description = "Build the shared UniFFI library for both supported Android ABIs."
    workingDir(repository)
    commandLine(
        repository.resolve("scripts/build-android-rust.sh"),
        sdkDirectory.get().dir("ndk/$pinnedNdk").asFile,
        minimumApi,
        nativeLibraries.get().asFile,
    )
}
tasks.named("preBuild") { dependsOn(buildRustLibraries) }

dependencies {
    val composeBom = platform("androidx.compose:compose-bom:2025.08.01")
    implementation(composeBom)
    implementation("androidx.activity:activity-compose:1.11.0")
    implementation("androidx.compose.material3:material3")
    implementation("net.java.dev.jna:jna:5.18.1@aar")

    androidTestImplementation(composeBom)
    androidTestImplementation("androidx.test.ext:junit:1.2.1")
    androidTestImplementation("androidx.test:runner:1.6.2")
    androidTestImplementation("androidx.compose.ui:ui-test-junit4")
}
