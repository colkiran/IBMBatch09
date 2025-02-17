
a = 10
b = -10

print(f"a :{a}")        # format string or f string used for interpolation
print(type(a))          # RTTI => Run Time Type Identification
print(f"b :{b}")
print(type(b))

print("-" * 60)
c = 10.34
d = -10.34

print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 60)
e = +2e3
f = -2e3

print(f"e :{e}")
print(type(e))        # float
print(f"f :{f}")
print(type(f))        # float

print("-" * 60)
g = 10 + 3j
h = 10 - 3j

print(f"g :{g}")
print(type(g))        # complex
print(f"h :{h}")
print(type(h))        # complex

print("-" * 60)
print(max(36, 78, 84))
print(min(35, 78, 84))

print("-" * 60)
x = 2 + 3.5
print(x)
print(type(x))

x = 2
y = 3.5
z = x + y

print(f"x = {type(x)}")
print(f"y = {type(y)}")
print(f"z = {type(z)}")

print("Conversion".center(60, "-"))
a = -100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")
