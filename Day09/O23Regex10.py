
import re

st = "sample.py"
print(f"st :{st}")
print("-" * 60)

# . matches a single character
# res = re.search(r'b.t', st)

# supress the meaning of . and search for .
res = re.search(r'\.py$', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found.....")