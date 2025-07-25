fn main() {
    let scale = 3;
    let rect1 = Rectangle{
        width: dbg!(25 * scale),
        height: 42,
    };

    println!("rect1 is {rect1:#?}");

    println!(
        "The are of the rectangle is {} square pixels",
        area(&rect1)
    );

    dbg!(&rect1);
}

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn area(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}
