fn main() {
    println!("Hello, world!");

    another_function();

    // Try the function with a paramater
    function_with_param(28);

    // Functions with multiple parameters 
    print_labeled_measurements(5, 'h');

    // Statements and expressions 
    let y = {
        let x = 5;
        x + 2 //expressions do not include an ending semicolon
    };

    println!("The value of y is: {y}");

    // return function without return keyword testing 
    let m = five();
    println!("The value of m is: {m}");

    // function with an early return with a return keyword 
    let label = early_return();
    println!("The length is: 7{label}");

}

fn another_function(){
    println!("Another Function");
}

// Modify the above function to accept arguments referred to
// as parameters 
fn function_with_param(x: i32){
    println!("The value of x is: {x}");
}

// try a function with multiple parameters 
fn print_labeled_measurements(value: i32, unit_label: char){
    println!("The measurement is: {value}{unit_label}");
}

// Functions with return values 
// - without a return word
fn five() -> i32 {
    5
}

// with a return keyword 
fn early_return() -> char{
    let my_label = 'C';
    return my_label; //early return
}