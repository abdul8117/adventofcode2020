import math


def parse_file(inputFile):
    f = open(f"Day 5/{inputFile}", "r")
    codes = f.read().split("\n")

    return codes


def decode_code(code):
    fb = code[:7]
    rl = code[7::]
    row = [0, 127]
    col = [0, 7]

    for i in fb:
        if i == "F":
            row[1] = math.floor((row[0] + row[1]) / 2)
        elif i == "B":
            row[0] = math.ceil((row[0] + row[1]) / 2)

    for i in rl:
        if i == "L":
            col[1] = math.floor((col[0] + col[1]) / 2)
        elif i == "R":
            col[0] = math.ceil((col[0] + col[1]) / 2)

    return row[0] * 8 + col[1]


def find_seat_ID(seat_IDs):
    i = 0
    while i < len(seat_IDs)-1:
        if (seat_IDs[i+1] - seat_IDs[i]) == 2:
            # print(seat_IDs[i], seat_IDs[i+1])
            seat = seat_IDs[i] + 1
        i += 1
    
    return seat


def main():
    codes = parse_file("input.txt")
    seat_IDs = []

    for code in codes:
        seat_IDs.append(decode_code(code))

    # print(max(seat_IDs))
    # print(seat_IDs)
    # print(sorted(seat_IDs))
    IDs_sorted = sorted(seat_IDs)
    # print(IDs_sorted)
    print(find_seat_ID(IDs_sorted))


main()