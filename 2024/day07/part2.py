f = open("2024/day07/input.txt").readlines()
lines = [x.strip('\n') for x in f]

targets = []
values = []


for li in lines:
    l, r = li.split(":") 
    targets.append(int(l))
    values.append([int(x) for x in r.strip(" ").split(" ")])


def dfs(t, l, target):
    if t == target and l == []:  
        return 1
    if not l:  
        return 0

    for op in ["+", "*", "||"]:
        match op:
            case "+":
                if dfs(t + l[0], l[1:], target):
                    return 1
            case "*":
                if dfs(t * l[0], l[1:], target):
                    return 1
            case "||":
                    new_n = int(str(t) + str(l[0]))
                    if dfs(new_n, l[1:], target):
                        return 1

    return 0  

res = 0
for t, vals in zip(targets, values):
    if dfs(vals[0], vals[1:], t) == 1:
        res += t

print(res)