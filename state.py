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
    player_or_ai = input("Play with other player? Write y for yes: ")
    if player_or_ai == 'y':
      self.player_mode = True
      power_cards_choice = input("Play with action cards? Write y for yes: ")
      if power_cards_choice == 'y':
        self.power_cards_mode = True
      else:
        self.power_cards_mode = False
    else:
      self.player_mode = False
      self.power_cards_mode = False
      
    while True:
      self.play_game()
      if input("Do you want to start a new game? Write y to continue: ") != 'y':
        break
    display_end()

  def play_game(self):
    self.state.intialize_clean_state(self.player_mode, self.power_cards_mode)
    self.global_playing = True

    while self.global_playing:
      for player in self.state.players:
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

        if not self.global_playing:
          break


class State:
  def __init__(self):
    pass

  def intialize_clean_state(self, player_mode, power_cards_mode):
    self.initialize_board()
    self.initialize_players(player_mode)
    if power_cards_mode:
      self.board.initialize_deck()

    self.place_pawns_on_start(self.players[0], self.players[1])

  def initialize_board(self):
    self.board = Board()

  def initialize_players(self, player_mode):
    player_one = player.Player(PLAYER_X)
    player_two = player.Player(PLAYER_Y) if player_mode else player.PlayerAI(PLAYER_AI)
    self.players = [player_one, player_two]

  def place_pawns_on_start(self, player_one, player_two):
    for i in range(NUMBER_OF_PAWNS):
      self.board.place_pawn(player_one.pawns[i], START_SQUARE)
      self.board.place_pawn(player_two.pawns[i], START_SQUARE)

