from collections import Counter


rng = [*map(int, open("2019/day04/input.txt").read().split("-"))]


def is_valid(x):
    last_digit = x % 10
    repeats = Counter()

    for _ in range(6):
        x //= 10
        new_digit = x % 10
        if x % 10 > last_digit:
            return False
        if x % 10 == last_digit:
            repeats[last_digit] += 1
        last_digit = new_digit
    
    return 1 in repeats.values()


t = 0
for x in range(rng[0], rng[1] + 1):
    if is_valid(x):
        t += 1

print(t)
