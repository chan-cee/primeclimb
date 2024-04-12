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
      final_number = square_number - dice
    elif operation_choice == "m":
      final_number = square_number * dice
    elif operation_choice == "d":
      final_number = square_number / dice

    return int(final_number)

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True