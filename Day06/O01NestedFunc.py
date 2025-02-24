
def outerFun():
    gname = 'Sachin'
    def innerFun():

        print("Hello World....")
        print(f"Greeting Mr.{gname}")

    innerFun()

outerFun()
