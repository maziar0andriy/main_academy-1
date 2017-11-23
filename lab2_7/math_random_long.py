# Importing modules
import math
import random

int_seq = random.sample(range(100), 5) 		# Generate random sequence
float_random = random.random()				# Generate random float

# Printing variables
print(int_seq)
print(float_random)

int_seq_max = max(int_seq)					# Find max value of sequence given

floor_div_result = int_seq_max // float_random		# Floor division

print(math.factorial(floor_div_result))			# Factorial

