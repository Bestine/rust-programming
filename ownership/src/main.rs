fn main() {
    let mut s = String::from("hello world");

    let word = first_word(&s);

    s.clear();

}

fn first_word(s: &String) -> usize {
    let bytes = s.as_bytes(); //Convert the string to an array of bytes

    // iterate through an array of bytes
    for (i, &item) in bytes.iter().enumerate(){
        if item == b' ' {
            return i;
        }
    }
    s.len()
}