use std::io::{stdout, Write};

use rand::Rng;

pub struct Knucklebones {
    player_one_board: [[i32; 3]; 3],
    player_two_board: [[i32; 3]; 3],

    player_one_score: i32,
    player_two_score: i32,

    game_over: bool,
    starting_player: i32,
    current_player: i32,
}

impl Knucklebones {
    // TODO: make static
    fn get_roll(&self) -> i32 {
        rand::thread_rng().gen_range(1..7)
    }

    // TODO: make static
    fn clear(&self) {
        print!("{}[2J", 27 as char);
        stdout().flush().unwrap();
    }

    pub fn new() -> Knucklebones {
        let starting_player = rand::thread_rng().gen_range(0..2);

        return Knucklebones {
            player_one_board: [[0; 3]; 3],
            player_two_board: [[0; 3]; 3],

            player_one_score: 0,
            player_two_score: 0,

            game_over: false,
            starting_player,
            current_player: starting_player,
        };
    }

    pub fn start(&mut self) {
        println!("starting game...");
        println!("player {} starts.", self.starting_player + 1);

        while !self.game_over {
            if self.is_board_full() {
                // TODO: fix this winner is not always the player with the highest
                //  score because one player may have a board full of low numbers
                let winner = {
                    if self.player_one_score > self.player_two_score {
                        1
                    } else {
                        2
                    }
                };
                println!("The winner is: Player {}", winner);
                self.game_over = true;
            }

            self.display();
            let roll = self.get_roll();

            loop {
                if self.is_board_full() {
                    self.game_over = true;
                    break;
                }

                // TODO: dont clear the invalid input message
                // self.clear();
                // self.display();

                print!("\nplayer {}: where do you want to put your {}? ", self.current_player + 1, roll);
                let mut input = String::new();
                std::io::stdin().read_line(&mut input).unwrap();
                let input = input.trim();

                println!("input: {}", input);

                self.current_player = {
                    if self.current_player == 0 {
                        1
                    } else {
                        0
                    }
                };

                // self.clear();
                self.calculate_score();
            }
        }
        println!("game over!");
    }

    fn is_board_full(&self) -> bool {
        for row in 0..3 {
            for col in 0..3 {
                if self.player_one_board[row][col] == 0 {
                    return false;
                }
            }
        }
        return true;
    }

    fn calculate_score(&mut self) {
        let mut player_one_score = 0;
        let mut player_two_score = 0;

        for row in 0..3 {
            for col in 0..3 {
                if self.player_one_board[row][col] == 1 {
                    player_one_score += 1;
                }
                if self.player_two_board[row][col] == 1 {
                    player_two_score += 1;
                }
            }
        }

        self.player_one_score = player_one_score;
        self.player_two_score = player_two_score;
    }

    fn display(&self) {
        println!("\nPlayer One: {}", self.player_one_score);
        for row in 0..3 {
            for col in 0..3 {
                print!("| {} ", self.player_one_board[row][col]);
            }
            print!("|\n");
        }

        println!("\nPlayer Two: {}", self.player_two_score);
        for row in 0..3 {
            for col in 0..3 {
                print!("| {} ", self.player_two_board[row][col]);
            }
            print!("|\n");
        }
    }
}