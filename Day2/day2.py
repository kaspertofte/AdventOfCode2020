data = open("day2.input", "r").read().strip().split("\n")
numInput = len(data)
solution1 = 0
for line in data:
    if(line == ""):
        continue
    elements = line.split(" ")
    limits = elements[0].split("-")
    char = elements[1][0]
    occurences = elements[2].count(char)
    if(int(limits[0]) <= occurences and occurences <= int(limits[1])):
        print(line)
        solution1 = solution1 + 1
print(solution1)

solution2 = 0
for line in data:
    if(line == ""):
        continue
    elements = line.split(" ")
    limits = elements[0].split("-")
    index1 = int(limits[0])-1
    index2 = int(limits[1])-1
    char = elements[1][0]
    if( (elements[2][index1] == char) ^ (elements[2][index2] == char)):
        print(line)
        solution2 = solution2 + 1
print(solution2)
