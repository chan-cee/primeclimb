import random
import math

ROW, COL = 10, 10
START_SQUARE = 0
END_SQUARE = 101
NUMBER_OF_SQUARES = ROW * COL
PLAYER_X, PLAYER_Y = "X", "Y"
NUMBER_OF_PAWNS = 2
OPERATION_CHOICES = ["a", "s", "m", "d"]
GAME_OVER = "GAME_OVER"

global_playing = False

def display_introduction():
  intro_string = "TODO"
  return intro_string

def display_end():
  end_string = "TODO"
  return end_string

class Square:
  def __init__(self, number):
    self.number = number

  def get_pawn(self):
    pass
  
  def add_pawn(self, pawn):
    pass

  def remove_pawn(self, pawn):
    pass

  def has_pawn(self):
    pass

  def is_end_square(self):
    pass
  
  def is_start_square(self):
    pass

class MiddleSquare(Square):
  def __init__(self, number):
    self.pawn = None
    self.number = number

  def __str__(self):
    if self.pawn is None:
      return '_'
    else:
      return str(self.pawn)
    
  def get_pawn(self):
    return self.pawn
  
  def add_pawn(self, pawn):
    self.pawn = pawn
    pawn.set_square(self)
    
  def remove_pawn(self, pawn):
    self.pawn = None
  
  def has_pawn(self):
    return self.pawn is not None

  def is_end_square(self):
    return False
  
  def is_start_square(self):
    return False
  
class StartSquare(Square):
  def __init__(self):
    self.pawns = []
    self.number = START_SQUARE

  def __str__(self):
    rep = "Start Square Pawns:"
    for pawn in self.pawns:
      rep += " " + str(pawn)
    rep += "\n"
    return rep
  
  def get_pawn(self):
    return self.pawns
  
  def add_pawn(self, pawn):
    self.pawns.append(pawn)
    pawn.set_square(self)

  def remove_pawn(self, pawn):
    self.pawns.remove(pawn)

  def has_pawn(self):
    return len(self.pawns) > 0
  
  def is_end_square(self):
    return False
  
  def is_start_square(self):
    return True
  
class EndSquare(Square):
  def __init__(self):
    self.pawns = []
    self.number = END_SQUARE

  def __str__(self):
    rep = "End Square Pawns:"
    for pawn in self.pawns:
      rep += " " + str(pawn)
    rep += "\n"
    return rep
  
  def get_pawn(self):
    return self.pawns
  
  def add_pawn(self, pawn):
    self.pawns.append(pawn)
    pawn.set_square(self)

  def remove_pawn(self, pawn):
    self.pawns.remove(pawn)

  def has_pawn(self):
    return len(self.pawns) > 0
  
  def is_end_square(self):
    return True
  
  def is_start_square(self):
    return False
  
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
    player_one = Player(PLAYER_X)
    player_two = Player(PLAYER_Y)
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
  
if __name__ == "__main__":
  engine = Engine()
  engine.run()