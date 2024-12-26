lines = [*map(int, open("2019/day01/input.txt").read().splitlines())]

t = 0
for x in lines:
    while x >= 0:
        x //= 3
        x -= 2
        if x >= 0:
            t += x

print(t)
