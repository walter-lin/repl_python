#範例
# a = [ int(s) for s in input().split()]
# print(a[::-1] )
# print(' '.join( [str(s) for s in a[::-1] ] ) )

#9.2
# a = {int(s) for s in input().split()}
# b = {int(s) for s in input().split()}
# print(len(a & b) )

#9
# a = {int(s) for s in input().split()}
# b = {int(s) for s in input().split()}
# c = list(a | b)

#A1
# a = [str(s) for s in input().split()]
# b = {}
# for i in a:
#     if i in b:
#         b[i] += 1
#     else :
#         b[i] = 0
#     print(b[i],end =' ')
#A1 anser
# text = input().split()
# times_seen = {}
# for word in text:
#   if word not in times_seen:
#     times_seen[word] = 0
#   print(times_seen[word], end=' ')
#   times_seen[word] += 1

#A2
# word = {}
# for i in range(int(input())):
#     s = input().split()
#     word[s[0]] = s[1]
#     word[s[1]] = s[0]
# print(word[input()])