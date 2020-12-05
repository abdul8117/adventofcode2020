def parse_file():
    f = open("Day 4/input.txt", "r")
    file_data = f.read()
    f.close()
    passport_list = file_data.split("\n\n")

    return passport_list


def validate_passport(passport):
    required_info = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for i in required_info:
        if i not in passport:
            return False
    
    return True
            

def main():
    passports = parse_file()
    valid_count = 0

    for passport in passports:
        if validate_passport(passport):
            valid_count += 1
    
    print(valid_count)


main()