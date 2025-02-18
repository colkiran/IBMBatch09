
"""
1. arithmetic
2. Augmentor - x++, x--
3. comparison or relational
4. logical
5. Bitwise
6. ternary
"""

print("Arithmetic Operators".center(60, "-"))
print(f"Add :10 + 3 = {10 + 3}")
print(f"Sub :10 - 3 = {10 - 3}")
print(f"Mul :10 * 3 = {10 * 3}")
print(f"Div :10 / 3 = {10 / 3}")
print(f"Flr Div :10 // 3 = {10 // 3}")
print(f"Mod : 10 % 3 :{10 % 3}")
print(f"Power :10 ** 3 :{10 ** 3}")
print(f"round :round(10 / 3, 2) = {round(10 / 3, 2)}")

print("Augmentor Operator".center(60, "-"))
# =, +=, -=, *=, /=
x = 10
print(f"x :{x}")

x += 5
print(f"x :{x}")

x /= 3
print(f"x :{x}")

print("Comparison".center(60, "-"))
# ==, >, <, >=, <=, !=
a = 10
b = 20
print(f"a = {a}, b = {b}")
print(f"a == b :{a == b}")
print(f"a >= b :{a >= b}")
print(f"a <= b :{a <= b}")
print(f"a != b :{a != b}")

print("Logical Operators".center(60, "-"))
# and, or, not
print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 1 and 2 == 1 :{1 == 1 and 2 == 1}")

print("-" * 60)
print(f"1 == 1 or 2 == 2 :{1 == 1 or 2 == 2}")
print(f"1 == 1 or 2 == 1 :{1 == 1 or 2 == 1}")
print(f"1 == 2 or 2 == 1 :{1 == 2 or 2 == 1}")

print("-" * 60)
print(f"not(1 == 1 or 2 == 1) :{not(1 == 1 or 2 == 1)}")
print(f"not(1 == 2 or 2 == 1) :{not(1 == 2 or 2 == 1)}")

print("-" * 60)
print(f"ord('a') :{ord('a')}")      # integer representation of unicode                                     characters (ascii)
print(f"ord('z') :{ord('z')}")
print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")
print(f"'apple' > 'orange' :{'apple' > 'orange'}")
print(f"'apple' < 'orange' :{'apple' < 'orange'}")

print("Bitwise Operators".center(60, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"5 >> 1 :{5 >> 1}")
print(f"16 >> 1 :{16 >> 1}")

print("Ternary Operators".center(60, "-"))
age = 25
print("eligible" if age > 17 else "not eligible")
