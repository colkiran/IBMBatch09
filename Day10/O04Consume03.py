


import sys

# environment variable path - place the modules in any one of the locations
sys.path.append("C:\\Delhi")
print(sys.path)

import gurgaon.mymodule as md
from  gurgaon.mymodule import Player, outerFun

@outerFun
def concatenate(a, b):
    print(f"concatenating {a} and {b}")
    return a + b


concatenate("hello ", "world")
