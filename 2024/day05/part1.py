f = open("2024/day05/input.txt", "r").readlines()
lines = [x.replace("\n", "") for x in f]
rules = [x for x in lines if "|" in x]
rules = [x.split("|") for x in rules]

ins = [x for x in lines if "|" not in x and x != '']
ins = [x.split(',') for x in ins]

t = 0
for l in ins:
    ok = True
    for i in range(1, len(l)):
        left, r = l[i - 1], l[i]
        # check r not l
        if [r, left] in rules:
            ok = False
        
    if ok:
        t += int(l[len(l) // 2])
print(t)