fn main() {
    let mut user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };

    user1.email = String::from("anotheruser@example.com");

    println!("User Email: {0}", user1.email);

    // Create a struct from the function `build_user`
    let user2 = build_user(
        String::from("bokinda@example.com"), 
        String::from("bo")
    );

    println!("Second User Name: {0}", user2.username);

    // Create a struct from other structs instances - affects ownership
    // since values are borrowed
    let user3 = User{
        active: user1.active, 
        username: user1.username,
        email: String::from("another@example.com"),
        sign_in_count: user1.sign_in_count,
    };

    println!(
        "Third User, Name: {0}, Email: {1}",
        user3.username,
        user3.email
        );

    // Create a struct from other structs instance using the 
    //update syntax - it also affects ownership as above
    let user4 = User{
        email: String::from("fourthuser@example.com"),
        ..user3
    };

    println!(
        "Fourth User, Name: {0}, email: {1}",
        user4.username,
        user4.email
    );

    // Use tuple structs 
    let white = Color(255, 255, 255);
    let origin = Point(0, 0, 0);

    println!("red-value White(rgb); {}", white.0);
    println!("Z-point on 3D Origin: {}", origin.2);

    // Use the unit-like structs - don't have any fields
    let _subject = AlwaysEqual;
}

struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username,
        email,
        sign_in_count: 1,
    }
}

// Create tuple structs 
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

// Unit-like struct 
struct AlwaysEqual;