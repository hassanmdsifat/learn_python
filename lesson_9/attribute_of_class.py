class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


person_one = Person("Sifat Hassan", 26, "Male")
person_two = Person("User A", 26, "Female")

print(person_one.name)
print(person_one.age)
print(person_one.gender)

print(person_two.name)
print(person_two.age)
print(person_two.gender)