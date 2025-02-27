
FL = open("Data.txt", "r")

# reads the entire file and returns it like a string
# st = FL.read()
# print(st)

# reads the specified number of bytes from the file
# st = FL.read(852)
# print(st)

# reads one line from the file and stores it in the buffer
# st = FL.readline()
# print(st)

# it can read the data based on the no of bytes specified (line size)
# st = FL.readline(875)
# print(st)

# reads all the lines from the file and stores it like a string list
# st = FL.readlines()
# print(st)

# for line in FL.readlines():
#     print(line)

st = FL.readlines(950)
print(st)

FL.close()