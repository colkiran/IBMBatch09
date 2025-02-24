
# calculate the time taken by a function to execute

import time

def timeCalc(fnc):
    def helper(x):
        print("Executing the function.....")
        st = time.perf_counter()
        fnc(x)
        et = time.perf_counter()
        print("completed executing....")
        print(f"The total time taken is  :{round(et - st, 2)}")

    return helper

@timeCalc
def fun(n):
    lst = []
    for i in range(1, n):
        for j in range(1, i+1):
            lst.append(j ** 3)

fun(6500)