#6.1
# n = int(input())
# a = 1
# while (a*a)<=n:
#     print(a*a)
#     a += 1

#6.2
# a = int(input())
# i = 2
# while a%i!=0 :
#     i += 1
# print(i)

#6.3
# x = int(input())
# n = 1
# while 2 ** n <= x:
#     n += 1 
# n -= 1 
# print(n,2 ** n )

#6.4
# x = int(input())
# y = int(input())
# i = 1
# while x < y:
#     i += 1
#     x *= 1.1
# print(i)

#6.5
# a = int(input())
# i = 1
# while a >0:
#     i += 1
#     a = int(input())
# print(i-1)

#6.6
# a = 1
# sum = 0
# while a>0:
#     a = int(input())
#     sum += a
# print(sum)

#6.7
# a = 1
# i = 0
# sum = 0
# while a != 0:
#     a = int(input())
#     sum += a
#     i += 1
# print(sum/(i-1))

#6.8
# a = int(input())
# max = 0
# while a != 0:
#     if a>max:
#         max = a
#     a = int(input())
# print(max)

#6.9
# a = int(input())
# max = 0
# i = 1
# Max_i = 1
# while a != 0:
#     if a>max:
#         max = a
#         Max_i = i
#     a = int(input())
#     i += 1
# print(Max_i)

#6A
# a = int(input())
# i = 1
# Max_i = 0
# while a != 0:
#     if a%2 == 0:
#         Max_i += 1
#     a = int(input())
#     i += 1
# print(Max_i)

#6B
# a = int(input())
# last_a = a
# Max_i = 0
# while a != 0:
#     if  a>last_a :
#         Max_i += 1
#     last_a =  a 
#     a = int(input())
# print(Max_i)

#6C 未完成
# a = int(input())
# sec = 0
# max = 0
# while a != 0:
#     if  a>max :
#         sec = max
#         max = a
#     a = int(input())
# print(sec)

#6F
# n = int(input())
# i = 3
# a = 1
# b = 1
# c = b + a  
# if n==1 or n== 2 : 
#     print(1)
# elif n == 3:
#     print(2)
# else:
#     while i < n:
#         i += 1
#         a = b 
#         b = c
#         c = a + b
#     print(c)

#6G 未完成
# x = int(input())
# if x == 1 :
#     print(1)
# elif x == 2:
#     print(3)
# else:
#     i = 3
#     a = 1
#     b = 1
#     c = a + b
#     while i < n:
#         i += 1
#         c = a + b
#         a = b 
#         b = c
#         if a+b==n:
#             print(i)
#         else:
#             print(-1)