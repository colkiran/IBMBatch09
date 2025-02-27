
FL = open("Employee.csv", "r")
FL.readline()

sal = 0
for line in FL.readlines():
    sal += int(line.split(",")[4])

print(f"Sum of all salries :{sal}")
FL.close()