class ControlUnit:
    def __init__(self, cpu):
        self.cpu = cpu
        self.registers = cpu.registers
        self.alu = cpu.alu
        self.ram = cpu.ram
        self.cu_operations = cpu.cu_operations
        self.alu_operations = cpu.alu_operations

    def __str__(self):
        return f'PC: {self.registers.pc}, IR: {self.registers.ir}, ACC: {self.registers.acc}, UP: {self.cpu.up}'
    
    def fetch(self):
        self.registers.ir = self.ram.read(self.registers.pc)
        self.registers.pc = self.registers.pc + 1
    
    def decode(self):
        if self.registers.ir == 'HALT':
            self.cpu.up = False
            return None, None
        else:
            operation = str(self.registers.ir).split(' ')
            return operation[0], int(operation[1])
            
    def execute(self, opcode, operand):
        if opcode in self.cu_operations:
            match opcode:
                case "LOAD":
                    self.memory_read(operand)
                case "STORE":
                    self.memory_write(operand)
                case "JNZ":
                    self.jnz(operand)
        elif opcode in self.alu_operations:
            self.registers.acc = self.alu.execute(opcode, self.registers.acc, self.ram.read(operand))
    
    def memory_read(self, address):
        print(f'LOAD {address} ({self.ram.read(address)}) -> ACC ({self.registers.acc})')
        self.registers.acc = self.ram.read(address)
    
    def memory_write(self, address):
        print(f'STORE {address} ({self.ram.read(address)}) <- ACC ({self.registers.acc})')
        self.ram.write(address, self.registers.acc)
    
    def jnz(self, address):
        if self.registers.acc != 0:
            print(f'JNZ {address} -> PC ({self.registers.pc})')
            self.registers.pc = address

    def cycle(self):
        while self.cpu.up:
            self.fetch()
            opcode, operand = self.decode()
            self.execute(opcode, operand)
            print(self)