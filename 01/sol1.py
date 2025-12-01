with open("input.txt") as f:
    instructions: list[str] = f.readlines()

status: int = 50
zeros: int = 0

for op in instructions:
    turn: int = int(op[1:]) # slice off instruction letter
    if op[0] == "L": turn *= -1 # subrtact if turning left
    status = (status + turn) % 100 # wrap around

    if status == 0: zeros += 1 # increment counter

print(zeros)