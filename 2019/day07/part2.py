from copy import deepcopy
from itertools import permutations
from collections import deque


program = [*map(int, open("2019/day07/input.txt").read().split(","))]


class IntCode:
    def __init__(self, program, inp):
        self.program = program
        self.pointer = 0
        self.output = []
        self.inp = inp
    
    def op1(self):
        self.program[self.program[self.pointer + 3]] = self.map_modes[1] + self.map_modes[2]

    def op2(self):
        self.program[self.program[self.pointer + 3]] = self.map_modes[1] * self.map_modes[2]
    
    def op3(self, inp):
        self.program[self.program[self.pointer +  1]] = inp 

    def op4(self, x , pos):
        self.program[pos] = x

    # two parameters
    def op5(self):
        if self.map_modes[1] != 0:
            self.pointer = self.map_modes[2]
            return
        self.pointer += 3

    # two parameters
    def op6(self):
        if self.map_modes[1] == 0:
            self.pointer = self.map_modes[2]
            return
        self.pointer += 3 
    
    # three parameters
    def op7(self):
        if self.map_modes[1] < self.map_modes[2]:
            self.program[self.program[self.pointer + 3]] = 1
        else:
            self.program[self.program[self.pointer + 3]] = 0
        self.pointer += 4
    
    # three parameters
    def op8(self):
        if self.map_modes[1] == self.map_modes[2]:
            self.program[self.program[self.pointer + 3]] = 1
        else:
            self.program[self.program[self.pointer + 3]] = 0
        self.pointer += 4


    def run(self):

        opcode = 42
        while opcode != 99:
            print("Updated pointer ", self.pointer)
            instruction = deepcopy(self.program[self.pointer])
            digits = []
            x = deepcopy(instruction)
            while True:
                last_digit = x % 10
                digits.append(last_digit)
                x //= 10
                if x == 0:
                    break
            
            digits = digits[::-1]
            if len(digits) != 5:
                digits = [0] * (5 - len(digits)) + digits
            opcode = int("".join([str(x) for x in digits][-2:]))

            # Parameter modes
            self.param1 = digits[2]
            self.param2 = digits[1]
            self.param3 = digits[0]
            self.map_modes = {}


            # Get corresponding values of parameters
            if opcode == 2 or opcode == 1 or opcode == 8 or opcode == 7:
                match self.param1:
                    case 0:
                        self.map_modes[1] = self.program[self.program[self.pointer + 1]]
                    case 1:
                        self.map_modes[1] = self.program[self.pointer + 1]

                match self.param2:
                    case 0:
                        self.map_modes[2] = self.program[self.program[self.pointer + 2]]
                    case 1:
                        self.map_modes[2] = self.program[self.pointer + 2]
                
                match self.param3:
                    case 0:
                        self.map_modes[3] = self.program[self.program[self.pointer + 3]]
                    case 1:
                        self.map_modes[3] = self.program[self.pointer + 3]

            if opcode == 4:
                match self.param1:
                    case 0:
                        self.map_modes[1] = self.program[self.program[self.pointer + 1]]
                    case 1:
                        self.map_modes[1] = self.program[self.pointer + 1]
            
            if opcode == 5 or opcode == 6:
                match self.param1:
                    case 0:
                        self.map_modes[1] = self.program[self.program[self.pointer + 1]]
                    case 1:
                        self.map_modes[1] = self.program[self.pointer + 1]
                match self.param2:
                    case 0:
                        self.map_modes[2] = self.program[self.program[self.pointer + 2]]
                    case 1:
                        self.map_modes[2] = self.program[self.pointer + 2]

            # print(self.map_modes)
            match opcode:
                case 1:
                    self.op1()
                    self.pointer += 4
                    continue
                case 2:
                    self.op2()
                    self.pointer += 4
                    continue
                case 3:
                    val = self.inp.popleft()
                    self.op3(inp=val)
                    self.pointer += 2
                    continue
                case 4:
                    self.output.append(self.map_modes[1])
                    print(self.map_modes[1])
                    self.pointer += 2
                    return self.map_modes[1]
                case 5:
                    self.op5()
                    continue
                case 6:
                    self.op6()
                    continue
                case 7:
                    self.op7()
                    continue
                case 8:
                    self.op8()
                    continue
                
                case 99:
                    return 
        
poss = permutations(list(range(5)))
tot = []
seq = [9,8,7,6,5]
VM = {}

# init VMs
best = -float('inf')
for p in permutations(range(5, 10)):
    for i in range(len(seq)):
        VM[i] = IntCode(program=deepcopy(program), inp=deque([p[i]]))
    VM[0].inp.append(0)
    i = 0
    while True:
        # print("pointer", VM[i % 5].pointer)
        output = VM[i % 5].run()
        if output is not None:
            best = max(best, output)
        if output is None:
            print(best)
            break
        VM[(i + 1) % 5].inp.append(output)
        i += 1
