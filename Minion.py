# string='ANANAS'
# vowels=['a' , 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# user1="Stuart"
# user2='kevin'
# score=0
# user1Lis=[]
# user2Lis=[]
# def met(char):
#     if char in vowels:
#         user2Lis.append(char)
#     else :
#         user1Lis.append(char)
#
# for i in range(len(string)):
#     st = string[i]
#     met(st)
#     for j in range(i + 1, len(string)):
#         new=st + string[j]
#         if  new[0]  not in vowels:
#             user1Lis.append(new)
#             #print(user1Lis)
#         else:
#             user2Lis.append(new)
#         st=new
#     print(' ')
#
# print(user1Lis)
# print(len(user1Lis))
# print(user2Lis)
# print(len(user2Lis))

#The above solution is not vaiable for large strings

string='BANANA'
s = list(string)
len_s = len(s)
score_Stuart = 0
score_Kevin = 0
for a, b in enumerate(s):

    if b in ('U', 'E', 'O', 'A', 'I'):
        score_Kevin += len_s - a
    else:
        score_Stuart += len_s - a

if score_Stuart > score_Kevin:
    print("Stuart", score_Stuart)
elif score_Stuart < score_Kevin:

    print("Kevin", score_Kevin)
else:
    print("Draw")