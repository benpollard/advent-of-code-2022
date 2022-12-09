with open('./input.txt') as f:
    total = 0
    count = 1
    seen = {}
    for line in f:
        items = []
        [ items.append(c) for c in line.rstrip() if c not in items]
        for item in items:
            if item not in seen:
                seen[item] = 1
            else:
                seen[item] += 1
        
        if count % 3 == 0:
            for k, v in seen.items():
                if v == 3:
                    val = ord(k)
                    if val > 96:
                        total += val - 96
                    else:
                        total += val - 38
                    break;
            seen.clear()
        count += 1
    print(total)