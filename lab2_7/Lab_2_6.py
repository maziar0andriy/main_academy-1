import string

set1 = set(string.ascii_letters + string.digits[3:7] + string.digits[:5])
set2 = set(string.ascii_letters + string.digits[3:7] + string.digits[6:])

print(set1)	# First set
print(set2)	# Second set

tpl_intersection = tuple(set1.intersection(set2))
print(tpl_intersection)  # Print intersection

tpl_diff = tuple(set1.difference(set2))
print(tpl_diff)    #  # Print difference between two sets

print(tpl_intersection[:3]) #Slice first 3 symbols from first tuple

print(set(string.digits).intersection(set2)) # Print only numbers from second set

print(tpl_intersection[::-1]) # Reverse tuple

print(list(tpl_intersection), list(tpl_diff))

