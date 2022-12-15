f_input = open("day1-input.txt", "r").readlines()
f_input = [x[:-1] for x in f_input]

l_output = []

i = 0
for element in f_input:
    if element != "":
        i = i + int(element)

    if element == "":
        l_output.append(i)
        i = 0

l_output.sort()
print(l_output[len(l_output) - 1])
