lines = list(map(int, open("2019/day01/input.txt").read().splitlines()))
print(sum([x // 3 - 2 for x in lines]))
