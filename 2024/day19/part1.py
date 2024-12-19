from functools import lru_cache 


towels, patterns = open("2024/day19/input.txt").read().split("\n\n")
towels = towels.split(", ")


@lru_cache(maxsize=None)
def find(pat):
    if pat == "":
        return True
    
    for t in towels:
        ln = len(t)
        if ln <= len(pat):
            if pat[:ln] == t:
                if find(pat[ln:]):
                    return True

    return False

t = 0
for p in patterns.splitlines():
    if find(p):
        t += 1

print(t)
