use knucklebones::Knucklebones;

pub mod knucklebones;

fn main() {
    println!("knucklebones");
    let mut knucklebones = Knucklebones::new();
    knucklebones.start();
}
