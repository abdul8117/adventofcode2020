
def parse_file(fileName):
    f = open(f"Day 6/{fileName}", "r")
    groups = f.read().split("\n\n")
    f.close()

    return groups

letters = []
answers = 0

for i in parse_file("input.txt"):
    print(f"{i}")

print(parse_file("input.txt"))
