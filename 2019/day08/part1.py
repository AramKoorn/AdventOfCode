from collections import Counter, defaultdict


digits = open("2019/day08/input.txt").read()

WIDE = 25
TALL = 6


layers = []
for i in range(len(digits)):
    if i % WIDE == 0:
        if  i != 0:
            layers.append(layer) 
        layer = []
    layer.append(digits[i])
layers.append(layer)


l = 0
cnts = {i: [0] * 10 for i in range(int(len(layers) / TALL))}
tmp = TALL
for i, x in enumerate(layers):
    tmp -= 1
    for j in x:
        cnts[l][int(j)] += 1
    if tmp == 0:
        l += 1
        tmp = TALL

smallest = float("inf")
for k, v in cnts.items():
    if v[0] < smallest:
        smallest = v[0]
        res = v

print(res[1] * res[2])
