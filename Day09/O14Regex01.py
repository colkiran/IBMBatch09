
# beginning of the string and end of the string

import re

st = "hello world"
# res = re.match(r'^hello', st)
# r'' - raw string

# match will search only at the beginning of the string
res = re.search(r'world$', st)


if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found.....")