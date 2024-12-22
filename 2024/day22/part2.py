from collections import Counter
import os


MOD = 16777216
secrets = list(map(int, open("input.txt").read().splitlines()))


def op1(n):
    return ((n * 64) ^ n) % MOD


def op2(n):
    return (int(n / 32) ^ n) % MOD


def op3(n):
    return  ((n * 2048) ^ n) % MOD


ops = [op1, op2, op3]
t = 0
prices = []
for n in secrets:
    p = []
    p.append(n % 10)
    for _ in range(2000):
        for op in ops:
            n = op(n)
        p.append(n % 10)
    prices.append(p)
    t += n
seq = []
c = Counter()
for p in prices:
    tmp = []
    s = []
    for i in range(1, len(p)):
        s.append(p[i] - p[i - 1])
        tmp.append(p[i] - p[i - 1])
        if len(tmp) > 4:
            tmp.pop(0)
        if len(tmp) == 4:
            c[tuple(tmp)] += 1
    seq.append(s)

# for k, v in c.most_common():
#     print(k, v)
# print(seq[0]) print(seq[1])


def score(order, seq, prices):
    for i in range(len(seq) - 3):
        if seq[i:i + 4] == order:
            return prices[i + 4]
    return 0

best_score = 0
cnt = 0

# idea check most common sequences across all price lists
# is relatively fast but doesn't guarantuee correct solution
for sequence, _ in c.most_common()[:100]:
    cnt += 1 
    if cnt % 10 == 0:
        print("best ", best_score)
    t = 0
    for i, s1 in enumerate(seq):
        t += score(list(sequence), s1, prices[i])
    best_score = max(t, best_score)
print(best_score)
