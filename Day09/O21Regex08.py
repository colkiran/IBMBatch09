
import re

st = "best"
print(f"st :{st}")
print("-" * 60)

res = re.search(r'^b(oa|es)t$', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found.....")