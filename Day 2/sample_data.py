critera_password = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
min_, max_ = 0, 0
letter_count = 0
valid_count = 0

for i in critera_password:
    criteria = i.split(":")[0]
    password = i.split(":")[1]
    min_ = int(criteria[0])
    max_ = int(criteria[2])
    target_letter = criteria[-1]

    for letter in password:
        if letter == target_letter:
            letter_count += 1

    if min_ <= letter_count <= max_:
        print(f"{password} is valid. Its criteria: {criteria}\n")
    else:
        print(f"{password} is invalid. Its criteria: {criteria}\n")

    letter_count = 0