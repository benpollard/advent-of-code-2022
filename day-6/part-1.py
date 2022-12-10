with open('./input.txt') as f:
    packet = f.readline()

seen = []

for i in range(len(packet)):
    if packet[i] in seen:
        seen = seen[seen.index(packet[i]) + 1 :]
        seen.append(packet[i])
    else:
        seen.append(packet[i])
        print(seen, i) 
    if len(seen) == 14:
        print(i + 1)
        break;
