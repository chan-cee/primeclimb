import random
from constants import *
from main import Board

class Player:
  def __init__(self, player_symbol):
    self.player_symbol = player_symbol
    self.pawns = [Pawn(player_symbol), Pawn(player_symbol)]

  def play_move(self, board : Board):
    print(f"It is now player {self.player_symbol}'s turn.\n")
    self.display_current_pawns(self.pawns)
    while True:
      user_action = input("What do you want to do? r to roll dice, q to quit: ")
      if user_action == "r":
        self.roll_dice(board, self.pawns)
        return True
      elif user_action == "q":
        return False
      else:
        print("That is not a valid move!\n")
  
  def roll_dice(self, board: Board, pawns):
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    dices = [first_dice, second_dice]
    dice_string = [str(first_dice), str(second_dice)]
    print(f"You got dice rolls {first_dice} and {second_dice}.\n")

    dice_choice = None

    while dice_choice not in dice_string:
      dice_choice = input("Which dice to use first? ")
      if dice_choice not in dice_string:
        print("Enter a valid dice number!\n")

    dice_choice_int = int(dice_choice)
    dices.remove(dice_choice_int)
    other_choice = dices[0]

    self.play_dice(dice_choice_int, board, pawns)
    self.play_dice(other_choice, board, pawns)

  def play_dice(self, dice, board: Board, pawns):
    pawn_numbers = ["1", "2"]

    while True:
      pawn_choice = None
      while pawn_choice not in pawn_numbers:
        pawn_choice = input(f"Which pawn to use for dice {dice}: ")
        if pawn_choice not in pawn_numbers:
          print("Enter a valid pawn number!\n")

      operation_choice = None
      while operation_choice not in OPERATION_CHOICES:
        print("What math operation do you want to apply on your pawn?")
        operation_choice = input(f"Choose a, s, m or d: ")
        if operation_choice not in OPERATION_CHOICES:
          print("Enter a valid math operation!")
      
      pawn_index_int = int(pawn_choice) - 1

      try:
        board.apply_operation(pawns[pawn_index_int], dice, operation_choice)
        break
      except Exception as e:
        print(e)
        
  def display_current_pawns(self, pawns):
    output_string = ""
    for i in range(NUMBER_OF_PAWNS):
      output_string += f"Pawn {i + 1} is on square {pawns[i].square.number}.\n"
    print(output_string)

class Pawn:
  def __init__(self, player_symbol):
    self.player_symbol = player_symbol
    self.square = None

  def __str__(self):
    return self.player_symbol

  def set_square(self, square):
    self.square = square