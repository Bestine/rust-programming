fn main() {
    // --------------BASIC LOOP --------------
    // loop {
    //     println!("again!");
    // }

    // ----------RETURNING VALUES FROM LOOPS -------
    let mut age = 0;

    let current_age = loop{
        age+=1;

        if age == 28{
            break age;
        }
    };

    println!("Current Age: {current_age}");
}
