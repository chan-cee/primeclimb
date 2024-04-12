import random
from utils import *
from constants import *

class Deck:
  def __init__(self) -> None:
    self.cards = [
      SendPawnToSixtyFourActionCard(),
      SendPawnToSixtyFourActionCard(),
      SendPawnToSixtyFourActionCard()
    ]

    # self.cards = [
    #   AddSubtractKeeperCard(1),
    #   AddSubtractKeeperCard(2),
    #   AddSubtractKeeperCard(3),
    #   AddSubtractKeeperCard(4),
    #   AddSubtractKeeperCard(5),
    #   AddSubtractKeeperCard(6),
    #   AddSubtractKeeperCard(7),
    #   AddSubtractKeeperCard(8),
    #   AddSubtractKeeperCard(9),
    #   TwoSpacesKeeperCard(),
    #   TwoSpacesKeeperCard(),
    #   SubtractOrDivideKeeperCard(),
    #   SubtractOrDivideKeeperCard(),
    #   RollAgainActionCard(),
    #   RollAgainActionCard(),
    #   RollAgainActionCard(),
    #   AddSubtractFiftyActionCard(),
    #   FiftySubtractTenOrDoubleActionCard(),
    #   AdvanceToNearestPawnActionCard(),
    #   ReverseToNearestPawnActionCard(),
    #   ReverseDigitsActionCard(),
    #   SwitchTwoPawnsActionCard(),
    #   SendPawnToSixtyFourActionCard(),
    #   StealOtherActionCard()
    # ]

    random.shuffle(self.cards)

  def draw_card(self):
    card = self.cards.pop()
    return card

class Card:
  def __init__(self) -> None:
    pass

  def description(self):
    pass

  def is_keeper(self):
    pass

  def is_roll_again(self):
    pass

  def execute(self, board, player, other_player):
    pass
    
class AddSubtractKeeperCard(Card):
  def __init__(self, digit) -> None:
    self.digit = digit
    self.identifier = 1

  def description(self):
    return f"Add or subtract your pawn by {self.digit}"
  
  def is_keeper(self):
    return True
  
  def is_roll_again(self):
    return False

  def execute(self, board, player, other_player):
    valid_operations = ["a", "s"]
    move_complete = False

    while not move_complete:
      pawn_choice = player.choose_pawn(player.pawns, self.digit)
      operation_choice = player.choose_operation(valid_operations)
      move = Move(self.digit, pawn_choice, operation_choice)
      is_valid_move, error = board.validate_move(move.dice_roll, move.pawn, move.operation)

      if is_valid_move:
        move_complete = True
        result = board.apply_move(move.dice_roll, move.pawn, move.operation)
        print(result)
      else:
        print(error)

class TwoSpacesKeeperCard(Card):
  def __init__(self) -> None:
    self.identifier = 10

  def description(self):
    return "Send all pawns within two spaces of you back to start"
  
  def is_keeper(self):
    return True
  
  def is_roll_again(self):
    return False
  
  def execute(self, board, player, other_player):
    pawn_choice = player.choose_pawn(player.pawns, "Two spaces card")
    square_number = pawn_choice.square.number

    for i in range(square_number - 2, square_number + 3):
      square = board.get_square_from_number(square_number)
      start_square = board.start_square
      if not square.is_end_square() and i != square_number and square.has_pawn():
        result_message = board.move_pawn(square.pawn, square, start_square)
        print(result_message)

class SubtractOrDivideKeeperCard(Card):
  def __init__(self) -> None:
    self.identifier = 12

  def description(self):
    return "Play this card on an opponent. On their following turn they may only subtract or divide"
  
  def is_keeper(self):
    return True
  
  def is_roll_again(self):
    return False
  
  def execute(self, board, player, other_player):
    other_player.restrict_operations()
    print(f"Restricted player {other_player.player_symbol} operations to subtract and divide.\n")

class RollAgainActionCard(Card):
  def __init__(self) -> None:
    self.identifier = 14

  def description(self):
    return "Roll Again!"
  
  def is_keeper(self):
    return False
  
  def is_roll_again(self):
    return True
  
  def execute(self, board, player, other_player):
    pass

class AddSubtractFiftyActionCard(Card):
  def __init__(self) -> None:
    self.identifier = 17

  def description(self):
    return "If you are above 50, subtract 50. If you are below 50, add 50"
  
  def is_keeper(self):
    return False
  
  def is_roll_again(self):
    return False
  
  def execute(self, board, player, other_player):
    pawn_choice = player.choose_prime_pawns(player.pawns)
    new_number = None
    if pawn_choice.square.number > 50:
      new_number = pawn_choice.square.number - 50
    else:
      new_number = pawn_choice.square.number + 50

    result_square = board.get_square_from_number(new_number)
    result_message = board.move_pawn(pawn_choice, pawn_choice.square, result_square)
    print(result_message)

class FiftySubtractTenOrDoubleActionCard(Card):
  def __init__(self) -> None:
    self.identifier = 18

  def description(self):
    return "If you are above 50, go back ten spaces. If you are below 50, double your number"
  
  def is_keeper(self):
    return False
  
  def is_roll_again(self):
    return False
  
  def execute(self, board, player, other_player):
    pawn_choice = player.choose_prime_pawns(player.pawns)
    new_number = None
    if pawn_choice.square.number > 50:
      new_number = pawn_choice.square.number - 10
    else:
      new_number = pawn_choice.square.number * 2

    result_square = board.get_square_from_number(new_number)
    result_message = board.move_pawn(pawn_choice, pawn_choice.square, result_square)
    print(result_message)

class AdvanceToNearestPawnActionCard(Card):
  def __init__(self) -> None:
    self.identifier = 19

  def description(self):
    return "Advance to the pawn nearest you. Send them back to start"
  
  def is_keeper(self):
    return False
  
  def is_roll_again(self):
    return False
  
  def execute(self, board, player, other_player):
    pawn_choice = player.choose_prime_pawns(player.pawns)
    square_number = pawn_choice.square.number
    forward_list = [i for i in range(square_number + 1, END_SQUARE)]

    for new_square_numbers in forward_list:
      result_square = board.get_square_from_number(new_square_numbers)
      if result_square.has_pawn():
        result_message = board.move_pawn(pawn_choice, pawn_choice.square, result_square)
        print(result_message)

    print("Nothing happened!")

class ReverseToNearestPawnActionCard(Card):
  def __init__(self) -> None:
    self.identifier = 20

  def description(self):
    return "Reverse to the pawn nearest you. Send them back to start"
  
  def is_keeper(self):
    return False
  
  def is_roll_again(self):
    return False
  
  def execute(self, board, player, other_player):
    pawn_choice = player.choose_prime_pawns(player.pawns)
    square_number = pawn_choice.square.number
    backward_list = [i for i in reversed(range(START_SQUARE, square_number))]

    for new_square_numbers in backward_list:
      result_square = board.get_square_from_number(new_square_numbers)
      if result_square.has_pawn():
        result_message = board.move_pawn(pawn_choice, pawn_choice.square, result_square)
        print(result_message)
        return

    print("Nothing happened!")

class ReverseDigitsActionCard(Card):
  def __init__(self) -> None:
    self.identifier = 21

  def description(self):
    return "Reverse the digits in your number"
  
  def is_keeper(self):
    return False
  
  def is_roll_again(self):
    return False
  
  def execute(self, board, player, other_player):
    pawn_choice = player.choose_prime_pawns(player.pawns)
    square_number = pawn_choice.square.number
    reversed_square_number = int("".join(reversed(str(square_number))))
    result_square = board.get_square_from_number(reversed_square_number)
    result_message = board.move_pawn(pawn_choice, pawn_choice.square, result_square)
    print(result_message)

class SwitchTwoPawnsActionCard(Card):
  def __init__(self) -> None:
    self.identifier = 22

  def description(self):
    return "Switch two pawns on the board"
  
  def is_keeper(self):
    return False
  
  def is_roll_again(self):
    return False
  
  def execute(self, board, player, other_player):
    pawn_choice = player.choose_prime_pawns(player.pawns)

    all_pawns_on_board = player.pawns + other_player.pawns
    pawns_on_board = [pawn for pawn in all_pawns_on_board if not pawn.square.is_end_square()]
    pawns_on_board.remove(pawn_choice)
    pawn_numbers = [f"{pawn} ({str(pawn.square.number)})" for pawn in pawns_on_board]

    pawn_index_int = self.choose_swap_pawn_index(pawn_numbers)
    other_pawn = pawns_on_board[pawn_index_int]
    result_message = board.swap_pawns(pawn_choice, other_pawn)
    print(result_message)
  
  def choose_swap_pawn_index(self, pawn_numbers):
    valid_numbers = [str(i + 1) for i in range(len(pawn_numbers))]
    pawn_choice = None
    pawn_index_int = None

    while pawn_choice not in valid_numbers:
      print("These are the pawns that remain:")
      print(pawn_numbers)
      pawn_choice = input(f"Which pawn to swap with? Give an index 1 - 3: ")
      if pawn_choice not in valid_numbers:
        print("Enter a valid pawn number!\n")

    pawn_index_int = int(pawn_choice) - 1
    return pawn_index_int


class SendPawnToSixtyFourActionCard(Card):
  def __init__(self) -> None:
    self.identifier = 23

  def description(self):
    return "Send your pawn to 64"
  
  def is_keeper(self):
    return False
  
  def is_roll_again(self):
    return False
  
  def execute(self, board, player, other_player):
    pawn_choice = player.choose_prime_pawns(player.pawns)
    result_square = board.get_square_from_number(64)
    result_message = board.move_pawn(pawn_choice, pawn_choice.square, result_square)
    print(result_message)
  
class StealOtherActionCard(Card):
  def __init__(self) -> None:
    self.identifier = 24

  def description(self):
    return "Steal another player's keeper card"
  
  def is_keeper(self):
    return False
  
  def is_roll_again(self):
    return False
  
  def execute(self, board, player, other_player):
    other_players_cards = other_player.cards
    if len(other_players_cards) == 0:
      print("No cards to steal\n")
    else:
      random_card = random.choice(other_players_cards)
      other_player.cards.remove(random_card)
      player.add_card(random_card)
      print(f"Stolen card: \"{random_card.description()}\" from other player")