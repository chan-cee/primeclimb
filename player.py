import random
import state
from board import *
from constants import *


class Player:
  def __init__(self, player_symbol):
    self.player_symbol = player_symbol
    self.pawns = [Pawn(player_symbol), Pawn(player_symbol)]
    self.cards = []

  def set_other_player(self, other_player):
    self.other_player = other_player

  def play_move(self, board : Board):
    if board.power_cards_mode:
      return self.play_move_power_card(board)
    else:
      return self.play_move_normal(board)

  def play_move_normal(self, board: Board):
    print(f"It is now player {self.player_symbol}'s turn.\n")
    self.display_current_pawns(self.pawns)
    while True:
      user_action = input("What do you want to do? r to roll dice: ")
      if user_action == "r":
        return self.play_dice(board)
      else:
        print("That is not a valid move!\n")


  def play_move_power_card(self, board: Board):
    print(f"It is now player {self.player_symbol}'s turn.\n")
    self.display_current_pawns(self.pawns)
    self.display_current_cards(self.cards)

    while True:
      user_action = input("What do you want to do? r to roll dice: ")
      if user_action == "r":
        return self.play_dice(board)
      else:
        print("That is not a valid move!\n")

  def play_dice(self, board: Board):
    dices = self.roll_and_choose_dice()

    for dice in dices:
      move_complete = False

      while not move_complete:
        self.prompt_choose_execute_card(board)

        pawn_choice = self.choose_pawn(self.pawns)
        action = self.choose_operation()
        move = Move(dice, pawn_choice, action)
        is_valid_move, error = board.validate_move(move.dice_roll, move.pawn, move.operation)

        if is_valid_move:
          move_complete = True
          result = board.apply_move(move.dice_roll, move.pawn, move.operation)
          print(result)
          if board.check_win(self.player_symbol):
            return [] # We leave it to state.py to manage victory conditions
        else:
          print(error)
          
    self.prompt_choose_execute_card(board)
    return [] # Return an empty list of moves as they have been applied already.
  
  def roll_and_choose_dice(self):
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    dices = [first_dice, second_dice]
    dice_string = [str(first_dice), str(second_dice)]
    print(f"You got dice rolls {first_dice} and {second_dice}.\n")

    if first_dice == second_dice:
      print(f"You get to roll the dice 4 times!")
      return [first_dice, first_dice, first_dice, first_dice]

    dice_choice = None

    while dice_choice not in dice_string:
      dice_choice = input("Which dice to use first? ")
      if dice_choice not in dice_string:
        print("Enter a valid dice number!\n")

    dice_choice_int = int(dice_choice)
    dices.remove(dice_choice_int)
    other_choice = dices[0]

    return [dice_choice_int, other_choice]

  def choose_pawn(self, pawns):
    pawn_one, pawn_two = pawns
    if pawn_one.square.number == END_SQUARE:
      return pawn_two
    
    if pawn_two.square.number == END_SQUARE:
      return pawn_one

    pawn_numbers = ["1", "2"]
    pawn_choice = None
    pawn_index_int = None

    while pawn_choice not in pawn_numbers:
      pawn_choice = input(f"Which pawn to use: ")
      if pawn_choice not in pawn_numbers:
        print("Enter a valid pawn number!\n")

    pawn_index_int = int(pawn_choice) - 1
    return pawns[pawn_index_int]
  
  def choose_operation(self):
    OPERATION_CHOICES = ["a", "s", "m", "d"]

    operation_choice = None
    while operation_choice not in OPERATION_CHOICES:
      print("What math operation do you want to apply on your pawn?")
      operation_choice = input(f"Choose a, s, m or d: ")
      if operation_choice not in OPERATION_CHOICES:
        print("Enter a valid math operation!")

    return operation_choice

  def add_card(self, card):
    self.cards.append(card)

  def prompt_choose_execute_card(self, board):
    if len(self.cards) == 0:
      return
    
    user_action = input("Do you want to use a keeper card? Write y to use: ")
    if user_action == "y":
      card = self.choose_card()
      card.execute(board, self, self.other_player)

  def choose_card(self):
    if len(self.cards) == 1:
      card = self.cards[0]
      self.cards.remove(card)
      return card
    
    card_choices = [str(i + 1) for i in range(len(self.cards))]

    card_choice = None
    while card_choice not in card_choices:
      card_choice = input(f"Which card number will you like to pick: ")
      if card_choice not in card_choices:
        print("Enter a valid card index!")

    card_choice_int = int(card_choice) - 1
    card = self.cards[card_choice_int]
    self.cards.remove(card)
    return card
  
  def display_current_pawns(self, pawns):
    output_string = ""
    for i in range(NUMBER_OF_PAWNS):
      output_string += f"Pawn {i + 1} is on square {pawns[i].square.number}.\n"
    print(output_string)

  def display_current_cards(self, cards):
    output_string = "Keeper cards available:\n"
    for i in range(len(cards)):
      output_string += f"Card {i + 1}: {cards[i].description()}.\n"
    print(output_string)

class PlayerAI:
  def __init__(self, player_symbol) -> None:
    self.player_symbol = player_symbol
    self.pawns = [Pawn(player_symbol), Pawn(player_symbol)]

  def play_move(self, board: Board): # Should return a list of valid Moves that needs to be made by the AI
    pass

class Move:
  def __init__(self, dice_roll, pawn, operation):
    self.dice_roll = dice_roll
    self.pawn = pawn
    self.operation = operation 

class Pawn:
  def __init__(self, player_symbol):
    self.player_symbol = player_symbol
    self.square = None

  def __str__(self):
    return self.player_symbol

  def set_square(self, square):
    self.square = square