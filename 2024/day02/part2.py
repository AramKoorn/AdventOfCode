from copy import deepcopy

f = open("2024/day02/input.txt", "r")
lines = f.readlines()
lines = [list(map(int, x.strip('\n').split(" "))) for x in lines]


def find_save(l):
    idx = []
    asc , desc = True, True
    for i in range(1, len(l)):
        diff = l[i] - l[i - 1]
        if diff <= 0 or abs(diff) > 3:
            idx.append(i)
            asc = False
        if diff >= 0 or abs(diff) > 3:
            idx.append(i)
            desc = False
    return asc or desc, idx

t = 0 
for l in lines:
    bool, idx = find_save(l)
    if bool:
        t += 1
    else:
        for i in range(len(l)):
            bool, _ = find_save([x for j, x in enumerate(l) if j != i])
            if bool: 
                t += 1
                break
print(t)