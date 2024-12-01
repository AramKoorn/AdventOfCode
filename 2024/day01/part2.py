from collections import Counter


f = open("2024/day01/input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n') for x in lines]

l1 = []
l2 = []

for l in lines:
    a, b = l.split("   ")
    l1.append(int(a))
    l2.append(int(b))

c = Counter()
for x in l2:
    c[x] += 1

t = 0
for x in l1:
    t += x * c[x]
    
print(t)
