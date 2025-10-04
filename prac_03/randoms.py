import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 1?
# A random number is generated each time it runs

# What was the smallest number you could have seen, what was the largest?
# The smallest number I have seen is 5, and the largest is 19.

# What did you see on line 2?
# I saw the odd numbers between 3 and 9.

# What was the smallest number you could have seen, what was the largest?
# The smallest number is 3, and the largest is 9.

# Could line 2 have produced a 4?
# No

# What did you see on line 3?
# A decimal between 2.5 and 3.5

# What was the smallest number you could have seen, what was the largest?
# The smallest number is 2.5361846381638, and the largest is 5.4384716473849.

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))