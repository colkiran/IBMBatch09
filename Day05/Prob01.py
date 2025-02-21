
# use sort and sort it according to the calendar months

months = ['dec', 'aug', 'oct', 'jul', 'nov', 'apr', 'sep', 'jan', 'may', 'jun', 'feb', 'mar']

print(f"unsorted months :\n{months}")

print("-" * 60)
from calendar import month_abbr
print(f"month_abbr :\n{list(month_abbr)}")

print("-" * 60)
res = sorted(months, key=list(map(lambda x: x.lower(), list(month_abbr))).index)
print(f"Sorted months :\n{res}")


