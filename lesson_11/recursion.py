def my_func(n):
    if n > 10:
        return
    my_func(n + 1)
    print(n)

my_func(1)