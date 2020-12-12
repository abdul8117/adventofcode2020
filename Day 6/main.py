f = open("Day 6/input.txt", "r")
groups = f.read().split("\n\n")
f.close()

answers = 0

for group in groups:
    group = group.replace("\n", "")
    answers += len(set(group))

print(answers)
