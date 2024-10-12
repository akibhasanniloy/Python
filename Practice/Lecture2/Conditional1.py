age = 21
if(age > 30):
    {
        print("Mature")
    }
elif(age < 30 and age > 18):
    {
        print("Adult")
    }
else:
    {
        print("Child")
    }  

# Grade
# marks = int(input("Enter your grade: "));
marks =85
if(marks >= 90):
    grade= "A"
elif(marks <90 and marks >= 80):
    grade= "B"
elif(marks<80 and marks >=70):
    grade= "C"
elif(marks<70):
    grade= "D"

print("Grade of the student =>", grade);

# Nesting
age1 =20
if(age1>= 18):
    if(age1>=80):
        print("Cann't drive")
    else:
        print("Can Drive")
else:
    print("Cann't drive")


# Practice 1
num =10
if(num % 2 == 0):
    print("Even")
else:
    print("Odd")

# Practice 2
a=2
b=5
c=1
if(a>b and a>c):
    print("a")
elif(b>a and b>c):
    print("b")
elif(c>b and a<c):
    print("a")

# Practice 3
mul =70
if(mul % 7 == 0):
    print("Yes")
else:
    print("No")