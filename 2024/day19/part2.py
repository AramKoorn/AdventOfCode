from functools import lru_cache 


towels, patterns = open("2024/day19/input.txt").read().split("\n\n")
towels = towels.split(", ")


@lru_cache(maxsize=None)
def find(pat, tot=0):
    if pat == "":
        return tot + 1
    
    for t in towels:
        ln = len(t)
        if ln <= len(pat):
            if pat[:ln] == t:
                tot += find(pat[ln:], 0)

    return tot

t = 0
for p in patterns.splitlines():
    t += find(p)

print(t)
