VALUES = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}

with open("./input.txt") as f:
    totalScore = 0
    for line in f:
        round = line.rstrip().split()
        if abs(VALUES[round[0]] - VALUES[round[1]]) > 1:
            if VALUES[round[0]] < VALUES[round[1]]:
                totalScore += VALUES[round[1]]   
            elif VALUES[round[0]] > VALUES[round[1]]:
                totalScore += 6
                totalScore += VALUES[round[1]]
        else:
            if VALUES[round[0]] == VALUES[round[1]]:
                totalScore += 3
                totalScore += VALUES[round[1]]
            elif VALUES[round[0]] > VALUES[round[1]]:
                totalScore += VALUES[round[1]]   
            elif VALUES[round[0]] < VALUES[round[1]]:
                totalScore += 6
                totalScore += VALUES[round[1]]
    print(totalScore)
