import re
import sys
from dataclasses import dataclass


@dataclass
class State:
    reg_A: int
    reg_B: int
    reg_C: int
    program: list[int]  # 3-bit numbers
    ip: int = 0

    output = ""

    def step(self) -> bool:
        if self.ip >= len(self.program):
            return True

        opcode, operand = self.program[self.ip : self.ip + 2]
        match opcode:
            case 0:  # adv
                self.reg_A = self.reg_A // 2 ** self.combo(operand)
            case 1:  # bxl
                self.reg_B = self.reg_B ^ operand
            case 2:  # bst
                self.reg_B = self.combo(operand) % 8
            case 3:  # jnz
                if self.reg_A != 0:
                    self.ip = operand
                    return False
            case 4:  # bxc
                self.reg_B = self.reg_B ^ self.reg_C
            case 5:  # out
                if self.output:
                    self.output += ","
                self.output += str(self.combo(operand) % 8)
            case 6:  # bdv
                self.reg_B = self.reg_A // 2 ** self.combo(operand)
            case 7:  # cdv
                self.reg_C = self.reg_A // 2 ** self.combo(operand)
            case _:
                print("Unknown opcode")
        self.ip += 2
        return False

    def combo(self, operand: int) -> int:
        if operand >= 0 and operand <= 3:
            return operand
        elif operand == 4:
            return self.reg_A
        elif operand == 5:
            return self.reg_B
        elif operand == 6:
            return self.reg_C
        else:
            raise ValueError("Invalid operand")


def parse(data: str) -> State:
    PATTERN = (
        r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: ([0-9,]+)"
    )
    m = re.match(PATTERN, data)
    if m is None:
        raise ValueError("Invalid input")
    reg_A, reg_B, reg_C, program = m.groups()
    return State(int(reg_A), int(reg_B), int(reg_C), list(map(int, program.split(","))))


if __name__ == "__main__":
    state = parse(sys.stdin.read())

    while not state.step():
        pass

    print(state.output)
