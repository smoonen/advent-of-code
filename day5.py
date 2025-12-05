import sys

ranges, items = "".join(sys.stdin.readlines()).rstrip().split("\n\n")
ranges = list(map(lambda x : list(map(int, x.split("-"))), ranges.split("\n")))
items = list(map(int, items.split("\n")))

fresh = sum([int(any([item in range(r[0], r[1]+1) for r in ranges])) for item in items])

print(f"Part 1: {fresh}")

