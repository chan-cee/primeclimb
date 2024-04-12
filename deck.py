import random
from utils import *

class Deck:
  def __init__(self) -> None:
    self.cards = [
      AddSubtractKeeperCard(1),
      AddSubtractKeeperCard(2),
      AddSubtractKeeperCard(3),
      AddSubtractKeeperCard(4),
      AddSubtractKeeperCard(5),
      AddSubtractKeeperCard(6),
      AddSubtractKeeperCard(7),
      AddSubtractKeeperCard(8),
      AddSubtractKeeperCard(9),
      TwoSpacesKeeperCard(),
      TwoSpacesKeeperCard(),
      SubtractOrDivideKeeperCard(),
      SubtractOrDivideKeeperCard(),
      RollAgainActionCard(),
      RollAgainActionCard(),
      RollAgainActionCard(),
      AddSubtractFiftyActionCard(),
      FiftySubtractTenOrDoubleActionCard(),
      AdvanceToNearestPawnActionCard(),
      ReverseToNearestPawnActionCard(),
      ReverseDigitsActionCard(),
      SwitchTwoPawnsActionCard(),
      SendPawnToSixtyFourActionCard(),
      StealOtherActionCard()
    ]

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
      pawn_choice = player.choose_pawn(player.pawns)
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
    pawn_choice = player.choose_pawn(player.pawns)
    square_number = pawn_choice.square.number

    for i in range(square_number - 2, square_number + 3):
      square = board.get_square_from_number(square_number)
      start_square = board.start_square
      if not square.is_end_square() and i != square_number:
        board.move_pawn(square.pawn, square, start_square)
        print(f"Sent pawn from {square.number} to start\n")


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
    pass

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
    pass

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
    pass

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
    pass

class ReverseDigitsActionCard(Card):
  def __init__(self) -> None:
    self.identifier = 21

  def description(self):
    return "Reverse to the pawn nearest you. Send them back to start"
  
  def is_keeper(self):
    return False
  
  def is_roll_again(self):
    return False
  
  def execute(self, board, player, other_player):
    pass

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
    pass

class SendPawnToSixtyFourActionCard(Card):
  def __init__(self) -> None:
    self.identifier = 23

  def description(self):
    return "Send a pawn of your choice to 64"
  
  def is_keeper(self):
    return False
  
  def is_roll_again(self):
    return False
  
  def execute(self, board, player, other_player):
    pass
  
class StealOtherActionCard(Card):
  def __init__(self) -> None:
    self.identifier = 24

  def description(self):
    return "Send a pawn of your choice to 64"
  
  def is_keeper(self):
    return False
  
  def is_roll_again(self):
    return False
  
  def execute(self, board, player, other_player):
    pass