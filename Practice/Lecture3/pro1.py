# array
marks=[12, 13, 14, 15, 16]
print(marks);
print(type(marks));
print(marks[1])
print(len(marks))

# Multiple type
student = ["Akib", 20, "University"]
print(student);
print(len(student));
print(student[2])
student[2]= "Hamburg"
print(student)

# Slicing
print(marks[1:4])
print(marks[1:])
print(marks[:4])
print(marks[ -3 : -1])

# List methods
list = [2,3,4,2]
# list.append(1)
# print(list);
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.sort(reverse=False)
# print(list)
# list.reverse();
# print(list);
# list.sort()
# list.insert(2, 10)
# print(list)
# list.remove(2)
# print(list)
list.pop(0)
print(list)

# Tuples
tup =(1,2,4,5,6)
print(tup)
print(tup[0])
print(tup[1])
print(tup[0:3])