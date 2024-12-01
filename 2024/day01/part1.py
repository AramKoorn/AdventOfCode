import os 
print(os.getcwd())

f = open("2024/day01/input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n') for x in lines]

l1 = []
l2 = []

for l in lines:
    a, b = l.split("   ")
    l1.append(int(a))
    l2.append(int(b))

l1.sort()
l2.sort()

d = 0
for a, b in zip(l1, l2):
    d += abs(a - b)

print(d)
