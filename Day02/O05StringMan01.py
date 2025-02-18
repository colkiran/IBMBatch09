
st = "hello world"
print(f'st :{st}')
print(type(st))

print("-" * 60)
print(f"st :{st}")
# strings can be indexed
print(f"st[0] :{st[0]}")
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

print("-" * 60)
# slicing
print(f"st[0:5]    :{st[0:5]}")
print(f"st[6:11]   :{st[6:11]}")
print(f"st[0:11]   :{st[0:11]}")
print(f"st[0:11:2] :{st[0:11:2]}")
print(f"st[0:]     :{st[0:]}")
print(f"st[:11]    :{st[:11]}")
print(f"st[:]      :{st[:]}")

print("-" * 60)
# reverse indexing
print(f"st[-1]  :{st[-1]}")
print(f"st[-5]  :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print("-" * 60)
# slicing using reversing indexing
print(f"st[-1:-6:-1]   :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1]  :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1]  :{st[-1:-12:-1]}")
print(f"st[-1::-1]     :{st[-1::-1]}")
print(f"st[:-12:-1]    :{st[:-12:-1]}")
print(f"st[::-1]       :{st[::-1]}")

print("-" * 60)
# Write a code to find if it is a palindrome
st = "malaYalaM"
print("Palindrome" if st[:].lower() == st[::-1].lower() else "Not a Palindrome")

print("-" * 60)
# st = "hello world"
# print(f"st :{st}")
#
# st[0] = "H"

# st is an object of str class
# print(dir(st))

# capitalize
st = "hello world"
print(f"st :{st}")
print(f"st.capitalize :{st.capitalize()}")

print("-" * 60)
# upper
print(f"st :{st}")
print(f"st.upper() :{st.upper()}")

print("-" * 60)
# strip, lstrip, rstrip
st = "******hello**********"
print(f"st :{st}")

# rstrip
print(f"st.rstrip('*')  :{st.rstrip('*')}")

# lstrip
print(f"st.lstrip('*') :{st.lstrip('*')}")

# strip
print(f"st.strip('*') :{st.strip('*')}")