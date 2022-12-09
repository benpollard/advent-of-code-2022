with open('./input.txt') as f:
    total = 0
    for line in f:
        seen = {}
        items = [c for c in line.rstrip()]
        for item in items[:(len(items)//2)]:
            seen[item] = 1
        for item in items[len(items)//2:]:
            if item in seen:
                val = ord(item)
                if val > 96:
                    total += val - 96
                else:
                    total += val - 38
                break;
    print(total)