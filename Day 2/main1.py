criteria_password = []
valid_count = 0

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
    min_ = int(criteria[0])
    max_ = int(criteria[1])
    target_letter = criteria[2]

    occurences = password.count(target_letter)

    if min_ <= occurences <= max_:
        valid_count += 1
    # else:
    #     print(criteria, password)

    occurences = 0

print(valid_count)
