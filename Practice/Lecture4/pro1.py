info ={
    "key": "value",
    "name": "akib",
    "Learning": "Python",
    "Subjects": ["Python", "C", "C++", "Java", "Javascript"],
    "Tuples": ("Dict", "Set"),
    "Time": 3,
    "is_Adult": True,
    12: 1.56
}
print(info)
print(info["name"])
info["name"]="Hasan"
info["Surname"]="Niloy"
print(info["name"])
print(info)

null_info={}
null_info["name"]="Akib"
print(null_info)

student ={
    "key": "value",
    "name": "akib",
    "Learning": "Python",
    "Subjects": {
      "phy": 54,  
      "Math": 54,  
      "che": 54  
    },
    "Tuples": ("Dict", "Set"),
    "Time": 3,
    "is_Adult": True,
    12: 1.56
}
print(student)
print(student.keys())
print(list(student.keys()))
print(student.values())
print(list(student.items()))