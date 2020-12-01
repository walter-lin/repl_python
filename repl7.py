#test
# a=[int(s)*2 for s in input().split()]
# print(a)

# a = [int(s) for s in input().split()]
# for i in range(len(a)):
#     print(a[i])

#7.1
# a = [int(s) for s in input().split()]
# for i in range(len(a)):
#     if i%2 == 0 :
#         print(a[i], end=' ')

#7.2
# a = [int(t) for t in input().split()]
# for t in a :
#     if t%2 == 0 :
#         print(t)

#7.3
# a = [ int(s) for s in input().split()]
# for i in range(1,len(a)):
#     if a[i-1]<a[i]:
#         print(a[i])

#7.4
# a = [ int(s) for s in input().split()]
# #-1 2 3 -1 -2
# for i in range(0,len(a)-1):
#     if a[i]*a[i+1]>0:
#         print(a[i],a[i+1])
#         break
#     if i == len(a)-2:
#         print(0)

#7.5
# a = [ int(s) for s in input().split()]
# cont = 0
# for i in range(1,len(a)-1):
#     if a[i]>a[i-1] and a[i]>a[i+1]:
#         cont += 1
# print(cont)

#7.6
# a = [ int(s) for s in input().split()]
# cont = 1
# for i in range(0,len(a)-1):
#     if a[i] != a[i+1]:
#         cont += 1
# print(cont)

#7.7 未完成
# a = input().split()
# disk = []
# for i in range(0,len(a),2):
#     disk = a[i]
#     for j in range(0,len(a),1):
#         a[i]

#7.A
# a = [ int(s) for s in input().split()]
# cont = 0
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if a[i] == a[j]:
#             cont += 1
# print(cont)

