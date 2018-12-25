
from utils import operations, read_input

if __name__ == "__main__":
    bound, instructions = read_input()

    registry = [0] * 6
    pointer = 0
    n = 0
    first = True
    while pointer < len(instructions) and n < 60:
        registry[bound] = pointer
        instr = instructions[pointer]
        operation = operations[instr[0]]
        print(registry, instr)
        registry = operation(registry, instr[1])
        if first and registry[5] == 24:
            first = False
            registry[4] = 256
            registry[5] = 24
            registry[0] = ((((registry[2]*65899)&16777215)+1)*65899)&16777215
            pointer = 25
            n = 0
        else:
            pointer = registry[bound]
            pointer += 1
        n += 1
    print(f"The value of register 0 is {registry[0]}")
