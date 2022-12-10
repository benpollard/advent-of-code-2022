import re

def parseStacks(stackData, stackCount):
    stacks = [[] for i in range(stackCount)]
    for i in range(len(stackData)-1, -1, -1):
        for j in range(1, stackCount+1):
            val = " "
            if j == 1:
                val = stackData[i][1]
            else:
                val = stackData[i][((j - 1) * 4) + 1]
            if val != " ":
                stacks[j-1].append(val)
    return stacks

def parseInstruction(instructionData):
    match = re.findall(r'\s\d+', instructionData)
    if match:
        return [int(x.lstrip()) for x in match]

with open('./input.txt') as f:
    stackData = []
    stacks = []
    stacksParsed = False
    instructions = []
    for line in f:
        if not stacksParsed:
            if line[1] == "1":
                stacks = parseStacks(stackData, int(line[-3]))
                stacksParsed = True
                f.readline()
            else:
                stackData.append(line.rstrip('\n'))
        else:
            instructions.append(parseInstruction(line))

for instruction in instructions:
    tmp = []
    for x in range(instruction[0]):
        fromIdx = instruction[1] - 1
        if len(stacks[fromIdx]) > 0:
            tmp.append(stacks[fromIdx].pop())
    for x in range(len(tmp)):
        toIdx = instruction[2] - 1
        stacks[toIdx].append(tmp.pop())

ans = ""
for stack in stacks:
    ans += stack[-1]

print(ans)