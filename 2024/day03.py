import re, sys

memory = "".join(sys.stdin.readlines())

matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory)
result = sum([int(x)*int(y) for x,y in matches])

print(f"Part 1: {result}")

# Strip irrelevant dont/do sequences as well as dont-to-the-end (if present)
memory_modded = re.sub(r"don't\(\).*?do\(\)", "", memory, flags = re.DOTALL)
memory_modded = re.sub(r"don't\(\).*$", "", memory_modded, flags = re.DOTALL + re.MULTILINE)

matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory_modded)
result = sum([int(x)*int(y) for x,y in matches])

print(f"Part 2: {result}")

