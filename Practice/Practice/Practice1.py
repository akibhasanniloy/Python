print("This is just a practice session: ")
n=10
sum=1
for i in range(1,6):
    sum*=i
    print(sum)


# light=input()
light="green"
if(light=="red"):
    print("Stop")
elif(light =="yellow"):
    print("Stop Ahead")
elif(light=="green"):
    print("Go")
else:
    print("Go go")

age =18
if(age>=18):
    print("Adult")
elif(age<18):
    print("Picchi")
else:
    print("Boyos hoy nay.")


name = input("Enter a value: ")
age= int(input("Enter your age: "))
mark= float(input("Enter your mark: "))
print(type(name))
print(type(age))
print(type(mark))