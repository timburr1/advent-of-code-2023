
grid = []

def checkGearRatio(x, y):
    # todo

    return 0

def sumGearRatios(lineNum):
    sum = 0

    for i in range(0, len(line)):
        if line[i] == '*':
            sum += checkGearRatio(i, lineNum)

    return sum

with open('input.txt') as fp:
    for line in fp:
        grid.append(line)

    sum = 0
    for i in range(len(grid)):
        sum += sumGearRatios(i)
    print(sum)

    