def my_func():
    print("Hello World")


def print_function(func):
    func()
    print("This is from print function")


def greet(func):
    def inner():
        func()
        print("This is from inner function")
    return inner

@greet
def hello():
    print("This is from hello function")

print(hello())