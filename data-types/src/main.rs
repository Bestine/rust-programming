fn main() {
    // Trial
    let guess: u32 = "42".parse().expect("Not a number!");
    println!("Guess: {guess}");

    // Scalar Types: Integers, floating-point, numbers, Booleans, characters
    // - Floating point types 
    let _x = 2.0; //f64

    let _y: f32 = 3.0; //f32

    // Numeric operations 
    // - sum
    let _sum = 5 + 10; 

    // - subtration 
    let _difference = 99.5 - 4.3;

    // - division 
    let _quotient = 56.7/32.2;
    let _truncated = -5/3; //results in -1 

    // - Multiplication 
    let _product = 4 * 30; 

    // - remainder 
    let _remainder = 43 % 5;

    
    // Boolean types  
    let _t = true; 
    let _f: bool = false;


    // Character types 
    let _c = 'z';
    let _z: char = 'Z'; // with explicit type annotation 
    let heart_eyed_cat = '😻';

    println!("Heart-eyed-cat: {heart_eyed_cat}");

    // COMPOUND TYPES 
    // - tuple : once declared cannot grow or shrink in size
    let tup: (i32, f64, u8) = (500, 6.4, 1);

    // get the individuals of a tup : destructuring 
    let (_x, y, _z) = tup; 
    println!("The value of y is: {y}");

    // access tuple elements
    let x: (i32, f64, u8) = (500, 6.4, 1);

    let _five_hundred = x.0;

    let _six_point_four = x.1;

    let _one = x.2;

    // Arrays
    let _a = [1, 2, 3, 4, 5];
}
