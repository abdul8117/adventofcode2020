# f = open("stuff.txt", "r")

# text = f.read()

# print(text)

f = open("stuff.txt", "a+")

f.write("More text")

text = f.read()

print(text)