import re

f = open("2024/day03/input.txt", "r")
lines = [x.strip('\n') for x in f]
txt = "".join(lines)
print(txt)
# print(f.readlines())

# Regular expression pattern
pattern = r"mul\((-?\d+),(-?\d+)\)"

# Find all matches
matches = re.findall(pattern, txt)
m_mul = [(match.group(), match.start(), match.end()) for match in re.finditer(pattern, txt)]
# print(m_mul)
t = 0
for a, b in matches:
    t += int(a) * int(b)


pattern = r"(do|don't)\(\)"
m = [(match.start(), match.group()) for match in re.finditer(pattern, txt)]

m_mul

# # Print the matches
# for match_text, start_idx, end_idx in m:
#     print(f"Match: '{match_text}' at index: {start_idx}-{end_idx}")
m.append((-1, 'do()'))
m.sort()
t = 0
for x in m_mul:
    group, start, end = x 
    integers = re.findall(r'\d+', group)
    integers = list(map(int, integers))
    # print(integers)
    start
    # find latest
    prev_command = "do()"
    for i, command in m:
        if i < start:
            prev_command = command
        else:
            break
    if prev_command == "do()":
        print(integers)
        t += integers[0] * integers[1]

print(t)




    