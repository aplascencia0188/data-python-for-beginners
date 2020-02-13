colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
colors[1]       # 'Orange'
colors[1:4]     # ['Orange', 'Yellow', 'Green']
colors[4]       # 'Blue'
colors[::2]     # ['Red', 'Yellow', 'Blue']
# Add new in an especific possition
colors[1] = "Black"
colors          # ['Red', 'Black', 'Yellow', 'Green', 'Blue', 'Purple']
colors[2:] = ["Black"] * 4
colors          # ['Red', 'Black', 'Black', 'Black', 'Black', 'Black']


sentence = "The quick brown fox jumped over the lazy dog."
sentence[0]     # 'T'
sentence[4]     # 'q'
sentence[-1]    # '.'
sentence[-5]    # ' '
sentence[4:9]   # 'quick'
sentence[4:]    # 'quick brown fox jumped over the lazy dog.'
sentence[::2]   # 'Teqikbonfxjme vrtelz o.'
sentence[4:-1:2] # 'qikbonfxjme vrtelz o'

# we cannot to modified a string
sentence[16:19] = "cat" # TypeError: 'str' object does not support item assignment
sentence[0:16] + "cat" + sentence[19:]  # 'The quick brown cat jumped over the lazy dog.'

########
# SPLIT
########
sentence.split(' ')         # ['The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog.']
"32:56:99".split(":")       # ['32', '56', '99']
sentence.split("he")        # ['T', ' quick brown fox jumped over t', ' lazy dog.']



colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
colors
# Splining inverse
" - ".join(colors)                  # 'Red - Orange - Yellow - Green - Blue - Purple'
" - ".join(colors).split(" - ")     # ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']

########
# LOOPS
########
# For 

for color in colors: print("Is " + color + " your favorite?")
    # Is Red your favorite?
    # Is Orange your favorite?
    # Is Yellow your favorite?
    # Is Green your favorite?
    # Is Blue your favorite?
    # Is Purple your favorite?

for number in [ 1, 2, 3, 4, 5]:
    double = number * 2
    print("Twice " + str(number) + " is " + str(double))
    # Twice 1 is 2
    # Twice 2 is 4
    # Twice 3 is 6
    # Twice 4 is 8
    # Twice 5 is 10

# -----------------------------------------------------------------
colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']
modifiers = ["Dark", "Light", "Brownish"]

for c in colors:
    for m in modifiers:
        print(m + " " + c)
    # Dark Red
    # Light Red
    # Brownish Red
    # Dark Orange
    # Light Orange
    # Brownish Orange
    # Dark Yellow
    # Light Yellow
    # Brownish Yellow
    # Dark Green
    # Light Green
    # Brownish Green
    # Dark Blue
    # Light Blue
    # Brownish Blue
    # Dark Purple
    # Light Purple
    # Brownish Purple

# -----------------------------------------------------------------
for v in "aeiou":
    print("My favorite vowel is " + v)
    # My favorite vowel is a
    # My favorite vowel is e
    # My favorite vowel is i
    # My favorite vowel is o
    # My favorite vowel is u

# -----------------------------------------------------------------
# While
coundDown = 10
while coundDown >= 0:
    print(str(coundDown))
    coundDown -= 1
    # 10
    # 9
    # 8
    # 7
    # 6
    # 5
    # 4
    # 3
    # 2
    # 1
    # 0

# -----------------------------------------------------------------
# infinitive loop
coundDown = 10
while coundDown >= 0:
    print(str(coundDown))
    coundDown = 1 # error 


# Remove the last element
names = ["Daniel", "James", "Peter", "Sean"]
names.pop()     # 'Sean'
names           # ['Daniel', 'James', 'Peter']
names.pop()     # 'Peter'
names.pop()     # 'James'
names.pop()     # 'Daniel'
names.pop()     # IndexError: pop from empty list

names = ["Daniel", "James", "Peter", "Sean"]
while names:
    print("Welcome, Mr. " + names.pop())
    # Welcome, Mr. Sean
    # Welcome, Mr. Peter
    # Welcome, Mr. James
    # Welcome, Mr. Daniel

# after loop, the variable is empty
names   # []


# Add element
names.append("Larry")
names                   # ['Larry']
names.append("Moe")
names.append("Curly")
names.append("Angel")
names                   # ['Larry', 'Moe', 'Curly', 'Angel']






