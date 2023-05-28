class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return "My name is {}".format(self.name)


class Student(Person):

    def __init__(self, name, age, courses):
        self.courses = courses
        Person.__init__(self, name, age)


student_one = Student("Sifat", 26, ["C", "C++"])

print(student_one.introduce())