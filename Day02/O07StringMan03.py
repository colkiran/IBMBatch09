
# Conversions
print("Coversions".center(60, "-"))
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("-" * 60)
print("The number {num} {num} {num} ".format(num=36))
print("The number {num} {num:f} {num:b} ".format(num=36))
print("The number {num:10} {num:f} {num:b} ".format(num=36))
print("The number {num:5} {num:f} {num:b} ".format(num=36))
print("The number {num:5} {num:f} {num:b} ".format(num=362372981092))
print("The number {num:5} {num:f} {num:b} ".format(num=36))

print(f"Alignment".center(60, "-"))
from math import pi
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))
print("{num:10.2}".format(num = pi))
print("{num:10.3}".format(num = pi))
print("{num:10.4}".format(num = pi))
print("{num:10.5}".format(num = pi))

print("-" * 60)
print("{num:>15} Tendulkar".format(num="Sachin"))       # right align
print("{num:^15} Tendulkar".format(num="Sachin"))       # center align
print("{num:<15} Tendulkar".format(num="Sachin"))       # left align

print("-" * 60)
print("{num:010.3}".format(num = pi))
print("{num:010.4}".format(num = pi))
print("{num:010.5}".format(num = pi))

print("-" * 60)
print("{num:-^60}".format(num = "Python"))
print("{num:*^60}".format(num = "Python"))
print("{num:+^60}".format(num = "Python"))

print("Python".center(60, "-"))

print("-" * 60)
print("{0:10.2f} \t {1:10.2f}".format(pi, -pi))
print("{0:10.2f} \t {1:=10.2f}".format(pi, -pi))
print("{0:10.2f} \t {1:=010.2f}".format(pi, -pi))
print("{0:10.2f} \t {1:010.2f}".format(pi, -pi))

