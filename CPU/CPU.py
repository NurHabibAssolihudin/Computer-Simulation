from .CU import ControlUnit
from .ALU import ALU
from .Registers import Registers
class CPU:
    def __init__(self, ram):
        self.up = True
        self.ram = ram
        self.registers = Registers()
        self.alu = ALU()
        self.cu_operations = {
            "LOAD",
            "STORE",
            "JNZ"
        }
        self.alu_operations = {
            "ADD",
            "SUB",
            "MUL",
            "DIV",
            "AND",
            "OR",
            "NOT"
        }
        self.cu = ControlUnit(self)
    
    def __str__(self):
        return str(self.cu)
    
    def run(self):
        self.cu.cycle()