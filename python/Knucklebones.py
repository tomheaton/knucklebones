import os

from typing import List
from random import randint
from collections import Counter


class Knucklebones():
    def __init__(self) -> None:
        self.player_one_board: List[List[int]] = [[0,0,0],[0,0,0],[0,0,0]]
        self.player_two_board: List[List[int]] = [[0,0,0],[0,0,0],[0,0,0]]

        self.player_one_score: int = 0
        self.player_two_score: int = 0

        self.game_over: bool = False
        self.starting_player: int = randint(0, 1)
        self.current_player: int = self.starting_player
    
    def start(self) -> None:
        print("starting game...")
        print(f"player {self.starting_player + 1} starts.")

        while not self.game_over:
            if self.is_board_full():
                # TODO: fix this
                # winner is not always the player with the highest score
                # because one player may have a board full of low numbers
                winner = 1 if self.player_one_score > self.player_two_score else 2
                print(f"The winner is: Player {winner}")
                self.game_over = True
    
            self.display();
            roll = self.get_roll()
            
            while True:
                if self.is_board_full():
                    self.game_over = True
                    break

                column = input(f"\nplayer {self.current_player + 1}: where do you want to put your {roll}? ")
                if column.isdigit() and int(column) in [1,2,3]:
                    column_index = int(column) - 1
            
                    if self.current_player == 0:
                        if 0 in self.player_one_board[column_index]:
                            free_row = self.player_one_board[column_index].index(0) 
                            self.player_one_board[column_index][free_row] = roll
                            
                            for index, number in enumerate(self.player_two_board[column_index]):
                                if number == roll:
                                    self.player_two_board[column_index][index] = 0

                            break
                        else:
                            print("column is full")

                    if self.current_player == 1:
                        if 0 in self.player_two_board[column_index]:
                            free_row = self.player_two_board[column_index].index(0)
                            self.player_two_board[column_index][free_row] = roll
                            
                            if roll in self.player_one_board[column_index]:
                                for index, number in enumerate(self.player_one_board[column_index]):
                                    if number == roll:
                                        self.player_one_board[column_index][index] = 0
        
                            break
                        else:
                            print("column is full")
                else:
                    print("invalid column")
            
            # TODO: clear and display again to remove incorrect input prints

            self.current_player = 1 if self.current_player == 0 else 0
            
            self.clear()
            self.calculate_score()

        print("game over")
        
    def calculate_score(self) -> None:
        b1 = self.player_one_board
        b2 = self.player_two_board
        
        p1_score = 0
        p2_score = 0
        
        for column in b1:
            for number, count in Counter(column).items():
                if number > 0:
                    p1_score += number * count**2

        for column in b2:
            for number, count in Counter(column).items():
                if number > 0:
                    p2_score += number * count**2
            
        self.player_one_score = p1_score
        self.player_two_score = p2_score

    def is_board_full(self) -> bool:
        b1 = self.player_one_board
        b2 = self.player_two_board

        return not 0 in (b1[0] + b1[1] + b1[2] + b2[0] + b2[1] + b2[2])
        
    def get_roll(self) -> int:
        return randint(1, 6)
    
    @staticmethod
    def clear() -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def display(self) -> None:
        b1 = self.player_one_board
        b2 = self.player_two_board
        
        print()

        print(f"Player One: {self.player_one_score}")
        print(f"| {b1[0][0]} | {b1[1][0]} | {b1[2][0]} |")
        print(f"| {b1[0][1]} | {b1[1][1]} | {b1[2][1]} |")
        print(f"| {b1[0][2]} | {b1[1][2]} | {b1[2][2]} |")
        
        print()
        
        print(f"Player Two: {self.player_two_score}")
        print(f"| {b2[0][0]} | {b2[1][0]} | {b2[2][0]} |")
        print(f"| {b2[0][1]} | {b2[1][1]} | {b2[2][1]} |")
        print(f"| {b2[0][2]} | {b2[1][2]} | {b2[2][2]} |")
