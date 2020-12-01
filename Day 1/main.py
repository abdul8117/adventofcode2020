# two numbers whose sum is 2020
def find_product_2(input_):
    for i in input_:
        for j in input_:
            if i + j == 2020:
                return i * j

# three numbers whose sum is 2020
def find_product_3(input_):
    for i in input_:
        for j in input_:
            for k in input_:
                if i + j + k == 2020:
                    return i * j * k


input_list = []
input_file = open("Day 1/input.txt", "r")

for line in input_file:
    input_list.append(line)

input_file.close()

# remove the last two characters of each string in the list
# cast each item into an integer
i = 0
for num in input_list:
    input_list[i] = input_list[i].replace("\n", "")
    input_list[i] = int(input_list[i])
    i += 1

print(find_product_2(input_list))
print(find_product_3(input_list))