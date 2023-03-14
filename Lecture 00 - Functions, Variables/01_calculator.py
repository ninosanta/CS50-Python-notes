##############################################################
#                         Integers                           #
##############################################################
x = input("What's x? ")
y = input("What's y? ")
z = int(x) + int(y)

print(z)

# Nesting functions... exaggerating a bit
print("")
print(int(input("What's x? ")) + int(input("What's y? ")))


##############################################################
#                         Floats                             #
##############################################################
x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)

# Rounding the result: round(number[ , ndigits])
print(round(x + y, 0))

z = round(x + y)
print(f"{z}")
print(f"{z:,}")  # thousands separator US: 1,000

"""Divisions"""
z = round(x / y, 2)  # e.g., x = 2, y = 3 -> z = 0.67
print(f"{(x / y):.2f}")  # same result
