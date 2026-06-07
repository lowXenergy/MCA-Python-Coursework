# Parent Class
class Student:
    def show_name(self):
        print("Student Name: Rahul")


# Single Inheritance
class Marks(Student):
    def show_marks(self):
        print("Marks: 90")


# Multilevel Inheritance
class Result(Marks):
    def show_result(self):
        print("Result: Pass")


# Hierarchical Inheritance
class Sports(Student):
    def show_sport(self):
        print("Sport: Cricket")


# Hybrid Inheritance
class Attendance:
    def show_attendance(self):
        print("Attendance: 95%")


class AllDetails(Marks, Attendance):
    pass


# -----------------------------
# Single Inheritance Example
# -----------------------------
print("Single Inheritance")

m = Marks()
m.show_name()     # From Student class
m.show_marks()    # From Marks class

print()


# -----------------------------
# Multilevel Inheritance Example
# -----------------------------
print("Multilevel Inheritance")

r = Result()
r.show_name()      # From Student class
r.show_marks()     # From Marks class
r.show_result()    # From Result class

print()


# -----------------------------
# Hierarchical Inheritance Example
# -----------------------------
print("Hierarchical Inheritance")

s = Sports()
s.show_name()      # From Student class
s.show_sport()     # From Sports class

print()


# -----------------------------
# Hybrid Inheritance Example
# -----------------------------
print("Hybrid Inheritance")

a = AllDetails()
a.show_name()         # From Student class
a.show_marks()        # From Marks class
a.show_attendance()   # From Attendance class