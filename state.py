import math
from utils import *
from square import *
from constants import *
from board import *
import player

class Engine:

  def __init__(self):
    self.state = State()
    self.global_playing = False
  
  def run(self):
    display_introduction()
    print(GAME_MODE_STRING)
    game_mode = input("Game mode?: ")
    if game_mode == '2':
      # Two Player
      self.game_mode = 2
      self.power_cards_mode = False
    elif game_mode == '3':
      # Two Player with power Cards
      self.game_mode = 3
      self.power_cards_mode = True
    elif game_mode == '4':
      # Single AI
      self.game_mode = 4
      self.power_cards_mode = False
    elif game_mode == '5':
      # Player vs AI
      self.game_mode = 5
      self.power_cards_mode = False
    else:
      # Single Player
      self.game_mode = 1
      self.power_cards_mode = False
      
    while True:
      self.play_game()
      if input("Do you want to start a new game? Write y to continue: ") != 'y':
        break
    display_end()
    
  def play_game(self):
    self.state.intialize_clean_state(self.game_mode, self.power_cards_mode)
    self.global_playing = True

    turn = 0 # 0 is for first player, 1 is for odd.
    while self.global_playing:
      player = self.state.players[turn]
      other_player = self.state.players[(turn + 1) % 2]
      for pawn in player.pawns:
        pawn.reset_square()

      self.state.board.print_board()
      moves = player.play_move(self.state.board)

      if self.state.board.check_win(player.player_symbol): # We check for player victories
        print(f"Player {player.player_symbol} won!\n")
        self.global_playing = False
        break

      for move in moves: # For AI moves as player returns empty moves.
        self.state.board.apply_move(move.dice_roll, move.pawn, move.operation)

        if self.state.board.check_win(player.player_symbol): # We check for AI victories
          print(f"Player {player.player_symbol} won!\n")
          self.global_playing = False
          break

      if self.power_cards_mode:
        prime_squares = self.state.board.find_new_prime_squares(player.player_symbol)
        if len(prime_squares) > 0:
          card = self.state.board.deck.draw_card()
          print(f"Player {player.player_symbol} drew card \"{card.description()}\"!\n")

          if card.is_keeper():
            print(f"Player {player.player_symbol} keeps the keeper card!\n")
            player.add_card(card)

          elif card.is_roll_again():
            print(f"Player {player.player_symbol} rolls again!\n")
            continue

          else:
            print(f"An action card is drawn!\n")
            card.execute(self.state.board, player, other_player)

      if not self.global_playing:
        break
      
      player.enable_operations()
      if other_player.player_symbol == PLAYER_DUMMY:
        turn = 0
      else:
        turn = (turn + 1) % 2
      


class State:
  def __init__(self):
    pass

  def intialize_clean_state(self, game_mode, power_cards_mode):
    self.initialize_board()
    self.initialize_players(game_mode)
    if power_cards_mode:
      self.board.initialize_deck()

    self.place_pawns_on_start(self.players[0], self.players[1])

  def initialize_board(self):
    self.board = Board()

  def initialize_players(self, game_mode):
    if game_mode == 1:
      player_one = player.Player(PLAYER_X)
      player_two = player.Player(PLAYER_DUMMY)
      self.players = [player_one, player_two]
    elif game_mode == 2:
      player_one = player.Player(PLAYER_X)
      player_two = player.Player(PLAYER_Y)
      self.players = [player_one, player_two]
    elif game_mode == 3:
      player_one = player.Player(PLAYER_X)
      player_two = player.Player(PLAYER_Y)
      player_one.set_other_player(player_two)
      player_two.set_other_player(player_one)
      self.players = [player_one, player_two]
    elif game_mode == 4:
      player_one = player.PlayerAI(PLAYER_AI)
      player_two = player.Player(PLAYER_DUMMY)
      self.players = [player_one, player_two]
    elif game_mode == 5:
      player_one = player.Player(PLAYER_X)
      player_two = player.PlayerAI(PLAYER_AI)
      self.players = [player_one, player_two]

  def place_pawns_on_start(self, player_one, player_two):
    for i in range(NUMBER_OF_PAWNS):
      self.board.place_pawn(player_one.pawns[i], START_SQUARE)
      self.board.place_pawn(player_two.pawns[i], START_SQUARE)


