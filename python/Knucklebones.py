from typing import List
from random import randint

class Knucklebones():
    def __init__(self) -> None:
        self.player_one_board: List[List[int]] = [[1,2,3],[1,2,3],[1,2,3]]
        self.player_two_board: List[List[int]] = [[0,0,0],[0,0,0],[0,0,0]]
    
    def start(self) -> None:
        print("starting game...")
        
    def get_roll(self) -> int:
        return randint(1, 6)
        
    def display(self) -> None:
        b1 = self.player_one_board
        b2 = self.player_two_board
        
        print("Player One:")
        print(f'|{b1[0][0]}| |{b1[1][0]}| |{b1[2][0]}|')
        print(f'|{b1[0][1]}| |{b1[1][1]}| |{b1[2][1]}|')
        print(f'|{b1[0][2]}| |{b1[1][2]}| |{b1[2][2]}|')
        
        print()
        
        print("Player Two:")
        print(f'|{b2[0][0]}| |{b2[1][0]}| |{b2[2][0]}|')
        print(f'|{b2[0][1]}| |{b2[1][1]}| |{b2[2][1]}|')
        print(f'|{b2[0][2]}| |{b2[1][2]}| |{b2[2][2]}|')
