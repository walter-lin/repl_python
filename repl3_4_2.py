#3J
# a = int(input())
# if a%4 == 0  and a%100 == ! 0 or a%400 == 0 :
#     print('LEAP')
# else:
#     print('COMMON')     


#3K
# m = int(input())
# d = int(input())
# if m==2:
#     maxd = 28
# elif m in [4,6,9,11]:
#     maxd = 30
# else:
#     maxd = 31 
# if d+1>maxd:
#     m =  m%12+1
#     d = 1
# else:
#    d = d + 1
# print(m)
# print(d)

#3L
a = int(input())
b = int(input())
ans = b /a
if ans < 0:
    print("no solution")
else:
    print(ans)