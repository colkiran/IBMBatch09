
import re

st = "b3t"
print(f"st :{st}")
print("-" * 60)

# character class
# between b and t - any one of the vowels
# res = re.search(r'b[aeiou]t', st)

# between b and t - it should not be a vowel
# res = re.search(r'b[^aeiou]t', st)

res = re.search(r'b[a-zA-Z0-9]t', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found.....")