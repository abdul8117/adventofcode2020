min_, max_ = 0, 0
valid_count = 0
criteria_password = []

# import puzzle input
input_file = open("Day 2/input.txt", "r")
for line in input_file:
    criteria_password.append(line.replace("\n", ""))
input_file.close()

# main
for i in criteria_password:
    criteria = i.split(":")[0].replace(" ", "-")
    password = i.split(":")[1].strip()

    criteria = criteria.split("-")
    pos1 = int(criteria[0])
    pos2 = int(criteria[1])
    target_letter = criteria[2]

    if (password[pos1-1] == target_letter) and (password[pos2-1] == target_letter):
        # the password has the letter in both positions
        continue
    elif (password[pos1-1] == target_letter) or (password[pos2-1] == target_letter):
        # only one has the target letter
        valid_count += 1 

print(valid_count)