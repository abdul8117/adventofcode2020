import math

map_ = []

f = open("Day 3/input.txt", "r")
for line in f:
    map_.append([line.replace("\n", "")])
f.close()

def trees(right, down):
    tree_count = 0
    r_index, d_index = 0, 0

    while d_index < len(map_):
        if map_[d_index][0][r_index] == "#":
            tree_count += 1

        r_index = (r_index + right) % (len(map_[0][0]))
        d_index += down

    return tree_count

print(trees(1, 1) * trees(3, 1) * trees(5, 1) * trees(7, 1) * trees(1, 2))