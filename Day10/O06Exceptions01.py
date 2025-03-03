
try:
    n = int(input("Enter the number :"))
    d = int(input("Enter the divsor :"))

    res = n / d

except ZeroDivisionError as e:
    print("Exception caught ....")
    print(e.__class__)
    print(e)
except TypeError as t:
    print("Exception caught ....")
    print(t.__class__)
    print(t)
except Exception as e:
    print(e.__class__)
    print(e)
else:
    print(f"res :{res}")

finally:
    print("finally block.....")