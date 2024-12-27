program = [*map(int, open("2019/day02/input.txt").read().split(","))]
pointer = 0

program[1] = 12
program[2] = 2

while True:
    match program[pointer]:
        case 1:
            program[program[pointer + 3]] = program[program[pointer + 1]] + program[program[pointer + 2]]
            pointer += 4
            continue
        case 2:
            program[program[pointer + 3]] = program[program[pointer + 1]] * program[program[pointer + 2]]
            pointer += 4
            continue
        case 99:
            break
    pointer += 1
    


print(program[0])