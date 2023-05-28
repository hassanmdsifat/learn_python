countries = ["Bangladesh", "India", "Germany", "Norway", "China"]
print(countries)
# using del statement

del countries[1]
# ['Bangladesh', 'Germany', 'Norway', 'China']
del countries[-1]
print(countries)

# using pop method

fruits = ["Banana", "Mango", "Apple", "Orange"]
print(fruits)
removed_item = fruits.pop()
print(removed_item)
print(fruits)
another_removed_item = fruits.pop(0)
print(fruits)

# using remove method
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

vowels.remove('i')
vowels.remove('z')
print(vowels)