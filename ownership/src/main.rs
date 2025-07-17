fn main() {
    let s = String::from("hello mustafa");
    
    let word = first_word(&s);

    println!("First word: {word}");

}

fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes(); //Convert the string to an array of bytes

    // iterate through an array of bytes
    for (i, &item) in bytes.iter().enumerate(){
        if item == b' ' {
            return &s[0..i];
        }
    }
    &s[..]
}