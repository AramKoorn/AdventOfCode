from copy import deepcopy


program = [*map(int, open("2019/day02/input.txt").read().split(","))]
pointer = 0


class IntCode:
    def __init__(self, program):
        self.program = program
        self.pointer = 0
    
    def run(self, i, j):
        self.program[1] = i 
        self.program[2] = j

        while True:
            match self.program[self.pointer]:
                case 1:
                    self.program[self.program[self.pointer + 3]] = self.program[self.program[self.pointer + 1]] + self.program[self.program[self.pointer + 2]]
                    self.pointer += 4
                    continue
                case 2:
                    self.program[program[self.pointer + 3]] = self.program[self.program[self.pointer + 1]] * self.program[self.program[self.pointer + 2]]
                    self.pointer += 4
                    continue
                case 99:
                    break
            self.pointer += 1
        return self.program
        
    
for i in range(100):
    for j in range(100):
        c = IntCode(program=deepcopy(program))
        try: 
            p = c.run(i, j)
        except:
            continue
        if p[0] == 19690720:
            print(100 * i + j)
            break