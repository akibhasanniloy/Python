# list = [1,2,1]
list = ["a", "b", "c", "d", "e"]

copy_list= list.copy()
copy_list.reverse()

if(list==copy_list):
    print("Palindrome")
else:
    print("Not Palindrome")