
import gurgaon.mymodule as md
from  gurgaon.mymodule import Player, outerFun

print("-" * 60)
import sys

for pth in sys.path:
    print(pth)


print("-" * 60)

@outerFun
def concatenate(a, b):
    print(f"concatenating {a} and {b}")
    return a + b


concatenate("hello ", "world")

print("-" * 60)

md.greet("Kapil Dev")

