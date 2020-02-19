input()
Hello

name = input() # type some name
Angel
name

name = input("Enter your name: ")
Jorge
name

age_str = input("How old are you? ")
31

age = int(age_str)
age

type(age)
type(age_str)

age = int(input("How old are you? "))   # ValueError: invalid literal for int() with base 10: 'five'
five

# ---------
while True:
    num = input("Enter a number: ")
    if not num:
        break
    # Enter a number: 5
    # Enter a number: 10
    # Enter a number: 11
    # Enter a number: zero
    # Enter a number:       <--- Press Enter key

total = 0
while True:
    num = input("Enter a number: ")
    if not num: 
        break
    total += int(num)
    print("Total: " + str(total))
    # Enter a number: 5
    # Total: 5
    # Enter a number: 125
    # Total: 130
    # Enter a number: 37
    # Total: 167
    # Enter a number: 55
    # Total: 222
    # Enter a number: 11
    # Total: 233
    # Enter a number:       <-- the same problem when press Enter key or enter letter


"5".isdigit()
"125".isdigit()

num_inp = input("Enter a number: ")
31

num_inp

if not num_inp.isdigit():
    print("Fine, be that way...")
else:
    product = int(num_inp) * 7
    print("Did you know that seven times {0} is {1}".format(num_inp, product))

num_inp = "five" # Exec again with this value


int(" 5 ")
" 5 ".isdigit() # False
int(-55)
"-55".isdigit() # False


# ------------
try:
    inp = input("Enter a number:")
    inp_int = int(inp)
except:
    inp_int = None
    print("That's not a number I know about!")
# -55
fafa        # That's not a number I know about!

inp_int


# ----
try:
    inp = input("Enter a number: ")
    inp_int = int(inp)
except ValueError:
    inp_int = None
    print("That's not a number I know about!")
except NameError as e:
    print("Something went wrong with my code!")
    print(e)
    raise e
except: 
    print("I have no idea what went wrong...")
    raise
else: 
    print("Somehow, everything went according to plan...")
finally:
    print("All done!")

#####################################################
# Reading files
#####################################################
filePath = "E:\\ProgramData\\Git\\github\\data-python-for-beginners\\02-Building-Blocks\\"
with open(filePath + "recipe.txt") as input_file:
    recipe = input_file.read()

print(recipe)

# --------------
filePath = "E:\\ProgramData\\Git\\github\\data-python-for-beginners\\02-Building-Blocks\\"
with open("words.txt") as input_file:
    for line in input_file:
        line = line.strip()
        if line[0] == 'x':
            print(line)


filePath = "E:\\ProgramData\\Git\\github\\data-python-for-beginners\\02-Building-Blocks\\"
with open(filePath + "words.txt") as input_file:
    for line in input_file:
        line = line.strip()
        if len(line) < 4:
            continue
        if line[0] == 'x' and line[3] == 'y':
            print(line)


# writting file
words = ["xenyl", "xenylamine", "xylyl", "xylylene", "xylylic"]
words

with open('scrabble.txt', 'w') as output_file:
    for word in words:
        output_file.write(word + "\n")


# append
words = ["new line", "another line"]
with open('scrabble.txt', 'a') as output_file:
    for word in words:
        output_file.write(word + "\n")

