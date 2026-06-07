# Parent Class
class Student:
    def show_name(self):
        print("Student Name: xyz")


# Single Inheritance
class Marks(Student):
    def show_marks(self):
        print("Marks: 85")


# Multilevel Inheritance
class Result(Marks):
    def show_result(self):
        print("Result: Distinction")


# Hierarchical Inheritance
class Sports(Student):
    def show_sport(self):
        print("Sport: Football")


# Hybrid Inheritance
class Attendance:
    def show_attendance(self):
        print("Attendance: 98%")


class AllDetails(Marks, Attendance):
    pass


print("Single Inheritance")
m = Marks()
m.show_name()
m.show_marks()

print()

print("Multilevel Inheritance")
r = Result()
r.show_name()
r.show_marks()
r.show_result()

print()

print("Hierarchical Inheritance")
s = Sports()
s.show_name()
s.show_sport()

print()

print("Hybrid Inheritance")
a = AllDetails()
a.show_name()
a.show_marks()
a.show_attendance()