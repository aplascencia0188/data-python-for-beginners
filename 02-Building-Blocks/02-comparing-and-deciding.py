
# Comparing values

# Boolean
35
"strings"
[]
True
False
true # error

5 == 5
'a string' == "a string"
'A string' != 'a string'
3 < 5
137 > 20.5
3 >= 3.0
3 == 3.0
.1 + .1 + .1 == 3
.1 + .1 + .1 

# it is true because apple comes before to pineapple in the dicctionary
"apple" < "pineapple"
"manuel" < "angel"
"manuel" > "angel"


"apple" in "pineapple"  # True
"pile" in "pineapple"   # False

# only individual values
5 in [1, 2, 3, 4, 5]

[2, 3] in [1, 2, 3, 4, 5]

# argument of type 'int' is not iterable
37 in 1337


if "key" in "monkey": print("Oook!")
if "banana" in "monkey": print("Oook!")

##########
# a Block
##########
if "monk" in "monkey":
    print("Monkey! Spit than out!")
    print("...")
    print("Yuck! Don't eat the monk!")


name = "Angel"
if name < "Angel":
    print("Go to the head of the line!")
else:
    print("Hey, no cutting in line!")


name = "Angel"
if name < "Angel":
    print("Go to the head of the line!")
elif name == "Angel":
    print("Great name!")
else:
    print("Hey, no cutting in line!")


name = "Alice"
if name < "Angel":
    print("Go to the head of the line!")
elif name == "Angel":
    print("Great name!")
else:
    print("Hey, no cutting in line!")


# for strings an "empty" string is False
"" 

# Every other string is considered True, including Zero and False
'0'
'False'

# You might have guessed an empty list is considered False
[]

# Examples
name = ""
if name:
    print("Hello, " + name)
else:
    print("You forgot to enter a name, dummy!")


cart = []
if cart:
    print("Ready to check out?")
else:
    print("Start shopping!")


cart = [ "babanas" ]
if cart:
    print("Ready to check out?")
else:
    print("Start shopping!")


True and True
False or True
not True


