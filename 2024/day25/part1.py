f = open("2024/day25/input.txt").read()
schema = f.split("\n\n")
schemas = [s.split("\n") for s in schema]

locks = set()
keys = set()

for s in schemas:
    h = [-1] * len(s[0]) 
    is_lock = True if s[0][0] == "#" else False
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == "#":
                h[j] += 1
    h = tuple(h)
    if is_lock:
        locks.add(h)
    else:
        keys.add(h)

limit = len(schemas[0]) - 1

t = 0
for key in keys:
    for lock in locks:
        ok = True
        for i in range(len(key)):
            if key[i] + lock[i] >= limit:
                ok = False
        if ok:
            t += 1

print(t)
