import string

text = string.ascii_letters + string.digits

print(text[0])	# First symbol

print(text[-1])	  # Last symbol

print(text[2])  # Third from beginning
print(text[-3])    # Third from the end

print(text[:8])		#  Slice of first 8 symbols

print(text[::3]) 	# Print each 3rd symbol

# First solution
print(text[int(len(text)/2):int(len(text)/2)+1])	# Counting first and last boundary
# Another solutuon
print(text[int(len(text) / 2 + 0.5)])			# Counting index

print(text[::-1])		# Reversed text. -1 means the it will print each symbol but will start from the end because of minus

