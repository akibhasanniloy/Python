# def sum(a,b):
#     s=a+b;
#     return s
# print(sum(2,4))

# def mul(a,b=3):
#     s=a*b
#     print(s)
#     return s
# mul(2)

# Practice problem 1
city =["Dhaka","Rajshahi", "Hamburg","Berlin","Lippstadt"]
def len_list(list):
    print(len(list))
len_list(city)

# 2
def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(city)
print()

# 3
def prt_fact(n):
    s=1
    for i in range(1, n+1):
        s*=n
    print(s)
prt_fact(5)

# 4
def conversion(usd_val):
    bdt = usd_val * 110
    print(usd_val, "Usd Value =", bdt, "BDT")

conversion(1)

# 5
def odd_even(num):
    if(num%2==0):
        print("Even")
    else:
        print("odd")

odd_even(5)