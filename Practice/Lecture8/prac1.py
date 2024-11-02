# class student:
#     name="Akib"

# s1 =student()
# print(s1.name)

# class cars:
#     color="BLue"
#     Brand1="BMW"
#     Brand2="Audi"
#     Pricing1=20000
#     pricing2=400000
#     Milage= "1000km"

# c1=cars()
# n1=c1.color
# n2= c1.Brand1
# n3=c1.Pricing1
# print(n1, n2, n3)

# c2=cars()
# a1= c2.color
# a2=c2.Brand2
# a3=c2.pricing2
# print(a1, a2, a3)

# class student:
#     # Default Constructor
#     def __init__(self):
#         pass
#     # parameterized Constructor
#     def __init__(self,name, marks):
#         self.name=name
#         self.marks= marks
#         print("adding a new student in database")

# s1 =student("Akib",87)
# print(s1.name, s1.marks)
# s2=student("Hasan", 21)
# print(s2.name, s2.marks)

# class akib:
#     def __init__(self):
#         pass
#     def __init__(self, age, profession):
#         self.age= age
#         self.profession= profession
#         print("Something Something fishy...")

# a1 = akib(21, "Developer")
# a2 = akib(25, "Software Engineer")
# print(a1.age, a1.profession)
# print(a2.age, a2.profession)

# class resume:
#     def __init__(info, name, age,profession,skill):
#         info.name= name
#         info.age= age
#         info.profession= profession
#         info.skill=skill

# c1= resume("Akib",21,"Software Developer", "C++, python, js so on")
# c2= resume("Hasan",25,"Software Developer", "C++, python, js so on")
# c3= resume("Akib",26,"Software Developer", "C++, python, js so on")
# print(c1.name, c1.age, c1.profession, c1.skill)
# print(c2.name, c2.age, c2.profession, c2.skill)
# print(c3.name, c3.age, c3.profession, c3.skill)

# class student:
#     # Default Constructor
#     def __init__(self):
#         pass
#     # parameterized Constructor
#     def __init__(self,name, marks):
#         self.name=name
#         self.marks= marks
#         print("adding a new student in database")
#     def welcome(self):
#         print("Welcome Student", self.name)
#     def get_mark(self):
#         return self.marks

# s1 =student("Akib",87)
# print(s1.name, s1.marks)
# s2=student("Hasan", 21)
# print(s2.name, s2.marks)
# s1.welcome()
# print(s2.get_mark())

# practice problem 1:
class student:
    def __init__(self,name, mark):
        self.name= name
        self.mark=mark
    # Static Method
    @staticmethod
    def hello():
        print("Hello Hello")
    def avg_mark(self):
        sum=0
        for val in self.mark:
            sum += val
        print("hi",self.name,"your av mark is", sum/3)
s1=student("Physics", [90, 94, 88])
s1.avg_mark()
s1.hello()