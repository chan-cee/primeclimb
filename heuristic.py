from collections import deque 
import math

def bfs():
  frontier = deque()
  frontier.append((101, 0))
  distance = [None] * 102
  while len(frontier) != 0:
    node, counter = frontier.popleft()
    if node < 0 or node > 101 or node - math.floor(node) != 0:
      continue

    node_int = int(node)
    if distance[node_int] is not None:
      continue

    distance[node_int] = counter
    for dice_roll in range(1, 7):
      new_number = node_int + dice_roll
      new_number_two = node_int - dice_roll
      new_number_three = node_int * dice_roll
      new_number_four = node_int / dice_roll
      frontier.append((new_number, counter + 1))
      frontier.append((new_number_two, counter + 1))
      frontier.append((new_number_three, counter + 1))
      frontier.append((new_number_four, counter + 1))

  for i in range(len(distance)):
    distance[i] = distance[i] + 0.01 * (101 - i)
    distance[i] = round(distance[i], 2)

  return distance

g = bfs()
print(g)
for i in g:
  print(i)


  