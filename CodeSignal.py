#___________________________________________
################ CodeSignal_1 ##############

# def add(param1, param2):
#     return (param1 + param2)
#
# a = 1
# b = 2
# add(a, b)

#___________________________________________
################ CpodeSignal_2 #############

# import math
#
# def centuryFromYear(year):
#     century = math.ceil(year / 100)
#     return century
# t = 1920
# print(centuryFromYear(t))

#___________________________________________
################ CodeSignal_3 ##############

# def checkPalindrome(inputString):
#     revString = ''.join(reversed(inputString))
#     if revString == inputString:
#         return True
#     else:
#         return False
# s = "aba"

#__________________________________________
################ CodeSignal_4 ##############

# def adjacentElementsProduct(list_nums):
#    return max(a*b for a, b in zip(list_nums, list_nums[1:]))
# arr = [3,6,-2,-5,7,3]
# print(adjacentElementsProduct(arr))

#_________________________________________
################ CodeSignal_5 #############

# def shapeArea(n):
#  return (n**2)+((n-1)**2)

#__________________________________________
################ CodeSignal_6 ##############

# def Make_Array_Consecutive2(statues):
#     s = sorted(statues, reverse=True)
#     count = 0
#     for i in range(len(s)-1):
#         x = (s[i] - s[i+1])-1
#         count += x
#     return count

#_________________________________________
############### CodeSignal_7 ############

# def almostIncreasingSequence(sequence):
#     removeCount = 0
#     if sequence[0] >= sequence[1]:
#         removeCount += 1
#     i = 2
#     while i < len(sequence):
#         if sequence[i - 1] >= sequence[i]:
#             removeCount += 1
#             if sequence[i - 2] >= sequence[i]:
#                 sequence[i] = sequence[i - 1]
#         i += 1
#     return (removeCount < 2)
# a = [ 10,1, 2, 3, 4, 5]
# print(almostIncreasingSequence(a))

#___________________________________________________
################## CodeSignal_8 ####################

# def solution(matrix):
#     c=0
#     j=0
#     for j in range(len(matrix[0])):
#         for i in matrix:
#             if i[j] == 0:
#                 break
#             else:
#                 c+= i[j]
#                 print(c)
#
# matrix = [[1, 1, 1, 0],
#           [0, 5, 0, 1],
#           [2, 1, 3, 10]]
# print(solution(matrix))

#____________________________________________
################# CodeSignal_9 ##############

# inputArray = ["enyky",
#  "benyky",
#  "yely",
#  "varennyky"]
# maxls= len(max(inputArray, key= len))
# print(maxls)
# new_ls= []
# for i in inputArray:
#     if len(i)==maxls:
#         new_ls.append(i)
# print(new_ls)

#_______________________________________________
################ CodeSignal_10 #################

# s1 = "aabcc"
# s2 = "adcaa"
# s1_ls = list(s1)
# s2_ls = list(s2)
# c=0
# for i in s1_ls:
#     for j in s2_ls:
#         if i == j:
#             c += 1
#             print(s2_ls)
#             s2_ls.remove(j)
#             break
# print(c)

#__________________________________________________
################## CodeSignal_11 ###################
#
# n = 1230
# n1 = [int(x) for x in str(n)]
# l = len(n1)
# m = l // 2
# s1 = n1[:m]
# s2 = n1[m:]
#
# print(bool(sum(s1)==sum(s2)))

#__________________________________________
############### CodeSignal_12 #############

# a = [-1, 150, 190, 170, -1, -1, 160, 180]
#
# for i in range(len(a)-1, 0, -1):
#     if a[i] > 0:
#         imax = i
#         for j in range(i):
#             if a[j] > a[imax]:
#                 print(a[imax])
#                 imax = j
#                 print(a[imax])
#         if imax != i:
#             a[i], a[imax] = a[imax], a[i]
# print(a)

#________________________________________________________
##################### CodeSignal_13 ##################
# def solution(inputString):
#     return eval('"' + inputString.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')
#
# print(solution("foo(bar)baz"))

# _______________________________________________________
###################  CodeSignal_14 ###################

# def solution(a):
#     team1 = sum(a[0::2])
#     team2 = sum(a[1::2])
#     print(team1, team2)
#
# j = [50, 60, 60, 45, 70]
# solution(j)


#____________________________________________________________
################ CodeSignal_15 #############################

# picture = ["abc",
#            "ded"]
# def solution(picture):
#
#     z = []
#     for i in picture:
#         s = (2+len(i)) * "*"
#         x ="*" + i + "*"
#         z.append(x)
#     z.insert(0, s)
#     z.append(s)
#     return z
#
# print(solution(picture))

#_______________________________________________________________
####################### CodeSignal_16 #########################

# a = [1, 2, 3]
#b = [1, 2, 3]
#1_______________________________________________________________
# def solution(a, b):
#     i = 0
#     i_val = []
#     while i < len(a):
#         if a[i] != b[i]:
#             i_val.append(i)
#         i += 1
#     if not i_val:
#         return True
#     if len(i_val) != 2:
#         return False
#     return a[i_val[0]] == b[i_val[1]] and a[i_val[1]] == b[i_val[0]]

#2________________________________________________________________

# def solution(A, B):
#    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2


#_________________________________________________________________
#################### CodeSignal_17 ###############################
#
# inputArray = [-1000, 0, -2, 0]
# s = 0
# count = 0
#
# for i in range(len(inputArray) - 1):
#     if inputArray[i] >= inputArray[i + 1]:
#         s = (inputArray[i] -inputArray[i + 1]) + 1
#         count += s
#         inputArray[i + 1]+= s
#
# print(inputArray)
# print(count)


#__________________________________________________________________
######################### CodeSignal_18 ############################

# def palindromeRearranging(inputString):
#
#     return sum(map(lambda x: inputString.count(x) % 2, set(inputString))) <= 1

#__________________________________________________________________
######################### CodeSignal_19 ###########################

# def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
#
#     return {yourLeft, yourRight} == {friendsLeft, friendsRight}









