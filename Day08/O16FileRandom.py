
FL = open("Data.txt", "rb")

pos = FL.seek(300, 0)
print(f"Position :{pos}")

pos = FL.seek(200, 1)
print(f"Position :{pos}")

pos = FL.seek(100, 2)
print(f"position {pos}")

FL.close()
