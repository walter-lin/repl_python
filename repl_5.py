#5.1
# s = input()
# print(s[2]) #1
# print(s[-2]) #2
# print(s[:5]) #3
# print(s[:-2]) #4
# print(s[0::2]) #5
# print(s[1::2]) #6
# print(s[::-1]) #7
# print(s[::-2]) #8
# print(len(s))

#5.2
# s = input()
# cout = 1
# for i in s:
#     if i == ' ':
#         cout += 1 
# print(cout)

# another_ans
# print(len(input().split()))

#5.3
# s = input()
# cont = int(len(s)/2)
# print(s[-cont:] , s[:(-cont)] , sep='' )

# another_ans
# s = input()
# mid = (len(s) + 1) // 2
# print(s[mid:] + s[:mid])

#5.4
# s = input().split()
# print(s[-1] , s[-2])

# another_ans
# word1, word2 = input().split()
# print(word2, word1)

#5.5
# s = input()
# f = -1
# l = ''
# for i in range(0,(len(s))):
#     if s[i] == 'f'and f == -1:
#         f = i
#     elif s[i] == 'f':
#         l = i
# print(f , l)

# another_ans
# s = input()
# if s.find('f') == s.rfind('f'):
#   print(s.find('f'))
# else:
#   print(s.find('f'), s.rfind('f'))

#5.6
# s = input().replace( 'p', '2',2 )
# if s.find('2') == -1:
#     print(-2)
# elif s.count('2') == 1:
#     print(-1)
# else:
#     print(s.rfind('2'))

# another_ans
# s= input()
# if s.find('p') == -1:
#     print(-2)
# elif s.find('p') == s.rfind('p'):
#     print(-1)
# else

#5.7
# s = input()
# a = s.find('h')
# b = s.rfind('h')
# for i in range(len(s)):
#     if a <= i <= b:
#         print('',end='')
#     else:
#         print(s[i],end='')

#another ans 
# s = input()
# print(s[:s.find('h')] + s[s.rfind('h') + 1:])

#5.8
# s = input()
# t = s[:s.find('h')]+s[s.rfind('h'):s.find('h'):-1]+s[s.rfind('h'):]
# print(t)

#5.9
# s = input()
# print(s.replace('1','one'))

#5.A
# print(input().replace('@',''))

#5.B
# s = input().replace('h','H')
# for i in range(len(s)):
#     if s.find('h') != i and s.rfind('h') != i:
#         print(s[i],end='')
#     else:
#         print('h',end='')

#5.B ans2
# s = input()
# print(s[:s.find('h')+1],s[s.find('h')+1:s.rfind('h')].replace('h','H'),s[s.rfind('h'):],sep='')

#5.C
s = input()
for i in range(len(s)):
    if i % 3 != 0:
        print(s[i],end='') 