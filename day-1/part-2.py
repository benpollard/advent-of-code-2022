with open('./input.txt') as f:
    topThree = [0, 0, 0]
    runningTotal = 0
    for line in f:
        line = line.rstrip()
        if line == "":
            if runningTotal > topThree[0]:
                topThree[0] = runningTotal
                topThree.sort()
            runningTotal = 0
        else:
            runningTotal += int(line)
    print(sum(topThree))

