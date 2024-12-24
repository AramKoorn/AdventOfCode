from tqdm import tqdm


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
        return self.output
    
    def reset_computer(self, a):
    
        self.a = a
        self.b = 0 
        self.c = 0
        self.output = []
        self.pointer = 0
    
    def find_a(self):
        i = 1
        power = len(self.program) - 1
        a = 8 ** power  # start incrementing when we first output 16 digits
        digits = [self.program[-1]]
        power -= 1
        cnt = 0
        while self.output != self.program:
            a += 8 ** power 
            self.reset_computer(a)
            self.run()
            if cnt == 0 and self.output[-i:] == [4, 1, 7, 5, 5, 3, 0]:
                print("test")
                cnt += 1
                continue
            if self.output[-(i):] == digits:
                print("test")
                print(digits)
                power -= 1
                power = max(power, 0)
                print(power)
                i += 1
                digits = self.program[-i:] 
                print(a)
            # print(self.output)
        print(a)


program = [2,4,1,7,7,5,0,3,4,4,1,7,5,5,3,0]
c = Computer(a=0, b=0, c=0, program=program)
c.find_a()

# a = 729
# b = 0
# c = 0
# program = [0,1,5,4,3,0]

'''
first digit A < 8 
second digit 8 <= A <= 64
thrid digit 64 < A <  512
etc.


'''

# from collections import Counter
# cnt = Counter()
# program = [2,4,1,7,7,5,0,3,4,4,1,7,5,5,3,0]
# b = 0
# c = 0
# a = 8 ** 15 
# a = 8 ** 16 -1

# nth = 15
# a_start = 8**nth + (6 * (8**nth)) 
# a_end = 8**nth + (7 * (8**nth))  
# print(a_end - a_start)


# program = [2,4,1,7,7,5,0,3,4,4,1,7,5,5,3,0]
# b = 0
# c = 0


