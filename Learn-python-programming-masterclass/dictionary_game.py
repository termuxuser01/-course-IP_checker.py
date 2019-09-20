location = {
  0:'en el cyber',
  1:'on the road',
  2:'on the hill',
  3:'in the building',
  4:'at the valley',
  5:'in the forest'
}

directions = [
  {"Q":0},
  {"N":5, "E":3, "W":2, "S":4},
  {"N":5, "S":4, "E":1},
  {"W":1},
  {"N":1, "W":2},
  {"W":2, "S":2}
]

vocabulary = {
  "WEST": "W",
  "NORTH": "N",
  "EAST": "E",
  "SOUTH": "S"
}

current_loc = 1

print("locations:")
for i in sorted(location.keys()):
  print("{} - {}".format(i, location[i]))
print("Q to quit")

while True:
  print("You are {}".format(location[current_loc]))
  print("-" * 40)
  print("you can go:")
  for k in directions[current_loc].keys():
    print(k)
  choice = input("wich direcction do you want to go?: ").upper()
  if len(choice) > 1:
    if choice in vocabulary:
        current_loc = directions[current_loc][vocabulary[choice]]
    else:
        print("cannot go in this direction!")
  elif choice in directions[current_loc]:
    current_loc = directions[current_loc][choice]
  elif choice == "Q":
    print("You are {}".format(location[0]))
    break
  else:
    print('cannot go in this direction!')
