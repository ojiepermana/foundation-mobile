//! Shared application behavior, independent of the mobile ABI.
#![forbid(unsafe_code)]

pub fn hello(name: String) -> String {
    format!("Hello, {name}!")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn greets_the_supplied_name() {
        assert_eq!(hello("World".into()), "Hello, World!");
    }

    #[test]
    fn preserves_empty_names_and_whitespace() {
        assert_eq!(hello(String::new()), "Hello, !");
        assert_eq!(hello(" Ada ".into()), "Hello,  Ada !");
    }
}
