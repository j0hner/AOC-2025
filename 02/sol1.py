import re

pattern = re.compile(r'(^(\d+)\2$)', re.MULTILINE)

with open("ranges.txt") as f:
    ranges: str = f.read()

matches: list[tuple[str]] = re.findall(pattern, ranges)

# with open("matches.txt", "w+") as f:
#     f.write("\n".join(str(match[0]) for match in matches))

# print(matches)
print(sum(int(match[0]) for match in matches))