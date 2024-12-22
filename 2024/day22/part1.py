MOD = 16777216

secrets = list(map(int, open("2024/day22/input.txt").read().splitlines()))
print(secrets)


def op1(n):
    return ((n * 64) ^ n) % MOD


def op2(n):
    return (int(n / 32) ^ n) % MOD


def op3(n):
    return  ((n * 2048) ^ n) % MOD


ops = [op1, op2, op3]
t = 0
for n in secrets:
    for _ in range(2000):
        for op in ops:
            n = op(n)
    t += n

print(t)
