# 1. Print each character of a string a="Tree Notes"

# a="Tree Notes"
# for b in a:
#     print(b)
# 2.Print vowels only s = "education"

# s="education"
# for i in (s):
#     if i in "aeiou":
#         print(i)


''' 3.Count uppercase letters s = "PyTHon" '''
# s = 'PyTHon'
# i=s.isupper()
# for i in s:
#     if i.isupper():
#         print(i)

'''4.Print digits from string '''
# s = 'as23df43fv3'
# # i=s.isupper()
# for i in s:
#     if i.isdigit():
#         print(i)
# s = "ab12cd34" 
'''5.Sum of list elements '''
# x=[25,70,90,100] 
# total=0
# for i in x:
#     total=total+1
# print(total)
# x = [10, 20, 30, 40, 50]

# total = 0

# for i in x:
#     total = total + i

# print( total)
    
'''6.Print even numbers from list'''
# e=[23,45,66,78,90]
# for i in e:
#     if i%2==0:
#         print(i)

'''7.Print negative numbers '''
# l = [4,-2,7,-9,3] 

# for i in l:
#     if i<0:
#         print(i)
'Count odd numbers '''
# l = [1,2,3,4,5,6,7] 
# count =0
# for i in l:
#     if i%2 !=0:
#         count += 1
# print(count)

# l = [1, 2, 3, 4, 5, 6, 7]
# count = 0
# for i in l:
#     if i % 2 != 0:
#         count += 1
# print("Count of odd numbers:", count)

# 9.Print odd numbers 1 to 20 
# for i in range(1,21):
#     if i % 2 != 0:
#         print(i)

# 10.wap Sum from 1 to 50 
# sum=0
# for i in range(1,51):
#     sum = sum +i
# print(sum)

'''11.wap Print numbers divisible by 5 (1 to 51)'''

# for i in range(1,51):
#     if i%5==0:
#         print(i)
'''12.Reverse 10 to 1'''

# for i in range(10,0,-1):
#     print(i)

'''13.Squares from 1 to 10'''
# for i in range(1,10):
#     i=i**2
#     print(i)

'''14.Print ASCII values of characters
s='ABC'''
# s='ABC'
# for i in s:
#     print(ord(i))

'''15.wap to Count consonants
s = "education"'''
# s='education'
# x=0
# for i in s:
#     if i not in 'aeiouAeiou':
#         print(i)
#         x=x+1
# print(x)


'''16.Print numbers greater than 50'''
# l = [23,67,12,89,54]

# for i in l:
#     if i>50:
#         print(i)

'''17.Count positive numbers'''
# l = [-1,4,-3,7,9]
# x=0
# for i in l:
#     if i>0:
#         print(i)
#         x=x+1
# print(x)

'''18.wap to Separate even/odd'''
# l=[1,2,3,4,5,6,7,8]
# e=[]
# o=[]
# for i in l:
#     if i%2==0:
#         e=e+[i]
#     elif i%2 !=0:
#         o=o+[i]
# print(e)
# print(o)
    
'''19.Sum of even numbers'''
# e=[1,2,3,4,5,6,7,8]
# add=0

# for i in e:
#     if i%2==0:
#         add += i
# print(add)

'''20.wap to print the number form 1 -20 segregate even and odd
number into list'''
# e=[]
# o=[]
# for i in range(1,-21,-1):
#     if i%2==0:
#         e=e+[i]
#     elif i%2 !=0:
#         o=o+[i]
# print(e)
# print(o)

'''21.wap to extract vowels and digits in a string'''
# s="hello123"
# v=''
# d=''
# for i in s:
#     if i in('aeiou'):
#         v=v+i

#     elif i.isdigit():
#         d=d+i
# print(v)
# print(d)
'''22.wap to capitalize only the first letter of every word in the given
list'''
# l=["vaidegi","rahul","shivam","kapil","patil"]
# for i in l:
#     i=i.capitalize()
#     print(i)

'''23.wap to extract only individual data types form the list'''
# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# for i in l:
#     if isinstance(i,(int,complex,float)):
#         print(i)

'''24.wap to extract only individual data types from the list and sum
all the individual data types'''
# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# sum=0
# for i in l:
#     if isinstance(i,(int,complex,float)):
#         sum +=i
#         print(i)
# print(sum)

'''25.wap to print the count of alphabets and numbers and space in
the given string'''
# s="india got the independence in the year 1947"
# c=0
# d=0
# sp=0
# for i in s:
#     if i.isalpha():
#         c += 1
#     elif i.isspace():
#         sp += 1
#     elif i.isdigit():
#         d +=1
# print(c)
# print(sp)
# print(d)

'''26.wap to check how many words are present in the given sentence'''
# s="hello world sentence"
# c=0
# for i in s:
#     if i.isalpha():
#         c += 1
# print(c)


# s="hello world sentence"
# # print(s.split())
# x=s.split()
# total=0
# for i in x:
#     total=total+1
# print(total)

'''27.wap to create a dictionary and print the characters
and its Ascii value pair'''
s="hello world"
d={}
for i in s:
   d.update({i:ord(i)})
print(d)

d={}
for i in s:
   d[i]=ord(i)
print(d)


'''28.wap to create a dictionary and traverse into it and if the length is
 even print as it else reverse it
 names=["apple","google","yahoo","microsoft","gmail","walmart"]
 output:-->{'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay',
 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}'''


'''29.wap to print series of factorial(take user input)'''


'''30.wap to create a dictionary with element and its count pair

l=["yellow","red","black","pink","orange","green","red","pink","yell
ow"]
output:-->
{'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}'''



'''31.wap to find the length of the string without using inbuilt function
s="Never Give Up"'''



'''33.wap to reverse a string without using inbuilt function
x="you did it guys"'''



'''33.wap to print alternative character from a given string
s="hello python"'''


'''34.wap to create a dictionary index and word pair
s="tomorrow is weekend and non-veg special"
o/p:-->{0: 'tomorrow', 1: 'is', 2: 'weekend', 3: 'and', 4: 'non-veg', 5:
'special'}'''