# Nested loops mean loops inside a loop.
'''
Outer_loop Expression:
    Statement inside outer_loop
    Inner_loop Expression:
        Statement inside inner_loop
    Statement inside outer_loop
'''

for i in range(1, 11):
    for j in range(1, 11):
        print(i, "*", j, "=", i * j)
    print("-----------------------")