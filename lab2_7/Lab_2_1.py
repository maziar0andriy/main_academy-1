# Create variable with name var1
var1 = 10

# Check type of var1 with type function
var_type = type(var1)
print(var_type)

# Check is var1 is True
print(var1 is True)

# Check is var1 is False
print(var1 is False)

# Create var2
var2 = var1 or True
# in case of var1 value False or None or 0, etc we will get True else var 1
print (var2)

# Check is var2 is True
print(var2 is True)

# Check is var2 is False
print(var2 is False)

# Check result
print(var1 and var2)
