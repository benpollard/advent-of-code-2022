with open('./input.txt') as f:
    total = 0
    for line in f:
        a, b = line.rstrip().split(',')
        a = a.split('-')
        a = [int(i) for i in a]
        b = b.split('-')
        b = [int(i) for i in b]
        if b[0] >= a[0] and b[0] <= a[1] or b[1] >= a[0] and b [1] <= a[1]:
            total += 1
        elif a[0] >= b[0] and a[0] <= b[1] or a[1] >= b[0] and a[1] <= b[1]:
            total += 1

    print(total)