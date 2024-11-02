# delete keyword
# class student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
# s1=student("Akib", 200)
# print(s1.name, s1.mark)

# private
# class account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no= acc_no
#         self.__acc_pass=acc_pass
#     def reset_pass(self):
#         print(self.__acc_pass)
# c1= account(1234, 2132)
# print(c1.acc_no, c1.reset_pass())

# Inheritance
# Single inheritance
# class car:
#     color="Black"
#     @staticmethod
#     def start():
#         print("car is starting...")
#     @staticmethod
#     def stop():
#         print("car is stop...")

# class toyotaCar(car):
#     def __init__(self, name):
#         self.name=name

# c1= toyotaCar("Toyota")
# c2= toyotaCar("F1")
# # print(c1.name)
# c1.start()
# print(c1.color)

# multi level inheritance
# class car:
#     @staticmethod
#     def start():
#         print("car is starting...")
#     @staticmethod
#     def stop():
#         print("car is stop...")

# class toyotaCar(car):
#     def __init__(self, name):
#         self.name=name

# class f1(toyotaCar):
#     def __init__(self, brand):
#         self.brand=brand

# c1 =f1("Astro MArtin")
# c1.start()

# multiple inheritance
# class a:
#     varA="Welcome to class A"
# class b:
#     varB="Welcome to class B"
# class c(a,b):
#     varC="Welcome to Class C"
# c1=c()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# Super Method
class car:
    def __init__(self, type):
        self.type=type

    @staticmethod
    def start():
        print("car is starting...")

    @staticmethod
    def stop():
        print("car is stop...")

class toyotaCar(car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name=name
        super().start()
c1= toyotaCar("Plus","Manual")
print(c1.type)