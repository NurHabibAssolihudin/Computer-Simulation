from CPU.CPU import CPU
from Memory.RAM import RAM

def main():
    memory1 = RAM(memory={
        0: 'LOAD 5',
        1: 'ADD 6',
        2: 'SUB 7',
        3: 'STORE 8',
        4: 'HALT',
        5: 7,
        6: 8,
        7: 2,
        8: 0
    })
    memory2 = RAM(memory={
        0: 'LOAD 10',
        1: 'SUB 9',
        2: 'STORE 8',
        3: 'JNZ 1',
        4: 'HALT',
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 1,
        10: 10
    })
    print('memory1: ', memory1.memory)
    print('memory2: ', memory2.memory)
    cpu = CPU(ram=memory1)
    cpu.run()
    cpu = CPU(ram=memory2)
    cpu.run()


if __name__ == "__main__":
    main()
