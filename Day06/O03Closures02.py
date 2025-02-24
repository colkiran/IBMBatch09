
def outerFun(greet):

    # simple curry
    def innerFun(gname):

        print(greet, gname)

    return innerFun

outerFun("Welcome")("Sachin")

print("-" * 60)
engGrt = outerFun("Welcome")
kanGrt = outerFun("Namaskara")

engGrt("Virat")

kanGrt("Rahul")
kanGrt("Anil")
kanGrt("Srinath")