'''
for <var> in <iterable>:
    <statement(s)>

<iterable> is a collection of objects, for example, a list or tuple.
<statement(s)> in the loop body are denoted by indentation.
<var> takes on the value of the next element in <iterable> each time through the loop.
'''

my_list = ["apple", "banana", "orange", "mango"]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

print("----------")

for fruit in my_list:
    print(fruit)