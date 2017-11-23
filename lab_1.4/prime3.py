def prime(a):
    return all(a % i for i in range(2, a))

# Calling function above and asking for enter. Or you can replace the 'input()' with your value explicitly
prime(input())