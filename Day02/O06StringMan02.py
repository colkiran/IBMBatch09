
# maketrans and translate

st = 'hello world'
print(f"st :{st}")

print('the length of a and b should be same')
a = 'helowrd'
b = 'HELOWRD'

res_tbl = st.maketrans(a, b)
print(f"res_tbl :{res_tbl}")

print("translate".center(60, "-"))
res = st.translate(res_tbl)
print(f"res :{res}")

print("-" * 60)
# formatting
# c style formatting - printf

format = "Welcome %s, what a %s player"
print(f"format :{format}")

values = ("Sachin", 'superb')
print(f"values :{values}")

print("-" * 60)
print(format, values)
print(format % values)

print("-" * 60)
format = "Welcome %s, your rating of %.3f, what a %s player"

print(format % ("Sachin", 4, "class"))
print(format % ("Sachin", 4.8, "class"))
print(format % ("Sachin", 4.79999999, "class"))
print(format % ("Sachin", 4, "class"))

print("-" * 60)
print("Welcome %s, your rating pf %.3f, what a %s player" % ('Sachin', 4.87922, 'class'))
# unix style formatting
from string import Template

tmpl = Template("Welcome $name,  what a $adj player")
print(tmpl)
print(tmpl.substitute(name='Sachin', adj = 'super'))
print("-" * 60)

# format string from python

print("Welcome {}, what a {} player for {}".format("Sachin", "class", "India"))


print("Welcome {0}, what a {1} player for {2}".format("Sachin", "class", "India"))

print("Welcome {2}, what a {0} player for {1}".format("Sachin", "class", "India"))

print("Welcome {name}, what a {adj} player for {ctry}".format(name ="Sachin", adj = "class", ctry = "India"))

print("Welcome {name}, your rating of {rating:.3f}, what a {adj} player".format(name="Sachin", rating=4.8, adj="class"))

print("-" * 60)
# interpolation
from math import pi, e
print(f"PI = {pi} and Eulers constant = {e}")

print("PI = {} and Eulers Constant = {}".format(pi, e))

print("PI = {} and Eulers Constant = {} magic number = {magic}".format(pi, e, magic=40585))

print("PI = {0} and Eulers Constant = {1} magic number = {magic}".format(pi, e, magic=40585))

print("-" * 60)
full_name = ['Sachin', 'Tendulkar']     # list
print(f"full_name :{full_name}")
print("Mr.{name}".format(name = full_name))
print("Mr.{name[0]} {name[1]}".format(name=full_name))

print("-" * 60)
import math
print(math.__name__)            # dunder name
print(__name__)                 # name of the current module __main__

print("the {mod.__name__} module gives the value of pi = {mod.pi} and Eulers constant = {mod.e}".format(mod=math))
