
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):

            from emojis import emojis

            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)

        return innerMostFun

    return innerFun

kangrt = outerFun("Namaskara")
kangrtTgr = kangrt("tiger")
kangrtTgr("Prabhakar")

"""
outerFun("Welcome")("---->")("Sachin")
print("-" * 60)

engGrt = outerFun("Welcome")
kanGrt = outerFun("Namaskara")

engGrtSngArw = engGrt("------>")
kanGrtDblArw = kanGrt("=====>>")


engGrtSngArw("Sachin")
engGrtSngArw("Virat")
kanGrtDblArw("Rahul")
"""