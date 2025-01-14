from copy import deepcopy
from itertools import permutations
from collections import deque


program = [*map(int, open("2019/day09/input.txt").read().split(","))]

class VM:
    def __init__(self, program, inp):
        self.program = program
        self.program += [0] * 10000000
        self.pointer = 0
        self.rel_pointer = 0
        self.output = []
        self.inp = inp
    
    def op1(self):
        if self.pointer == 109:
            debug = True
        self.program[self.writes[3]] = self.map_modes[1] + self.map_modes[2]

    def op2(self):
        self.program[self.writes[3]] = self.map_modes[1] * self.map_modes[2]
    
    def op3(self, inp):
        self.program[self.program[self.pointer +  1]] = inp 

    def op4(self, x , pos):
        self.program[pos] = x

    # two parameters
    def op5(self):
        if self.pointer == 849:
            debug = True
        if self.map_modes[1] != 0:
            print("reads", self.map_modes[2])
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
            self.program[self.writes[3]] = 1
        else:
            self.program[self.writes[3]] = 0
        self.pointer += 4
    
    # three parameters
    def op8(self):
        if self.pointer == 845:
            debug = True
        if self.map_modes[1] == self.map_modes[2]:
            self.program[self.writes[3]] = 1
        else:
            self.program[self.writes[3]] = 0
        self.pointer += 4

    def get_values(self, params):
        self.map_modes = {}
        for i, param in enumerate(params):
            # print("param", param)
            match param:
                case 0:
                    self.map_modes[i + 1] = self.program[self.program[self.pointer + (i + 1)]]
                case 1:
                    self.map_modes[i + 1] = self.program[self.pointer + (i + 1)]
                case 2:
                    self.map_modes[i + 1] = self.program[self.rel_pointer + self.program[self.pointer + (i + 1)]]
        return self.map_modes
    
    def get_writes(self, params):

        self.writes = {}

        for i, param in enumerate(params):
            match param:
                case 2:
                    self.writes[i + 1] = self.rel_pointer + self.program[self.pointer + (i + 1)]
                case _:
                    self.writes[i + 1] = self.program[self.pointer + (i + 1)]
        return self.writes

    def run(self):

        opcode = 42
        while opcode != 99:
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

            print("OPCODE", opcode)
            print("Updated pointer ", self.pointer)
            print("memory 1015", self.program[1015])
            match opcode:
                case 1:
                    self.get_values(params=[self.param1, self.param2, self.param3])
                    self.get_writes(params=[self.param1, self.param2, self.param3])
                    self.op1()
                    self.pointer += 4
                    continue
                case 2:
                    self.get_values(params=[self.param1, self.param2, self.param3])
                    self.get_writes(params=[self.param1, self.param2, self.param3])
                    self.op2()
                    self.pointer += 4
                    continue
                case 3:
                    self.get_values(params=[self.param1])
                    self.get_writes(params=[self.param1])
                    val = self.inp.popleft()
                    # self.program[]
                    if self.param1 == 2:
                        self.program[self.rel_pointer + self.program[self.pointer + 1]] = val
                    else:
                        self.program[self.program[self.pointer + 1]] = val
                    # self.op3(inp=val)
                    self.pointer += 2
                    continue
                case 4:
                    self.get_values(params=[self.param1])
                    self.output.append(self.map_modes[1])
                    print("output", self.map_modes[1])
                    self.pointer += 2
                case 5:
                    self.get_values(params=[self.param1, self.param2])
                    self.op5()
                    continue
                case 6:
                    self.get_values(params=[self.param1, self.param2])
                    self.get_writes(params=[self.param1, self.param2])
                    self.op6()
                    continue
                case 7:
                    self.get_values(params=[self.param1, self.param2, self.param3])
                    self.get_writes(params=[self.param1, self.param2, self.param3])
                    self.op7()
                    continue
                case 8:
                    self.get_values(params=[self.param1, self.param2, self.param3])
                    self.get_writes(params=[self.param1, self.param2, self.param3])
                    self.op8()
                    continue
                case 9:
                    self.get_values(params=[self.param1])
                    self.rel_pointer += self.map_modes[1]
                    self.pointer += 2
                
                case 99:
                    print("final output", self.output)
                    return self.output 
        
vm = VM(program=program, inp=deque([1]))
vm.run()