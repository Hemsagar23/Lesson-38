a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

print("\nBefore swapping:")
print("a =", a, ", b =", b, ", c =", c)

a, b, c = c, a, b

print("\nAfter swapping:")
print("a =", a, ", b =", b, ", c =", c)