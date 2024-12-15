import numpy as np

f = open("input.txt").read()
parsed_data = []
blocks = f.strip().split("\n\n")
for block in blocks:
    lines = block.split("\n")
    button_a = list(map(int, lines[0].split("X+")[1].split(", Y+")))
    button_b = list(map(int, lines[1].split("X+")[1].split(", Y+")))
    prize = list(map(int, lines[2].split("X=")[1].split(", Y=")))
    parsed_data.append([button_a, button_b, prize])


a = 3
b = 1
cost = 0
for eq in parsed_data:
    debug = True
    a = np.array([[eq[0][0], eq[1][0]], [eq[0][1], eq[1][1]]])
    b = np.array(eq[2])
    s = np.linalg.solve(a, b)
    # print(s)
    if np.allclose([x % 1 for x in np.round(s, 3)] , 0, atol=0.01):
        print("valid", s)
        cost += 3 * s[0]
        cost += s[1]
print(cost)
