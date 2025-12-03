with open("test.txt") as f:
    ranges: list[str] = f.read().split(",")

# unpack ranges into a text file

with open("test-ranges.txt", "w+") as f:
    for id_range in ranges:
        split: list[str] = id_range.split("-")
        
        begin: int = int(split[0])
        end: int = int(split[1])

        f.write("\n".join(str(num) for num in range(begin, end + 1)))
        f.write("\n")