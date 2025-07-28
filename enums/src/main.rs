fn main() {
    let home = IpAddr::V4(127, 0, 0, 1);
    let loopback = IpAddr::V6(String::from("::1"));

    // route(home);
    // route(loopback);

    let m = Message::Write(String::from("Hello"));
    m.call();
}

enum IpAddr {
    V4(u8, u8, u8, u8),
    V6(String),
}

// fn route(ip_kind: IpAddr) {}

enum Message {
    Quit, 
    Move {
        x: i32, 
        y: i32
    }, 
    Write(String),
    ChangeColor(i32, i32, i32),
}

// Create a method call on an enum `Message`
impl Message{
    fn call(&self) {
        // define method body here
    }
}