with open("input.txt") as f:
    instructions: list[str] = f.readlines()

status: int = 50
zeros: int = 0

for op in instructions:
    turn: int = int(op[1:]) # slice off instruction letter
    step = -1 if op[0] == "L" else 1

    for i in range(turn):
        status = (status + step) % 100
        if status == 0: zeros += 1

print("=", zeros)