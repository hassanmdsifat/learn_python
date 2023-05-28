class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return "My name is {}".format(self.name)



person_one = Person("Sifat Hassan", 26, "Male")
person_two = Person("User Two", 24, "Female")

print(person_one.introduce())
print(person_two.introduce())