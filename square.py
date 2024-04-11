from constants import *

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