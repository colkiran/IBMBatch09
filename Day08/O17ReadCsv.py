
import csv
from prettytable import PrettyTable

with open("Employee.csv", "r") as CSVR:
    emp_detials = csv.reader(CSVR)
    pretyTbl = PrettyTable(next(emp_detials))

    for row in emp_detials:
        pretyTbl.add_row(row)

print(pretyTbl)




"""    
    colnames = next(emp_detials)
    print(*colnames)

    for row in emp_detials:
        print(*row)
"""