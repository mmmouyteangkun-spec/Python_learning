# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Dulplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicate
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# List
# fruits = ["apple", "orange", "banana", "coconut"]

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
#print("pineapple" in fruits)

# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear
# print(fruits.index("coconut "))
# print(fruits.count("pineapple"))

# print(fruits)
# for fruit in fruits:
   #print(fruit)

# Set
# fruits = {"apple", "orange", "banana", "coconut", "coconut"}
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear


# print(fruits)

# Tuple
fruits = ("apple", "orange", "banana", "coconut", "coconut")
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# print(fruits.index("apple"))
print(fruits.count("coconut"))

# print(fruits)
for fruit in fruits:
    print(fruit)