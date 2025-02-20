
from collections import namedtuple
def retMarks(p, m, c, b, l1, l2):
    # create a named tuple
    result = namedtuple("Result", 'phy mat che bio lan1 lan2')
    current_result = result(phy=p, mat=m, che=c, bio=b, lan1=l1, lan2=l2)
    return current_result

print(retMarks(89, 93, 85, 97, 70,  73))
res = retMarks(89, 93, 85, 97, 70,  73)

print(f"Physic      :{res.phy}")
print(f"Maths       :{res.mat}")
print(f"Chemistry   :{res.che}")
print(f"Biology     :{res.bio}")
print(f"language-1  :{res.lan1}")
print(f"language-2  :{res.lan2}")

