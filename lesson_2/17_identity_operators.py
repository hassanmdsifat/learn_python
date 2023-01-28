number_one = 2
number_two = 2

print(id(number_one))
print(id(number_two))

print(number_two is number_one)

my_list = []
my_list_two = []

print(id(my_list))
print(id(my_list_two))

print(my_list == my_list_two)
print(my_list is not my_list_two)