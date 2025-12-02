from functools import reduce
import sys

STATE = (50, 0)

# Calculate the incremental amount for a given instruction; for example, L5 yields -5
amount = lambda x : (1 if x[0] == 'R' else -1) * int(x[1:])

# Given a starting and ending number, determine how many times we passed zero.
# 
# Naive approach is to us // to count passes of zero, and then add 1 if we ended up at zero exactly.
# However, 
# Reduction function takes input of a state - (counter, zerocount) - and an instruction such as L5, and produces a state
# For the zero counter, we take into account the number of times we passed 0 as well as whether we ended up on zero
increment = lambda state, instruction : ((state[0] + amount(instruction)) % 100,
                                         state[1] + abs((state[0] + amount(instruction)) // 100) + (1 if (state[0] + amount(instruction)) == 0 else 0))

# Reduce the input given our starting state
result = reduce(increment, sys.stdin.readlines(), STATE)

print(result[1])

# 6806 is too high
print(increment((50, 0), "L50"))
print(increment((50, 0), "R50"))
print(increment((50, 0), "L5"))
print(increment((50, 0), "R5"))
print(increment((50, 0), "L500"))
print(increment((50, 0), "R500"))
print(increment((50, 0), "L550"))
print(increment((50, 0), "R550"))

