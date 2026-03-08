class RAM:
    def __init__(self, memory):
        self.memory = memory

    def __str__(self):
        return str(self.memory)
    
    def read(self, address):
        return self.memory[address]

    def write(self, address, value):
        self.memory[address] = value