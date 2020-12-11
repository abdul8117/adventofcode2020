f = open("Day 6/input.txt", "r")
letters = []
answers = 0

for line in f:
    # indicates a new group's answers
    if line == "\n":
        letters = []
        answers = 0
        continue
    
    for letter in line:
        line = line.replace("\n", "")

    
f.close()