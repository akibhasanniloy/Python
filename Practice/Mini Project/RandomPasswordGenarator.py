# import random
# import string

# pass_len=10
# charValues = string.digits + string.punctuation + string.ascii_letters

# password =""
# for i in range(pass_len):
#     password+= random.choice(charValues)

# print("Your Password is: ", password)

# using list
import random
import string

pass_len=10
charValues = string.digits + string.punctuation + string.ascii_letters

password= "".join([random.choice(charValues) for i in range(pass_len)])

print("Your Password is: ", password)