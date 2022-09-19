use std::io;


fn main() {
    println!("knucklebones");

    loop {
        println!("Please enter chosen column: ");
  
        let mut column_string = String::new();
        io::stdin().read_line(&mut column_string).unwrap();
        
        let column: i32 = column_string.parse().unwrap(); 

        println!("Chosen column: {}", column);
    }
}
