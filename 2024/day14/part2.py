import re
from functools import reduce
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


f = open("2024/day14/input.txt").read().splitlines()
r = 103 
c = 101

pattern = r'([-+]?\d+),([-+]?\d+)'

steps = 100

with PdfPages("test1.pdf") as pdf:
    for i in range(10000):
        print(i)
        pos = []
        for l in f:
            steps = i
            matches = re.findall(pattern, l)
            (x, y), (dx, dy) = matches   
            x, y, dx, dy, = int(x), int(y), int(dx), int(dy)
            nc = (steps * dx + x) % c
            nr = (steps * dy + y) % r
            pos.append((nr, nc))
        
        # Found this criterium later. Initially I inspected a PDF with 10000 plots
        if len(pos) == len(set(pos)):
            x, y = zip(*pos)
            plt.figure(figsize=(5, 5))
            plt.scatter(x, y, s=10, alpha=0.7)
            fig = plt.gcf()
            plt.gca().invert_yaxis()  # Invert y-axis to have (0,0) at the top left
            plt.suptitle(f"Iteration: {i}")
            plt.show()
