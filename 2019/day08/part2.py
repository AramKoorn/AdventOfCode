import matplotlib.pyplot as plt
import numpy as np


digits = open("2019/day08/input.txt").read()

WIDE = 25
TALL = 6


layers = []
for i in range(len(digits)):
    if i % WIDE == 0:
        if  i != 0:
            layers.append(layer) 
        layer = []
    layer.append(digits[i])
layers.append(layer)

pixels = []
tmp = []
for i, l in enumerate(layers):
    if i % 6 == 0 and i != 0:
        pixels.append(tmp.copy())
        tmp = []
    tmp.append(l)
pixels.append(tmp)

image = [['.' for x in range(WIDE)] for _ in range(TALL)]
for i in range(len(image)):
    for j in range(len(image[0])):
        # find top layer
        for p in pixels:
            if p[i][j] != '2':
                image[i][j] = p[i][j]
                break
            


data = image.copy()
mapping = {'.': 0.0, '0': 0.0, '1': 1.0}
# Convert the data to a NumPy array of floats
image_array = np.array([[mapping[c] for c in row] for row in data], dtype=float)
plt.figure(figsize=(8, 3))      # Adjust figure size as you like
plt.imshow(image_array, cmap='gray', interpolation='nearest')
plt.tight_layout()
plt.show()