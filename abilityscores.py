import random


# Roll 4d6 and add the 3 highest values
def get_value():
  # Roll 4d6
  dice_values = []
  for i in range(4):
    val = random.randint(1, 6)
    dice_values.append(val)

  # Remove the lowest value
  dice_values.sort()
  dice_values.pop(0)

  # Add remaining values
  sum = 0
  for i in dice_values:
    sum += i

  return sum


# Get a list of values for ability scores
def get_ability_scores():
  # Get values for ability scores and put in a list
  scores = []
  for i in range(6):
    scores.append(get_value())

  # Sort the list
  scores.sort(reverse=True)
  print(scores)


get_ability_scores()




# class Character():
#   def __init__(self, name):

# Each Character class has a Race, Class, etc.