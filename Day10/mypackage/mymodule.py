
gname = "Sachin Tendulkar"

# --------------------------------------------------

sports =['cricket', 'hockey', 'football', 'badmiton', 'basketball', 'swimming']

# --------------------------------------------------
runs = {'test': 15800, 'odi': 19345, 't20': 1200}


# --------------------------------------------------
def greet(gst):
    print(f"Greeting {gst}, welcome to the event...")

# --------------------------------------------------
# class

class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name is {self.name}\nAge is {self.age}"


# --------------------------------------------------
# decorator
def outerFun(fnc):

    def innerFun(*args):
        print("logging into the service......")
        print(fnc(*args))
        print("logging out of the module")
        print("-" * 60)

    return innerFun




# --------------------------------------------------

if __name__  == '__main__':
    greet(gname)
    print("-" * 60)

    ply1 = Player('Rahul', 34)
    print(ply1)

    print(type(ply1))