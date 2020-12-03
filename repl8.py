#範例
# n = 3
# m = 4 
# a = [ [0] * m ] * n  
# a = [ [0] * m for i in range(n) ]

# a[1][0] = 5
# a[2][3] = 7
# for row in a : 
#     print(''.join([str(i) for i in row ]) )

# for row in a :
#     for i in row:
#         print(i,end=' ')
#     print()

#8.1
# m =[ int(i) for i in input().split()]
# a =[[ int(j) for j in input().split()] for i in range(m[0]) ]
# mul = int(input())
# a = [[j*mul for j in i]for i in a ]
# # for i in range(m[0]) :
# #     for j in range(m[1]):
# #         a[i][j] *= mul

# for row in a :
#     print(' '.join([str(i) for i in row ]))

#8.2
# m,n =[ int(i) for i in input().split()]
# a =[[ int(j) for j in input().split()] for i in range(int(m)) ]
# max = maxi = maxj = -1
# for i in range(m) :
#     for j in range(n):
#         if a[i][j] > max:
#             max = a[i][j]
#             maxi = i
#             maxj = j
# print(maxi,maxj)

#8.3
# n = int(input())
# a = [ [0] * n for i in range(n) ]

# for i in range(n):
#     for j in range(n):
#         a[i][j] = abs(i-j)

# for r in a:
#     print(''.join([str(i) for i in r]))

#8.3 函式寫法
# def print2DList(arr):
#     """
#     (註解寫這裡) 印出一個2DList
#     """
#     for r in arr:
#         print(' '.join([str(i) for i in r]))

# n = int(input())
# a = [ [0] * n for i in range(n) ]

# for i in range(n):
#     for j in range(n):
#         a[i][j] = abs(i-j)

# print2DList(a)