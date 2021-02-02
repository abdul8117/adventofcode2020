f = open("Day 6/input.txt", "r")
groups = f.read().split("\n\n")

unique_letters = []
answers = 0

for line in f:
    # indicates a new group's answers
    if line == "\n":
        letters = []
        continue

    line = line.replace("\n", "")

    for letter in line:
        if letter not in unique_letters:
            answers += 1
            unique_letters.append(letter)


f.close()

print(answers)
