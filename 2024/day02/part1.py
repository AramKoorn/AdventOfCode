f = open("2024/day02/input.txt", "r")
lines = f.readlines()
lines = [list(map(int, x.strip('\n').split(" "))) for x in lines]

t = 0 
for l in lines:
    asc , desc = True, True
    for i in range(1, len(l)):
        diff = l[i] - l[i - 1]
        if diff <= 0 or abs(diff) > 3:
            asc = False
        if diff >= 0 or abs(diff) > 3:
            desc = False
    if asc or desc:
        t += 1
print(t)