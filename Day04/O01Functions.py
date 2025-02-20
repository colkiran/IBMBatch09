
def greet():
    print("Greetings Mr. Sachin, Welcome to the event...")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event......")

# city is a default argument and gname is a non default argument
def greetGstCty(gname, y, city = "Mumbai", x=100):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event.....")

greet()

print("-" * 60)

greetGst("Rahul")
greetGst("Sachin")

print("-" * 60)

greetGstCty("Rohit", 10)
greetGstCty("Sachin", 20)
greetGstCty("Rahul", 10, "Bangalore", 500)

print("-" * 60)

# functions with simple args
def myProd(x, y):
    return x * y

print("%i * %i = %i" % (10, 20, myProd(10, 20)))

print("-" * 60)
# args vs keyword_args
def admsn(fname, lname, dob, gender, qlf, contno, mailid, city, adhrno):
    print(f"Name :{fname} {lname}")
    print(f"DOB  :{dob}")
    print(f"Gender :{gender}")
    print(f"Qualification :{qlf}")
    print(f"Contact No. :{contno}")
    print(f"Email ID :{mailid}")
    print(f"City :{city}")
    print(f"Adhar No. :{adhrno}")

# args
admsn('Jack', 'Slater', '10/03/1998', 'Male', 'Engineering Graduate', 90232302, 'jack@gmail.com', 'Real Madrid', 'ABE340502')

print("-" * 60)
# kwargs
admsn(gender='Female', contno=92934892, city="Barcelona", fname='Tina', qlf='Commerce Graduate', dob="19/08/2000", mailid='tina@gmail.com', lname='turner', adhrno='XJF232029')

print("-" * 60)
# variable length args

# *var can accept more than one value and store it in a tuple
def prodAll(*numbers):
    print(numbers)
    print(*numbers)         # unpack
    prod = 1
    for number in numbers:
        prod *= number
    return prod

res = prodAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)

def extractDetails(**details):
    print(details)
    for k,v in details.items():
        print(k, "=>", v)


extractDetails(name="Sachin", age=32, runs=45, oppnt="Aus")

print("-" * 60)

def basicArith(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = basicArith(20, 8)
print(f"res :{res}")

print("-" * 60)
# recursive calls

def fun(x):
    print(x)
    if x == 0:
        return x
    fun(x - 1)

fun(10)

print("-" * 60)
# use recursive calls
# 1. factorial of a number
# 2. fibonacci series

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")

print("-" * 60)
def fibo(x):
    if x == 1 or x == 0:
        return x
    else:
        return fibo(x - 1) + fibo(x - 2)

iter = int(input("Enter the number of fibanocci numbers to be generated :"))

for i in range(iter):
    print(fibo(i), end=" ")
print()


print("-" * 60)
# document strings - strings that are written on top of the function definition

def fun():
    "This is a doc string"
    # This is a comment
    print("Hello World")

fun()
print(fun.__doc__)          # prints the doc string

print("-" * 60)

def fun1(x, y):
    """
    fun1 takes two arguments x and y

    1. if x and y are integers then the function returns the sum of the numbers
    2. if x and y are strings then it returns the concatenated string
    3. if x and y are different data types then it returns and error
    """
    return x + y

print(fun1(10, 20))
print(fun1('hello ', 'world'))
# print(fun1(10, 'abc'))

print("-" * 60)
help(fun1)