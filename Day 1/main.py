inputList = []
inputFile = open("Day 1/input.txt", "r")

for line in inputFile:
    inputList.append(line)

inputFile.close()

# remove the last two characters of each string in the list
# cast each item into an integer

i = 0
for num in inputList:
    inputList[i] = inputList[i].replace("\n", "")
    int(inputList[i])
    i += 1

# print(inputList)

for i in inputList:
    for j in inputList:
        if i + j == 2020:
            print(f"{i} and {j}")