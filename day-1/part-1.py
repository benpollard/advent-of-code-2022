with open('./input.txt') as f:
    maxKcal = 0
    runningTotal = 0
    for line in f:
        line = line.rstrip()
        if line == "":
            maxKcal = max(maxKcal, runningTotal)
            runningTotal = 0
        else:
            runningTotal += int(line)
    print(maxKcal)