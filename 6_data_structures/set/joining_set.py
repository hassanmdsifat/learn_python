set1 = {1, 3, 5, 7, 9}
set2 = {1, 2, 4, 6, 8, 10}

# .union()
set3 = set1.union(set2)

print(set1)
print(set2)
print(set3)

# .update()

set1.update(set2)
print(set1)