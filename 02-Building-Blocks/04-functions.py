# Building Functions
#####################
print("Hello, world!")

len("Hello, world!")

str()
float()
abs(-11)
abs(-32342.24)
abs(5)

bin(1014)

round(3.14159)

sum([1, 2, 3])

max([-5, 100, 5000])

min([-5, 100, 5000])

for x in range(10): print(x)

sorted("abracadabra")       # ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'c', 'd', 'r', 'r']

reversed(sorted("abracadabra"))           # <list_reverseiterator object at 0x0000022C46E60AF0>
list(reversed(sorted("abracadabra")))     # ['r', 'r', 'd', 'c', 'b', 'b', 'a', 'a', 'a', 'a', 'a']

''.join(reversed(sorted("abracadabra")))  # 'rrdcbbaaaaa'

''.join(reversed(sorted(["Alice", "Bob", "Charlie", "Angel"])))     # 'CharlieBobAngelAlice'


# DON'T DO THIS NEVER
print = 5 + 8
print
print("Hello")  # TypeError: 'int' object is not callable
quit()


# ------------------------
'This is a long string'.split(" ")  # ['This', 'is', 'a', 'long', 'string']

a_string = "Apples, oranges, and bananas"
a_string.find('an')     # 10
a_string[10:]           # 'anges, and bananas'


"Hello, {0}, and welcome to {1}".format("Robin", "Python")  # 'Hello, Robin, and welcome to Python'
"There are " + str(5) + " items in your cart"   # 'There are 5 items in your cart'
"There are {0} items in your cart".format(5)    # 'There are 5 items in your cart'


a_list = 'This is a long string'.split(" ")
a_list          # ['This', 'is', 'a', 'long', 'string']
a_list.sort()
a_list          # ['This', 'a', 'is', 'long', 'string']
a_list.reverse()
a_list          # ['string', 'long', 'is', 'a', 'This']
a_list.remove('long')
a_list          # ['string', 'is', 'a', 'This']

# that's not really a copy
b_list = a_list
b_list          # ['string', 'is', 'a', 'This']
a_list          # ['string', 'is', 'a', 'This']

# if I say b_list.pop 
b_list.pop()    # 'This'
b_list          # ['string', 'is', 'a']

# I will get this out, and as you can see that modified a_list as well. 
# This is an important point, remember in Python when I do an assignment like this, I'm just pointing this name at data.
# What data am I pointing it at? Well, the same data that a_list points to
a_list          # ['string', 'is', 'a']

# If I want a copy of the list, instead of pointing at the same data, I should use copy. Now c_list is different from a a_list or b_list
c_list = a_list.copy()
c_list.append("Owls")
c_list      # ['string', 'is', 'a', 'Owls']
a_list      # ['string', 'is', 'a']
b_list      # ['string', 'is', 'a']


###########################
# Build your own functions
###########################
def greet(name):
    return "Hello, {0}".format(name)

greet("Angel")


def product(numbers):
    p = 1
    for n in numbers:
        p *= n
    return p

product([1, 2, 3, 4])


def combine_and_sort(first, second):
    return sorted((first + second))

combine_and_sort([1, 3, 5], [2, 4, 6])


def naughty_product(numbers):
    p = 1
    while numbers:
        p *= numbers.pop()
    return p

# it works apparently good
naughty_product([1, 2, 3, 4])

# but what happens if I create a list?
nums = [1, 2, 3, 4]
nums                    # [1, 2, 3, 4]
naughty_product(nums)   # 24

# what happened to nums?
nums       # []


# Remember "sorted" vs "sort"?
# Remember, sorted is making a copy of that list
[ 5, -3, 1, 11]
sorted([ 5, -3, 1, 11])

# If I copy this list
nums = [ 5, -3, 1, 11]

# It doesn't change nums, it's returning a new list with all the elements of nums sorted
sorted(nums)    # [-3, 1, 5, 11]
nums            # [5, -3, 1, 11]

# but if I call "sort" it's changed the list in place
nums.sort()
nums            # [-3, 1, 5, 11]









