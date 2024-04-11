import math
from utils import *
from square import *
from constants import *
import player

global_playing = False
  
class Engine:

  def __init__(self):
    self.state = State()
  
  def run(self):
    display_introduction()
    while True:
      self.play_game()
      if input("Do you want to start a new game? Write y to continue: ") != 'y':
        break
    display_end()
  
  def play_game(self):
    self.state.intialize_clean_state()
    global global_playing
    global_playing = True

    while global_playing:
      for player in self.state.players:
        self.state.board.print_board()
        if not player.play_move(self.state.board):
          print("Quitting game!\n")
          global_playing = False
          break

        if not global_playing:
          break


class State:
  def __init__(self):
    pass

  def intialize_clean_state(self):
    self.initialize_board()
    self.initialize_players()
    self.place_pawns_on_start(self.players[0], self.players[1])

  def initialize_board(self):
    self.board = Board()

  def initialize_players(self):
    player_one = player.Player(PLAYER_X)
    player_two = player.Player(PLAYER_Y)
    self.players = [player_one, player_two]
    
  def place_pawns_on_start(self, player_one, player_two):
    for i in range(NUMBER_OF_PAWNS):
      self.board.place_pawn(player_one.pawns[i], START_SQUARE)
      self.board.place_pawn(player_two.pawns[i], START_SQUARE)

class Board:
  def __init__(self):
    self.board = [MiddleSquare(i + 1) for i in range(NUMBER_OF_SQUARES)]
    self.start_square = StartSquare()
    self.end_square = EndSquare()

  def check_win(self, symbol):
    count = 0
    for pawn in self.end_square.pawns:
      if pawn.player_symbol == symbol:
        count += 1

    return count == 2

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
    
    print(f"Moving pawn from {original_square.number} to {result_square.number}\n")

    original_square.remove_pawn(pawn)
    if not result_square.is_end_square() and not result_square.is_start_square() and result_square.has_pawn():
      result_pawn = result_square.get_pawn()
      self.move_pawn(result_pawn, result_square, self.start_square)
      print(f"Knocked other pawn from {result_square.number} to {self.start_square.number}\n")

    result_square.add_pawn(pawn)

  def get_square_from_number(self, number):
    if number == START_SQUARE:
      return self.start_square
    elif number == END_SQUARE:
      return self.end_square
    else:
      return self.board[number - 1]
    
  def apply_operation(self, pawn, dice_choice, operation_choice):
    final_number = None
    square = pawn.square

    if operation_choice == "a":
      final_number = square.number + dice_choice
    elif operation_choice == "s":
      final_number = square.number - dice_choice
    elif operation_choice == "m":
      final_number = square.number * dice_choice
    elif operation_choice == "d":
      final_number = square.number / dice_choice

    if final_number > END_SQUARE:
      raise Exception("You cannot exceed square 101\n")
    elif final_number < START_SQUARE:
      raise Exception("You cannot go below square 0\n")
    elif final_number - math.floor(final_number) != 0:
      raise Exception("You cannot divide by that number\n")
    else:
      result_square = self.get_square_from_number(final_number)
      self.move_pawn(pawn, square, result_square)

    global global_playing
    if self.check_win(pawn.player_symbol):
      print(f"Player {pawn.player_symbol} won!\n")
      global_playing = False

  def print_board(self):
    horizontal_rule = '+' + ('-'*3 + '+') * COL
    print(self.start_square)
    for i in range(ROW):
      print(horizontal_rule)
      print('| ' +  ' | '.join(' ' if str(self.board[i * ROW + j]) == '_' else str(self.board[i * ROW + j]) for j in range(COL)) + ' |')
    print(horizontal_rule)
    print(self.end_square)

  
