None

True

none
true

# How do you test your date with "None"? It depends. If all you care about is whether it is true or false
# If it doesn't matter if it's none, empty string, zero, etc... It turns out that "None"
# When used in a boolean context evaluats to false
my_data = ""
if my_data: 
    print("Got data?")

# It works exactly tha same way
my_data = False
if my_data: 
    print("Got data?")

my_data = None
if my_data: 
    print("Got data?")

# Any true value like "True" or "Yes" and it evaluate to true and we get the answer
my_data = True
if my_data: 
    print("Got data?")

my_data = "Yes"
if my_data: 
    print("Got data?")

# Remember, 
# each of the data types we have learned about so far has a "natural FALSE" value like "zero" or an "empty string"
# and ANY other value is considered "True"
# You can use them in an if statement in a way that is pretty intuitive. However, sometimes it does matter

#############
# Dictionary - looks like JSON [{key:value}] 
# BTW, other languages sometimes call this type of data "MAP" or "HashMap"
#############
cats = {}   # Dicts
a_list = []

cats["Robin"] = 5
cats["Adrian"] = 2
cats["Camila"] = 1
cats                # {'Robin': 5, 'Adrian': 2, 'Camila': 1}

# Reassigning is exactly tha same as adding
cats["Robin"] = 99
cats                # {'Robin': 99, 'Adrian': 2, 'Camila': 1}

# Remember though, that "Robin" isn't the same to Python as "robin" with a lower case 'r'
cats["robin"] = 2   
cats                # {'Robin': 99, 'Adrian': 2, 'Camila': 1, 'robin': 2}

#############################
# Two ways to get out values
#############################
# get single value
cats["Robin"]       # 99
cats["adrian"]      # KeyError: 'adrian' *** it doesn't exists

# with get()
cats.get("Bilbo Baggins")
cats.get("Robin")   # 99

# default value like output
print(cats.get("Bilgo Baggins"))    # None

# different defalut value if you want to change it
cats.get("Bilgo Baggins", 0)        # 0


# validate if exists some value, just check a keys not a values
"Robin" in cats     # True
"Angel" in cats     # False
cats                # {'Robin': 99, 'Adrian': 2, 'Camila': 1, 'robin': 2}

# Iterate it
for name in cats:
    print(name)
    # Robin
    # Adrian
    # Camila
    # robin

for name in cats:
    print("{0} has {1} cat(s)".format(name, cats[name]))
    # Robin has 99 cat(s)
    # Adrian has 2 cat(s)
    # Camila has 1 cat(s)
    # robin has 2 cat(s)

# Wen can also get the keys like this
for name in cats.keys():
    print("{0} has {1} cat(s)".format(name, cats[name]))


# and if you only want the values
for num_cats in cats.values():
    print(num_cats)
    # 99
    # 2
    # 1
    # 2


# Often, we want both the key and the value. We can iterate over each pair
for (person, num_cats) in cats.items():
    print(person)
    print(num_cats)
    # Robin
    # 99
    # Adrian
    # 2
    # Camila
    # 1
    # robin
    # 2

# Delete items
cats                # {'Robin': 99, 'Adrian': 2, 'Camila': 1, 'robin': 2, 'Bilbo': 5}
del cats["robin"]
cats                # {'Robin': 99, 'Adrian': 2, 'Camila': 1, 'Bilbo': 5}
cats.pop("Robin")
cats                # {'Adrian': 2, 'Camila': 1, 'Bilbo': 5}
cats.pop("Camila")
cats                # {'Adrian': 2, 'Bilbo': 5}

cats.pop("Robin")   # KeyError: 'Robin'
# Add default error
cats.pop("Robin", 0)   # 0


# ------------------
countries = { "AF": "Afghanistan", "AL": "Albania", "DZ": "Algeria"}
countries

for (code, country) in countries.items():
    print('<option value="{0}">{1}</option'.format(code, country))
    # <option value="AF">Afghanistan</option
    # <option value="AL">Albania</option
    # <option value="DZ">Algeria</option


# ------------------
thumbnail = None
cond = "Cloudy"

if cond == "Rainy": thumbnail = "rain.png"
if cond == "Cloudy": 
    thumbnail = "clouds.png" 
    print(thumbnail)

# instead of do that ^^^ we can use dicts like this
weather = {"Rainy": "rain.png", "Cloudy": "clouds.png"}
weather[cond]       # 'clouds.png'

# If we want to make the default be "None"
thumbnail = weather.get(cond)
thumbnail           # 'clouds.png'

# but if the condition doesn't exists in our dictionary "Thumbnail" becomes "None"
cond = "Stormy"
thumbnail = weather.get(cond)   # "Thumbnail" becomes "None"
thumbnail


# ------------------
# It's easy to create nested data structures out of them
#
users = { 1: { "name": "Joe", "email": "joe@mail.com"}, 2: {"name": "Sarah", "email": "sara@mail.com" } }
users
# {1: {'name': 'Joe', 'email': 'joe@mail.com'},
#  2: {'name': 'Sarah', 'email': 'sara@mail.com'}}

