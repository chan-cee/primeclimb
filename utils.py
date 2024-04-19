from constants import *

class Move:
  def __init__(self, dice_roll, pawn_index, operation):
    self.dice_roll = dice_roll
    self.pawn_index = pawn_index
    self.operation = operation 

def eval_comparator(player_AI, other_player):
    def compare(tup):
      board, moves_so_far = tup
      pawns = board.get_pawns(player_AI)
      other_pawns = board.get_pawns(other_player)
      score = 0
      for pawn in pawns:
        score -= HEURISTIC[pawn.square.number]
      
      for other_pawn in other_pawns:
        score += HEURISTIC[other_pawn.square.number]

      return score
    
    return compare

def display_introduction():
  intro_string = "TODO"
  return intro_string

def display_end():
  end_string = "TODO"
  return end_string

def get_number_from_operation(operation_choice, square_number, dice):
    final_number = None

    if operation_choice == "a":
      final_number = square_number + dice
    elif operation_choice == "s":
      final_number = max(square_number - dice, 0)
    elif operation_choice == "m":
      final_number = square_number * dice
    elif operation_choice == "d":
      final_number = square_number / dice

    return final_number

def is_prime_above_10(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1

    return n > 10

def rolls():
  count = {}
  total = 0
  for i in range(1,7):
    for j in range(1,7):
      add = [i,j]
      add.sort()
      if i == j:
        add.append(i)
        add.append(i)
      add_tuple = tuple(add)
      if add_tuple not in count:
        count[add_tuple] = 0

      count[add_tuple] += 1
      total += 1

  for add_tuple in count:
    count[add_tuple] = count[add_tuple] / total
  
  return count