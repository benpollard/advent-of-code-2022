with open("./input.txt") as f:
    totalScore = 0
    for line in f:
        round = line.rstrip().split()
        if round[1] == 'X':
            if round[0] == 'A':
                totalScore += 3
            elif round[0] == 'B':
                totalScore += 1
            elif round[0] == 'C':
                totalScore += 2
        elif round[1] == 'Y':
            totalScore += 3
            totalScore += ord(round[0]) - 64
        elif round[1] == 'Z':
            totalScore += 6
            if round[0] == 'A':
                totalScore += 2
            elif round[0] == 'B':
                totalScore += 3
            elif round[0] == 'C':
                totalScore += 1
    print(totalScore)