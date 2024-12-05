f = open("2024/day05/input.txt", "r").readlines()
lines = [x.replace("\n", "") for x in f]
rules = [x for x in lines if "|" in x]
rules = [x.split("|") for x in rules]

ins = [x for x in lines if "|" not in x and x != '']
ins = [x.split(',') for x in ins]


def is_correct(l):
    for i in range(1, len(l)):
        left, r = l[i - 1], l[i]
        if [r, left] in rules:
            return False
    return True


def make_correct(l):
    while not is_correct(l):
        for i in range(1, len(l)):
            left, r = l[i - 1], l[i]
            if [r, left] in rules:
                # swap elements
                l[i], l[i - 1] = l[i - 1], l[i]
    return l


t = 0
for l in ins:
    if not is_correct(l):
        l = make_correct(l)
        t += int(l[len(l) // 2])
print(t)
