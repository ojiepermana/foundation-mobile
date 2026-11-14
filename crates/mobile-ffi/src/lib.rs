//! Public mobile contract. UniFFI derives both native APIs from this signature.
uniffi::setup_scaffolding!();

#[uniffi::export]
pub fn hello(name: String) -> String {
    foundation_core::hello(name)
}
