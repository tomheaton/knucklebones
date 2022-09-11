from typing import List
from random import randint


class Knucklebones():
    def __init__(self) -> None:
        self.player_one_board: List[List[int]] = [[0,0,0],[0,0,0],[0,0,0]]
        self.player_two_board: List[List[int]] = [[0,0,0],[0,0,0],[0,0,0]]

        self.game_over: bool = False
        self.starting_player: int = randint(0, 1)
        self.current_player: int = self.starting_player
    
    def start(self) -> None:
        print("starting game...")
        
        while not self.game_over:
            if self.is_board_full():
                self.game_over = True
    
            self.display();
            print(f"player {self.starting_player + 1} starts.")
            roll = self.get_roll()
            
            while True:
                column = int(input(f"player {self.current_player + 1}: where do you want to put your {roll}"))
                if column in [1,2,3]:
                    break
                
            # TODO: place roll in column
            
            print(f"{column = }")
            
        print("game over")

    def is_board_full(self) -> bool:
        b1 = self.player_one_board
        b2 = self.player_two_board

        if 0 in (b1[0] + b1[1] + b1[2]):
            return False
        
        if 0 in (b2[0] + b2[1] + b2[2]):
            return False
            
        return True
        
    def get_roll(self) -> int:
        return randint(1, 6)
        
    def display(self) -> None:
        b1 = self.player_one_board
        b2 = self.player_two_board
        
        print("Player One:")
        print(f"|{b1[0][0]}| |{b1[1][0]}| |{b1[2][0]}|")
        print(f"|{b1[0][1]}| |{b1[1][1]}| |{b1[2][1]}|")
        print(f"|{b1[0][2]}| |{b1[1][2]}| |{b1[2][2]}|")
        
        print()
        
        print("Player Two:")
        print(f"|{b2[0][0]}| |{b2[1][0]}| |{b2[2][0]}|")
        print(f"|{b2[0][1]}| |{b2[1][1]}| |{b2[2][1]}|")
        print(f"|{b2[0][2]}| |{b2[1][2]}| |{b2[2][2]}|")
