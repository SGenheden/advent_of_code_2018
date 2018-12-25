
r2 = 0
r0 = 0
visited = []
first = True
while True:
    r1 = r2 | 65536
    r2 = 1250634
    while True:
        r4 = r1 & 255
        r2 += r4
        r2 &= 16777215
        r2 *= 65899
        r2 &= 16777215
        if r1 < 256:
            break
        r1 //= 256
    if r2 not in visited:
        visited.append(r2)
    else:
        print(f"Found {r2} for second part")
        break
