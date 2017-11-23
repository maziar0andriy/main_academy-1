import string

lst = list(string.ascii_letters + string.digits)

print(lst[0])	# First symbol

print(lst[-1])	  # Last symbol

print(lst[2])  # Third from beginning
print(lst[-3])    # Third from the end

print(lst[:10])		#  Slice of first 10 symbols

print(lst[::2]) 	# Print each 2nd symbol

# Print only integer values from list
int_lst = []
for i in lst:
    try:
        int_lst.append(int(i)) # Only integer can be converted here
    except:
        pass
    
print(int_lst)
print(int_lst[::-1])

print("-".join(lst))  # String from list

