data = open("day1.input", "r").read().strip().split("\n")
numInput = len(data)
for i in range(numInput):
    for j in range(i+1, numInput-1):
        if (int(data[i]) + int(data[j])) == 2020:
            print(data[i] +", line " + str(i) + " ; " + data[j] + ", line " + str(j))
            print(int(data[i])*int(data[j]))


data = open("day1.input", "r").read().split("\n")
numInput = len(data)
for i in range(numInput):
    for j in range(i+1, numInput-1):
        for k in range(j+1, numInput-2):
            if (int(data[i]) + int(data[j]) + int(data[k]) ) == 2020:
                print(data[i] +", line " + str(i+1) + " ; " + data[j] + ", line " + str(j+1) + " ; " + data[k] + ", line " + str(k+1))
                print(int(data[i])*int(data[j])*int(data[k]))
