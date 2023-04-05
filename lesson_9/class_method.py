class Student:
    school_name = "Test School"

    def __init__(self, name, course):
        self.name = name
        self.course = course

    @classmethod
    def get_school_name(cls):
        return cls.school_name


student_one = Student("S1", "C1")
student_two = Student("S2", "C2")


print(Student.get_school_name())

