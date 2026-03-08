class ALU:
    def __init__(self):
        self.flags = {
            'ZERO': 0,
            'NEGATIVE': 0
        }

    def execute(self, operation, acc, operand=0):
        match operation:
            case "ADD":
                result = acc + operand
                print(f'ADD ({operand}) -> ACC ({result})')
            case "SUB":
                result = acc - operand
                print(f'SUB ({operand}) -> ACC ({result})')
            case "MUL":
                result = acc * operand
                print(f'MUL ({operand}) -> ACC ({result})')
            case "DIV":
                result = acc // operand
                print(f'DIV ({operand}) -> ACC ({result})')
            case "AND":
                result = acc & operand
                print(f'AND ({operand}) -> ACC ({result})')
            case "OR":
                result = acc | operand
                print(f'OR ({operand}) -> ACC ({result})')
            case "NOT":
                result = ~acc
                print(f'NOT ({operand}) -> ACC ({result})')
            case _:
                raise ValueError(f"Unknown ALU operation: {operation}")
        self.update_flags(result)
        return result
    
    def update_flags(self, result):
        self.flags["ZERO"] = int(result == 0)
        self.flags["NEGATIVE"] = int(result < 0)