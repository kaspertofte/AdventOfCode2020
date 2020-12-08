def slopes(data, dx, dy):
    numLines = len(data)
    numCol = len(data[0])
    result = 0
    x=1
    for y in range(1,numLines,dy):
      if(data[y-1][(x % numCol)-1] == "#"):
          result = result + 1
      x=x+dx
    return result

data = open("day3.input", "r").read().strip().split("\n")

print(slopes(data,1,1))
print(slopes(data,3,1))
print(slopes(data,5,1))
print(slopes(data,7,1))
print(slopes(data,1,2))
print("\n")
print(slopes(data,1,1)*slopes(data,3,1)*slopes(data,5,1)*slopes(data,7,1)*slopes(data,1,2))
