fn main() {
    let rect1 = Rectangle{
        width: 25,
        height: 48,
    };

    // Calculate AREA 
    println!(
        "The area of rectangle is {} square pixels.",
        rect1.area()
    );

    // Calculate PERIMETER 
    println!(
        "The perimeter of rectangle is {} pixels.",
        rect1.perimeter()
    );
    
}

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    // Calculate area 
    fn area(&self) -> u32 {
        self.width * self.height
    }

    // Calculate perimeter
    fn perimeter(&self) -> u32{
        2*(self.width + self.height)
    }
}
