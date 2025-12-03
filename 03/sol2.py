


with open("input.txt") as f:
    banks: list[str] = f.readlines()


joltage: int = 0
joltage_len: int = 12

for bank in banks:
    ints: list[int] = [int(char) for char in bank.strip()]
    left_cut: int = 0
    rslt: str = ""
    
    for i in range(joltage_len, 0, -1):
        slice:list[int] = ints[left_cut : len(ints) -i + 1]
        # print("_" * left_cut, "".join(str(i) for i in slice), "_" * (i + 1) , sep="")
        nth_max = max(slice)
        left_cut = left_cut + ints[left_cut:].index(nth_max) + 1
        rslt += str(nth_max)

    increase = int(rslt)
    # print()
    # print(increase)
    joltage += increase

print(joltage)