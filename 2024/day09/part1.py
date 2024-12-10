import os

print(os.getcwd())
f = open("input.txt").read()
disk = []
fid = 0

for i, char in enumerate(f):
    x = int(char)
    if i % 2 == 0:
        disk += [fid] * x
        fid += 1
    else:
        disk += [-1] * x

spaces = [(i, x) for i, x in enumerate(disk) if x == -1]
files = [(i, x) for i, x in enumerate(disk) if x != -1]

while min(spaces) < max(files):
    spaces.sort()
    files.sort()
    f = files.pop()
    s = spaces.pop(0)
    files.append((s[0], f[1]))
    spaces.append((f[0], s[1]))

    disk[s[0]] = f[1]
    disk[f[0]] = s[1]
    # print(disk)


print("".join([str(x) for x in disk]))
print(sum(i * x for i, x in enumerate(disk) if x != -1))