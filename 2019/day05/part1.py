from copy import deepcopy


program = [*map(int, open("2019/day05/input.txt").read().split(","))]


class IntCode:
    def __init__(self, program):
        self.program = program
        self.pointer = 0
        self.output = []
    
    def op1(self):
        self.program[self.program[self.pointer + 3]] = self.map_modes["c"] + self.map_modes["b"]

    def op2(self):
        self.program[self.program[self.pointer + 3]] = self.map_modes["c"] * self.map_modes["b"]
    
    def op3(self, inp):
        self.program[self.program[self.pointer +  1]] = inp 

    def op4(self, x , pos):
        self.program[pos] = x


    def run(self, inp=1):


        while True:
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

            self.mode_c = digits[2]
            self.mode_b = digits[1]
            self.mode_a = digits[0]
            self.map_modes = {}

            print(opcode)
            print(digits)

            if opcode == 2 or opcode == 1:
                match self.mode_c:
                    case 0:
                        self.map_modes['c'] = self.program[self.program[self.pointer + 1]]
                    case 1:
                        self.map_modes['c'] = self.program[self.pointer + 1]

                match self.mode_b:
                    case 0:
                        self.map_modes['b'] = self.program[self.program[self.pointer + 2]]
                    case 1:
                        self.map_modes['b'] = self.program[self.pointer + 2]
                
                match self.mode_a:
                    case 0:
                        self.map_modes['a'] = self.program[self.program[self.pointer + 3]]
                    case 1:
                        self.map_modes['a'] = self.program[self.pointer + 3]

            if opcode == 4:
                match self.mode_c:
                    case 0:
                        self.map_modes['c'] = self.program[self.program[self.pointer + 1]]
                    case 1:
                        self.map_modes['c'] = self.program[self.pointer + 1]

            print(self.map_modes)
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
                    self.op3(inp=inp)
                    self.pointer += 2
                    continue
                case 4:
                    self.output.append(self.map_modes['c'])
                    print(self.map_modes["c"])
                    self.pointer += 2
                    continue
                
                case 99:
                    print("end of program")
                    return self.output
        # return self.output
        
c = IntCode(program=program)
output = c.run(inp=1)
print(output)

    