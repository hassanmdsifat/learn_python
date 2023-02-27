fruits = ("Mango", "Orange", "Banana") # 1, 2, 3

fruits = list(fruits)
fruits[1] = "Apple"
fruits.append(1)
fruits.append(2)
fruits.append(3)
fruits = tuple(fruits)
print(fruits)

fruits = list(fruits)
fruits.remove(1)
fruits = tuple(fruits)
print(fruits)