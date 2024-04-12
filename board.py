import math
from utils import *
from square import *
from constants import *
from deck import *

class Board:
  def __init__(self):
    self.board = [MiddleSquare(i + 1) for i in range(NUMBER_OF_SQUARES)]
    self.start_square = StartSquare()
    self.end_square = EndSquare()
    self.power_cards_mode = False

  def initialize_deck(self):
    self.power_cards_mode = True
    self.deck = Deck()

  def check_win(self, symbol):
    count = 0
    for pawn in self.end_square.pawns:
      if pawn.player_symbol == symbol:
        count += 1

    return count == 2

  def find_prime_squares(self, symbol):
    output_squares = []

    for square in self.board:
      if str(square.pawn) == symbol and is_prime(square.number) and square.number > 10:
         output_squares.append(square)

    return output_squares

  def get_pawn_squares(self, player_symbol):
    output_squares = []
    for pawn in self.start_square.pawns:
      if str(pawn) == player_symbol:
         output_squares.append(self.start_square)

    for pawn in self.end_square.pawns:
      if str(pawn) == player_symbol:
         output_squares.append(self.end_square)

    for square in self.board:
      if str(square.pawn) == player_symbol:
         output_squares.append(square)

    return output_squares

  def place_pawn(self, pawn, number):
    square = self.get_square_from_number(number)
    square.add_pawn(pawn)

  def move_pawn(self, pawn, original_square : Square, result_square: Square):
    result_message = f"Moving pawn from {original_square.number} to {result_square.number}\n"

    original_square.remove_pawn(pawn)
    if not result_square.is_end_square() and not result_square.is_start_square() and result_square.has_pawn():
      result_pawn = result_square.get_pawn()
      self.move_pawn(result_pawn, result_square, self.start_square)
      result_message += f"Knocked other pawn from {result_square.number} to {self.start_square.number}\n"

    result_square.add_pawn(pawn)

    return result_message

  def get_square_from_number(self, number):
    if number == START_SQUARE:
      return self.start_square
    elif number == END_SQUARE:
      return self.end_square
    else:
      return self.board[number - 1]
    
  def validate_move(self, dice_choice, pawn, operation_choice): # return success, error message

    square = pawn.square
    final_number = get_number_from_operation(operation_choice, square.number, dice_choice)

    if final_number > END_SQUARE:
      return False, "You cannot exceed square 101\n"
    
    if final_number < START_SQUARE:
      return False, "You cannot go below square 0\n"
    
    if final_number - math.floor(final_number) != 0:
      return False, "You cannot divide by that number\n"
    
    return True, "Good"

  def apply_move(self, dice_choice, pawn, operation_choice): # returns result of move.
    square = pawn.square
    final_number = get_number_from_operation(operation_choice, square.number, dice_choice)
    result_square = self.get_square_from_number(final_number)
    result_message = self.move_pawn(pawn, square, result_square)
    return result_message

  def print_board(self):
    horizontal_rule = '+' + ('-'*3 + '+') * COL
    print(self.start_square)
    for i in range(ROW):
      print(horizontal_rule)
      print('| ' +  ' | '.join(' ' if str(self.board[i * ROW + j]) == '_' else str(self.board[i * ROW + j]) for j in range(COL)) + ' |')
    print(horizontal_rule)
    print(self.end_square)

  