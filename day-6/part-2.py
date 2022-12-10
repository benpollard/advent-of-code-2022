with open('./input.txt') as f:
    packet = f.readline()

seen = []

for i in range(len(packet)):
    print(seen)
    if packet[i] in seen:
        seen.clear()
    else:
        seen.append(packet[i]) 
    if len(seen) == 14:
        print(i)
        break;
