my_list = []

for i in range(1, 101):
    my_list.append(i)

print(my_list)

'''
List comprehensions are lists that generate themselves with an internal for loop.

[thing for thing in list_of_things]
'''

another_list = [i for i in range(1, 101)]
print(another_list)