f_input = open("day2-input.txt", "r").readlines()
f_input = [x[:-1] for x in f_input]

i = 0
for element in f_input:
  j = element.split(" ")
  print(j)

  if j[1] == "X":
    # LOSE
    if j[0] == "A":
      i += 3

    if j[0] == "B":
      i += 1

    if j[0] == "C":
      i += 2

  if j[1] == "Y":
    # DRAW
    if j[0] == "A":
      i += 4

    if j[0] == "B":
      i += 5

    if j[0] == "C":
      i += 6

  if j[1] == "Z":
    # WIN
    if j[0] == "A":
      i += 8

    if j[0] == "B":
      i += 9

    if j[0] == "C":
      i += 7

  print(i)
  