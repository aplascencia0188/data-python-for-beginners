####################################################
# Beyond the Basics I: Iterables and Advanced Loops
####################################################

# Python has two types to handle binary data. 
# First there's bytes. Bytes work a lot like string, there an immutable sequence of bytes, which is basically what strings are.
# The main difference is that the data in a string is always interpreted as text while the data in bytes can be anything

b = bytes()
b           # b''

greeting = b"Hello, World!"

# Python helpfully interprets it as letters
print(greeting)    # b'Hello, World!'

# but if we iterate over it, we can see the data inside of it. You can see the numerical value that represents each character
for c in greeting:
    print(c)
    # 72
    # 101
    # 108
    # 108
    # 111
    # 44
    # 32
    # 87
    # 111
    # 114
    # 108
    # 100
    # 33

# Like string you cannot modify bytes
greeting[0] = 80        # TypeError: 'bytes' object does not support item assignment

# if we have binary data we need to modify, we use byte arrays.
# Byte arrays are a little more like lists, still binary data but yo can modify and append to them
data = bytearray()
print(data)         # bytearray(b'')

data += b"Hi, how are you?"
data                # bytearray(b'Hi, how are you?')
data[0] = 120
print(data)         # bytearray(b'xi, how are you?')

# Usually you would use bytes or byte arrays for something like an image or a video


# --------------------------------------------------------------
# The next 3 types of data are all basically variants of a list.
# -------------------------------------------------------------- 
########
# Tuple
########
fruits = ("Apple", "Orange", "Lemon", "Tomato")
fruits[0]       # 'Apple'

for f in fruits:
    print("Would you like a nice {0}?".format(f))
    # Would you like a nice Apple?
    # Would you like a nice Orange?
    # Would you like a nice Lemon?
    # Would you like a nice Tomato?

# The big difference is, you can't modify a tuple
fruits.append("Strawberry")     # AttributeError: 'tuple' object has no attribute 'append'
fruits[2] = "Strawberry"        # TypeError: 'tuple' object does not support item assignment

# However it's easy to switch back and forth between a tuple and a list
list(fruits)            # ['Apple', 'Orange', 'Lemon', 'Tomato']
tuple(list(fruits))     # ('Apple', 'Orange', 'Lemon', 'Tomato')

# So, when do you use a tuple instead of a list? Performance 
red = (255, 0, 0)
purple = (255, 0, 255)

grades = ( [95, 90], [50, 90])
grades[1]                   # [50, 90]
grades[1] = [100, 100]      # TypeError: 'tuple' object does not support item assignment

# You can go inside the list and change the elements. 
# The list itself is mutable
grades[1][0] = 100
grades                      # ([95, 90], [100, 90])

# So don't think of a tuple as a way to create a constant data structure, it's only the tuple itselt that is immutable not the things inside of it


########
# Sets
########
# A set is basically just what you'd expect from math class. It's an unordered collection of unique items.
# A list that is both unique and in no particular order

vegetables = {"Asparagus", "Onion", "Carrot", "Tomato"}
vegetables[0] # TypeError: 'set' object is not subscriptable | not support indexing

# You just need to remember that you won't get them out in any particular order
for v in vegetables:
    print(v)

# we can also add or remove sets
vegetables.pop()
vegetables          # {'Onion', 'Carrot', 'Tomato'}
vegetables.remove('Onion')
vegetables          # {'Carrot', 'Tomato'}
vegetables.add("Radish")
vegetables          # {'Radish', 'Tomato', 'Carrot'}

# Remember, the elements of a set are unique
vegetables.add("Radish") 
vegetables          # {'Radish', 'Tomato', 'Carrot'} *** it's still only in the set a single time


# The signature feature of sets is that you can do set operation with them, like from math class
vegetables.intersection(fruits)     # {'Tomato'}
fruits          # ('Apple', 'Orange', 'Lemon', 'Tomato')
vegetables      # {'Asparagus', 'Onion', 'Carrot', 'Tomato'}

set(fruits)                     # {'Tomato', 'Orange', 'Lemon', 'Apple'}
list(set(tuple(vegetables)))    # ['Asparagus', 'Onion', 'Carrot', 'Tomato']

# One other limitations of sets. Unlike lists, the values of a set can't be just anything. Values of a set have the same limitations as dictionary keys.
# So, you can't put lists, dictionaries or other sets inside of a set


########
# Frozen Sets
########
# A Frozen set is just a set you can't modify
frozen = frozenset(vegetables)

frozen.pop()    # AttributeError: 'frozenset' object has no attribute 'pop'


##################
# Advanced Loops
##################
for l in "A string":
    print(l)
    # A

    # s
    # t
    # r
    # i
    # n
    # g

for i in ["a", "list", "of", "String"]:
    print(i)
    # a
    # list
    # of
    # String

for k in { "this": 4, "is": 2, "a": 1, "dict": 4}:
    print(k)
    # this
    # is
    # a
    # dict


colors = { "Red": (255, 0, 0), "Yellow": (255, 255, 0), "Purple": (255, 0, 255)}
for (name, rgb) in colors.items():
    print(name, rgb)
    # Red (255, 0, 0)
    # Yellow (255, 255, 0)
    # Purple (255, 0, 255)

fruits      # ('Apple', 'Orange', 'Lemon', 'Tomato')
for (i, c) in enumerate(fruits):
    print(i, c)
    # 0 Apple
    # 1 Orange
    # 2 Lemon
    # 3 Tomato

# You can also iterate over two iterables at once
fruits          # ('Apple', 'Orange', 'Lemon', 'Tomato')
vegetables      # {'Asparagus', 'Onion', 'Carrot', 'Tomato'}

# zip will essentially pair up items from the two iterables and wil stop when either iterable runs out
for (f, v) in zip(fruits, vegetables):
    print(f, v)
    # Apple Asparagus
    # Orange Onion
    # Lemon Carrot
    # Tomato Tomato

vegetables.add("Rhubarb") # Repeat loop again
    # Apple Tomato
    # Orange Asparagus
    # Lemon Rhubarb
    # Tomato Onion


# --------------------------------------------
haystack = [ "hey" ] * 20
haystack[6] = "needle"
haystack

idx = None
for (i, v) in enumerate(haystack):
    print("Looking...")
    if v == "needle":
        idx = i
        print("FOUND IT!!")

haystack[idx]
idx

# use break to stop it
for (i, v) in enumerate(haystack):
    print("Looking...")
    if v == "needle":
        idx = i
        print("FOUND IT!!")
        break


for (i, v) in enumerate(haystack):
    print("Looking...")
    if v == "hey":
        continue
    idx = i
    print("FOUND IT!!")
    break

# using else
haystack = [ "hey" ] * 20

for (i, v) in enumerate(haystack):
    print("Looking...")
    if v == "hey":
        continue
    idx = i
    print("FOUND IT!!")
    break
else:
    print("Couldn't find it... :(")


# --------------------------------------------

for i in range(1, 21):
    print(i)


powers = []
for i in range(1, 21):
    powers.append(2 ** i)

powers      # [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]

powers = [ 2 ** i for i in range(1, 21) ]
powers      # [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]






















