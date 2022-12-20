f_input = open("day2-input.txt", "r").readlines()
f_input = [x[:-1] for x in f_input]

i = 0
for element in f_input:
  j = element.split(" ")
  j[1] = j[1].replace("X", "A").replace("Y", "B").replace("Z", "C")
  print(j)

  if j[1] == "A":
    i += 1

  elif j[1] == "B":
    i += 2

  elif j[1] == "C":
    i += 3

  if (j[0] == "A" and j[1] == "B") or (j[0] == "B" and j[1] == "C") or (j[0] == "C" and j[1] == "A"):
    i += 6

  elif j[0] == j[1]:
    i += 3

print(i)
  