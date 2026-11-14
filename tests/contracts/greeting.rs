#[test]
fn exported_contract_preserves_unicode() {
    assert_eq!(mobile_ffi::hello("世界🌍".into()), "Hello, 世界🌍!");
}
