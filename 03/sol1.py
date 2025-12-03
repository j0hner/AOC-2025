with open("input.txt") as f:
    banks: list[str] = f.readlines()

joltage: int = 0

for bank in banks:
    ints: list[int] = [int(char) for char in bank.strip()]
    first_max = max(ints[:-1])
    second_max = max(ints[ints.index(first_max) + 1:])

    increase = int(f"{first_max}{second_max}")
    print(increase)
    joltage += int(f"{first_max}{second_max}")

print(joltage)