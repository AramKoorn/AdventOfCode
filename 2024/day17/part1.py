class Computer:
    def __init__(self, a, b, c, program: list):
        self.a = a
        self.b = b
        self.c = c
        self.program = program
        self.output = []
        self.pointer = 0
        self.ops = [self.op0, self.op1, self.op2, self.op3, self.op4, self.op5, self.op6, self.op7]

    def get_combo(self, x):
        if x <= 3:
            return x
        return [self.a, self.b, self.c ][x - 4]


    def op0(self, operand):
        comb = self.get_combo(operand)
        self.a = int(self.a / (2**comb))
    
    def op1(self, operand):
        self.b = self.b ^ operand
    
    def op2(self, operand):
        comb = self.get_combo(operand)
        self.b = comb % 8

    def op3(self, operand):
        if self.a >  0:
            self.pointer = operand
    
    def op4(self, operand):
        self.b = self.b ^ self.c
    
    def op5(self, operand):
        self.output.append(self.get_combo(operand) % 8)
    
    def op6(self, operand):
        comb = self.get_combo(operand)
        self.b = int(self.a / (2**comb))
    
    def op7(self, operand):
        comb = self.get_combo(operand)
        self.c = int(self.a / (2**comb))
    
    def run(self):
        while self.pointer < len(self.program):
            instruction = self.program[self.pointer]
            operand = self.program[self.pointer + 1]
            self.pointer += 2
            self.ops[instruction](operand)
        print(",".join(list(map(str, self.output))))


# a = 729
# b = 0
# c = 0
# program = [0,1,5,4,3,0]

a = 52042868
b = 0
c = 0
program = [2,4,1,7,7,5,0,3,4,4,1,7,5,5,3,0]

c = Computer(a, b, c, program)
c.run()