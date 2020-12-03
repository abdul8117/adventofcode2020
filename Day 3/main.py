"""

get input data from input.txt
save the data in map_ as a 2d list where each inner lists are rows and their items are the coloumns they are in

e.g.
x = [[1, 2, 3], [4, 5, 6]]

x[0] is the first row.
x[1] is the last row.

x[0][0] is the first row and coloumn
etc...

iteration through the 2d list:
    n1, n2 shall be indexes for map_
    n1 is the row, n2 is the column
    declare them to be 0

    before iterating through the map, check if the edge of the map has been passed:
        if the length of the row minus n2+1 (the column) is less than 3:
            map_ += map_

    start from the top left (map_[0][0])
    if map_[n1][n2] is a tree:
        increment tree_count

    add one to n1, three to n2

"""

import math

map_ = []
tree_count = 0

f = open("Day 3/input.txt", "r")
for line in f:
    map_.append([line.replace("\n", "")])
f.close()


index = 0
for i in map_:
    if i[0][index] == "#":
        tree_count += 1
    
    index = (index + 3) % (len(i[0]))

print(tree_count)