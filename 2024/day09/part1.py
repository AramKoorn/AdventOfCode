import os
print(os.getcwd())
f = open("input_test.txt").read()

start_id = "0"
blocks = ""

for i in range(len(f) - 1):
    if i % 2 == 0:
        blocks += start_id * int(f[i]) + "." * int(f[i + 1])
        start_id = str(int(start_id) + 1)
blocks += start_id * int(f[-1])

print(blocks)