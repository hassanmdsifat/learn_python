number = [1, 2, 3, 4, 5]
number_two = [6, 7, 8, 9, 10]
number_third = [100, 200, 300]

merged_list = number + number_two + number_third
print(merged_list)

# using extend() method

fruits = ["Banana", "Apple", "Orange"]
fruits_two = ["Mango", "ABCD", "EFGH"]

fruits.extend(fruits_two)

print(fruits)