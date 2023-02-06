numbers = [4, 5, 1, 2, 10, 100]
fruits = ["banana", "mango", "apple", "orange"]
# [1, 2, 4, 5, 10, 100]

# sort()

numbers.sort()
fruits.sort()
print(numbers)
print(fruits)

numbers.sort(reverse=True)
print(numbers)

# sorted()
another_numbers = [4, 3, 5, 10, 100]
sorted_numbers = sorted(another_numbers)
sorted_numbers_des = sorted(another_numbers, reverse=True)
print(another_numbers)
print(sorted_numbers)
print(sorted_numbers_des)