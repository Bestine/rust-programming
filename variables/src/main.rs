fn main() {
    // Mutability
    let mut x = 5;
    println!("The value of x is: {x}");

    x = 6;
    println!("The value of x is: {x}");

    // Constants
    const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
    println!("Three hours in seconds: {THREE_HOURS_IN_SECONDS}");

    // Shadowing
    let y = 10; 

    let y = y + 4;

    {
        let y = y * 3; 
        println!("The value of y in the inner scope is: {y}");
    }

    println!("The value of y is: {y}");

    // Use shadowing to create a new variable with the same name 
    // but a different data type
    let spaces = "   ";
    let spaces = spaces.len();
    println!("Spaces: {spaces}");
    
    // // However if you use 'mut' a compile-time error arises
    // let mut spaces = "   ";
    // spaces = spaces.len();
}