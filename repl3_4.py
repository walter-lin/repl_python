# #3.1
# a = int(input())
# if a%2 == 1 :
#     print('odd')
# else: 
#     print('even')

#3.2
# a = int(input())
# b = int(input())
# if a>b:
#     print(b)
# else:
#     print(a)

# #3.2
# x = int(input())
# if x>0:
#     print(1)
# elif x<0:
#     print(-1)
# else:
#     print(0)

#3.3
# x = int(input())
# if x//100 > 0 and x //1000 == 0 :
#     print('YES')
# else :
#     print('NO')

#3.5
# a = int(input())
# b = int(input())
# if a*b<0:
#     print('YES')
# else:
#     print('NO')

#3.6
# a,b,c = input()
# if int(a)<int(b)<int(c):
#     print('YES')
# else:
#     print('NO')

#3.8
# a = int(input())
# if a==2:
#     print('28')
# elif a in [4,6,9,11]:
#     print('30')
# else:
#     print('31')

#3A
# a = int(input())
# b = int(input())
# c = int(input())
# if a == b ==c:
#     print(3)
# elif a!= b and a!=c and b!=c:
#     print(0)
# else :
#     print(2) 

#3B
# a = int(input())
# b = int(input())
# c = int(input())
# if a == b:
#     print(c)
# elif a == c:
#     print(b)
# else:
#     print(a)


# 3C
# x1 = int(input())
# x2 = int(input())
# y1 = int(input())
# y2 = int(input())
# if x1 == y1 or x2 == y2:
#     print('YES')
# else :
#     print('NO')

#3D
# a = int(input())
# b = int(input())
# if (a+b)%2 == 0:
#     print('YES')
# else:
#     print('NO')

#3E
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if (x1+y1+x2+y2)%2 == 0:
#     print('YES')
# else:
#     print('NO')

#3F
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x1-x2) <= 1 and abs(y1-y2) <= 1:
#     print('YES')
# else:
#     print("NO")

#3G
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if  abs(x1-x2) == abs(y1-y2):
#     print('YES')
# else:
#     print('NO')

#3H
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if  abs(x1-x2) == abs(y1-y2) or x1 == x2 or y1 == y2 :
#     print('YES')
# else:
#     print('NO')

#3I
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x1-x2)*abs(y1-y2) == 2:
#     print('YES')
# else:
#     print('NO')

#3J
# a = int(input())
# if a%4 == 0 and a%100 != 0 or a%400 == 0:
#     print('LEAP')
# else:
#     print('COMMON')

#3k
# m = int(input())
# d = int(input())
# if m==2:
#     maxd = 28
# elif m in [4,6,9,11]:
#     maxd = 30
# else:
#     maxd = 31 
# if d+1>maxd and (m+1) > 12:
#     d = 1  
#     m = 1
# elif  d+1>maxd:
#     d = 1
#     m = m + 1
# else:
#    d = d + 1
# print(m)
# print(d)

#3L
# a = int(input())
# b = int(input())
# if a == 0 and b == 0:
#     print('many solutions')
# elif a == 0 or b%a != 0:
#     print("no solution")
# else:
#     print(int(b/a))

#3M
# x1 = int(input())
# x2 = int(input())
# x3 = int(input())
# x4 = int(input())
# x5 = int(input())

# if x1<x2 and x1 < x3 and x1 <x4 and  x1 <x5:
#     print(x1)
# elif x2 <x3 and x2 < x4 and x2 < x5:
#     print(x2)
# elif x3 < x4 and x4 < x5:
#     print(x3)
# elif x4 < x5 :
#     print(x4)
# else:
#     print(x5)
# 3N
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# x3 = int(input())
# y3 = int(input())

# if x1 == x2 :
#     print(x3)
#     if y1 == y3:
#         print(y2)
#     else:
#         print(y1)
# elif x1 == x3:
#     print(x2)
#     if y1 == y2:
#         print(y3)
#     else:
#         print(y1)
# else:
#     print(x1)
#     if y1 == y2:
#         print(y3)
#     else:
#         print(y2)

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# x3 = int(input())
# y3 = int(input())

# if x1 == x2:
#   x4 = x3
# elif x1 == x3:
#   x4 = x2
# else:
#   x4 = x1
# if y1 == y2:
#   y4 = y3
# elif y1 == y3:
#   y4 = y2
# else:
#   y4 = y1

#3O
# x1 = int(input())
# x2 = int(input())
# x3 = int(input())

# if x1 < x2 and x1 < x3:
#     min = x1
#     if x2 < x3:
#         mid = x2
#         max = x3
#     else:
#         mid = x3
#         max = x2
# elif x2 < x3 :
#     min = x2
#     if x1 < x3 :
#         mid = x1
#         max = x3
#     else:
#         mid = x3
#         max = x1
# else:
#     min = x3
#     if x1 <x2:
#         mid = x1
#         max = x2
#     else:
#         mid = x2
#         max = x1
# print(min,mid,max,sep='\n') 

#另一種寫法
# a = int(input())
# b = int(input())
# c = int(input())

# if a <= b <= c:
#   print(a, b, c, sep='\n')
# elif a <= c <= b:
#   print(a, c, b, sep='\n')
# elif b <= a <= c:
#   print(b, a, c, sep='\n')
# elif b <= c <= a:
#   print(b, c, a, sep='\n')
# elif c <= a <= b:
#   print(c, a, b, sep='\n')
# else:
#   print(c, b, a, sep='\n')
