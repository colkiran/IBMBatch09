
def outerFun():
    gname = "Sachin"                # local var
    def innerFun():

        nonlocal gname          # cannot convert a global var to non local
        gname += " Tendulkar"
        print('Hello World')
        print(gname)

    # outerFun Scope
    innerFun()
    print(f"after :{gname}")

outerFun()
