# for loop
# nums=[1,2,5,6]

# for val in nums:
#     print(val)

# problem:1
# n=[1,2,3,4,5,6,7,23]

# for i in n:
#     print(i)
# else:
#     print('End')

# problem: 2
# n=[1,2,3,4,5,3,6,7,23]
# m=3
# idx=0
# for i in n:
#     if(i==m):
#         print("index",idx)
#     # print(i)
#     idx+=1
# else:
#     print('End')

# for a in range(1,10, 2):
#     print(a)

# p.p1: 1-100 print

# for i in range(1,101):
#     print(i)

# p.p:2
# for a in range(1,11):
#     print(a*5)

# p.p:3
# for a in range(100,0,-1):
#     print(a)

# for a in range(5):
#     pass
# print("Useful work.")

# p.p:1
# n=1
# sum=0
# while n<=10:
#     sum+=n
#     print(sum)
#     n+=1

# p.p 2
n=5
fact=1
for a in range(1, n+1):
    fact*=a
    a+=1

print(fact)