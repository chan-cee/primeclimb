import random

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
    pass

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
    pass

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
    pass

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