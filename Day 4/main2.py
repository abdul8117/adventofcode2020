def parse_file():
    f = open("Day 4/input.txt", "r")
    file_data = f.read()
    f.close()
    passport_list = file_data.split("\n\n")

    return passport_list


def validate_passport_fields(passport):
    global valid_passport
    required_info = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for i in required_info:
        if i not in passport:
            return False
        else:
            valid_passport = passport

    return True


def validate_passport_info(passport):
    passport_fields = passport.replace("\n", " ").split(" ")
    isvalid = True

    # byr 
    # four digits, 1920 <= x <= 2002
    for i in passport_fields:
        # print(passport)
        if "byr" in i:
            birth_year = i.split(":")[1]
            if len(birth_year) != 4:
                isvalid = False
                continue
            elif not(1920 <= int(birth_year) <= 2002):
                isvalid = False
                continue
        
        if "iyr" in i:
            issue_year = i.split(":")[1]
            if len(issue_year) != 4:
                isvalid = False
                continue
            elif not(2010 <= int(issue_year) <= 2020):
                isvalid = False
                continue
        
        if "eyr" in i:
            expiry_year = i.split(":")[1]
            if len(expiry_year) != 4:
                isvalid = False
                continue
            elif not(2020 <= int(expiry_year) <= 2030):
                isvalid = False
                continue
        
        if "hgt" in i:
            height = i.split(":")[1]
            if height[-2::] == "cm":
                if not(150 <= int(height.replace("cm", "")) <= 193):
                    isvalid = False
                    continue
            elif height[-2::] == "in":
                if not(59 <= int(height.replace("in", "")) <= 76):
                    isvalid = False
                    continue

        if "hcl" in i:
            accepted_chars = [chr(i) for i in range(ord('a'), ord('f')+1)] + [str(i) for i in range(0, 9+1)] + ["#"]
            colour = i.split(":")[1]
            if not(colour[0] == "#"):
                isvalid = False
                continue
            else:
                for char in colour:
                    if char not in accepted_chars:
                        isvalid = False
                        continue
        
        if "ecl" in i:
            accepted_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            colour = i.split(":")[1]
            if not(colour in accepted_colours):
                isvalid = False
                continue

        if "pid" in i:
            id_ = i.split(":")[1]
            if len(id_) != 9:
                isvalid = False
                continue
    
    if isvalid:
        return True
    else:
        return False


def main():
    passports = parse_file()
    valid_count = 0

    for passport in passports:
        if validate_passport_fields(passport):
            if validate_passport_info(valid_passport):
                valid_count += 1

    print(valid_count)


main()
