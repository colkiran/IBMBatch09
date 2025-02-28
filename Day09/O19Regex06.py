
import re

st = "baaaaaaaaaaaaaaaaaaaaaaaaaat"
print(f"st :{st}")
print("-" * 60)

res = re.search(r'ba{3,}t', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found.....")