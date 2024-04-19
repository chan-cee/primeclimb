import math
from utils import *
from square import *
from constants import *
from deck import *
import player

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

  def find_new_prime_squares(self, symbol):
    output_squares = []

    for square in self.board:
      pawn = square.pawn
      if str(pawn) == symbol and is_prime_above_10(square.number) and pawn.square != pawn.previous_square:
         output_squares.append(square)

    return output_squares
  
  def get_pawns(self, player_symbol):
    pawns = [None, None]
    for i in range(102):
      square = self.get_square_from_number(i)
      if i == 0 or i == 101:
        square_pawns = square.get_pawn()
        for p in square_pawns:
          if p.player_symbol == player_symbol and p.index == 0:
            pawns[0] = p
          elif p.player_symbol == player_symbol and p.index == 1:
            pawns[1] = p

      elif square.has_pawn():
        p = square.get_pawn()
        if p.player_symbol == player_symbol and p.index == 0:
          pawns[0] = p
        elif p.player_symbol == player_symbol and p.index == 1:
          pawns[1] = p

    return pawns
  
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

  def swap_pawns(self, pawn_one, pawn_two):
    result_message = f"Swapping pawns on square {pawn_one.square.number} and square {pawn_two.square.number}\n"
    pawn_one_square = pawn_one.square
    pawn_two_square = pawn_two.square

    pawn_one_square.remove_pawn(pawn_one)
    pawn_two_square.remove_pawn(pawn_two)

    pawn_two_square.add_pawn(pawn_one)
    pawn_one_square.add_pawn(pawn_two)

    return result_message

  def move_pawn(self, pawn, original_square : Square, result_square: Square):
    result_message = f"Moving pawn {pawn.player_symbol} from {original_square.number} to {result_square.number}\n"

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
  
    if final_number - math.floor(final_number) != 0:
      return False, "You cannot divide by that number\n"
    
    return True, "Good"

  def apply_move(self, dice_choice, pawn, operation_choice): # returns result of move.
    square = pawn.square
    final_number = get_number_from_operation(operation_choice, square.number, dice_choice)
    final_number_int = int(final_number)
    result_square = self.get_square_from_number(final_number_int)
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

  def get_copy(self):
    new_board = Board()
    
    for i in range(102):
      old_square = self.get_square_from_number(i)
      new_square = new_board.get_square_from_number(i)
      if i == 0 or i == 101:
        pawns = old_square.get_pawn()
        for p in pawns:
          new_pawn = player.Pawn(p.player_symbol, p.index)
          new_square.add_pawn(new_pawn)

      elif old_square.has_pawn():
        old_pawn = old_square.get_pawn()
        new_pawn = player.Pawn(old_pawn.player_symbol, old_pawn.index)
        new_square.add_pawn(new_pawn)

    return new_board
        
