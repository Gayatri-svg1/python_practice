'''90. Wap to get the following output.
 S='hai hello'
 Out={'hai':'ai','hello':'eo'}'''

# S="hai hello"
# a={}
# for i in S.split():
#     a[i]=i in 'aeiou' and i[1:] or i[-2:]
# print(a)

'''91. Wap to get the following output.
 S=[‘http://jiocinema.com’,’http://file.py’,’web.html’,’http://amazom.com’,’http://www.org’]
 Out=[‘com’,’py’,’html’,’org’]'''
# S=['jiocinema.com','file.py','web.html','amazom.com','www.org']
# l=[]

# for i in S:
#     l=l+[i.split('.')[-1]]
# print(l)


'''92. Wap to get the following output.
 S=[‘http://jiocinema.com’,’http://file.py’,’web.html’,’http://amazom.com’,’http://www.org ’http://python.py’]
 Out={‘com’:[‘jiocinema’,’amazon’],’py’:[‘file’,’python’],’html’:[‘web’],
 ’org’:[‘www’]}'''

# s=['jiocinema.com','file.py','web.html','amazom.com','www.org','python.py']
# a={}

# for i in s:
#     k=i.split('.')[-1]
#     v=i.split('.')[0]
#     if k not in a:
#         a[k]=[v]
#     else:
#         a[k].append(v)
# print(a)
'''93.Wap to get the following output.
 L=[‘hai’,34,3.4,’hello’,90,’byebye’]
 Out={‘hai’:’hi’,’hello’:’ho’,’byebye’:’be’}'''
# L=['hai',34,3.4,'hello',90,'byebye']
# s={}
# for i in L:
#     if type(i)==str:
#         s[i]=i[0]+i[-1]
# print(s)
'''94.wap to get the following output.
 In='hello'
 Out={0:’h’,1:’e’,2:’l’,3:’l’,4:’e’}'''
# In='hello'
# s={}
# for i in range(len(In)):
#     if i>=0:
#         s[i]=In[i]
# print(s)

'''95.Wap to extract all the string values present in list only if the string is palindrome.'''
# a=eval(input('Enter a value: '))
# l=[]
# for i in a:
#     if type(i)==str:
#         if i==i[::-1]:
#             l+=[i]
# print(l)

'''96.Wap to return the positions of vowels present in the given string.'''
# s=input('Enter a String: ')
# for i in range(len(s)):
#     if s[i] in 'aeiouAEIOU':
#         print(i)

'''97.Wap to check whether the given collection is having nested collection or not.'''
# s=eval(input('Enter a Collection: '))

# for i in s:
#     if isinstance(i,(list, tuple, set, dict)):
#         print('It has a Nested Collection')
#         break
# else:
#     print('Nested not present')

'''98.Wap to count the number of words in a string.'''
# w=input('Enter a String: ')
# count=0
# a =w.split()

# for i in a:
#     if len(i)>0:
#         count+=1
# print(count)

'''99.Wap to check whether the number is neon number or not.
N=9→9**2=81→8+1=9'''

# s=int(input("Enter a Number: "))
# t=s**2
# sum=0
# while t>0:
#     l_d=t%10
#     sum+=l_d
#     t//=10
# if sum==s:
#     print('Neon number')
# else:
#     print('Not a neon number')
'''100.Wap to find the longest word in a string.'''
# s=input('Enter a String: ')
# str=''
# for i in s:
#     if len(s)>len(str):
#         str=
# print(i)

'''101.Wap to replace the special character present in a string by space.'''
# a=input('Enter a String: ')

# for i in a:
#     if not i.isalnum():
#         a=a.replace(i," ")
# print(a,end=' ')
'''102.wap to print the square of all the integers present in a list.'''
# a=eval(input('Enter a List'))

# for i in a:
#     if type(i)==int:
#         print("Square of Integers: ",i**2,end=' ')
'''103.Wap to extract all the odd number present at even index from a list.'''
# a=eval(input('Enter a List: '))
# #l=[]
# for i in range(len(a)):
#     if i%2==0 and a[i]%2!=0:
#         print(a[i],end=' ')
'''104.Wap to extract all the mutable values present in a tuple.'''
# a=eval(input('Enter a Tuple: '))

# for i in a:
#     if isinstance(i,(set,dict,list)):
#         print(i)

'''105.Wap to get the following output.
 In=’10100011231’
 Out=’010111000’ ( 0→1 and 1→0 if it is other than 0 &1 ignore)'''

# s='10100011231'
# str=''
# for i in s:
#     if i=='0':
#         str+='1'
#     elif i=='1':
#         str+='0'
# print(str)
'''106.Wap to get the following output.
 In='abacbaacc'
 Out={'a':4,'b':2,'c':3}'''

# a='abacbaacc'
# d={}

# for i in a:
#     if i not in d:
#         d[i]=a.count(i)
# print(d)
'''107.wap to extract keyvalue pair from the dictionary only if the key is Boolean datatype.'''
# s=eval(input('Enter a String: '))
# d={}

# for i in d:
#     if type(i)==bool:
#         d[i]=i[s]   
# print(d)

'''108.Wap to get the following output.
 In=’127342’
 Out=’242173’ (extract even and odd digits separately and concatenate both)'''

# a='127342'
# e=''
# o=''
# for i in a:
#     if int(i)%2==0:
#         e+=i
#     else:
#         o+=i
# print(e+o)
'''109.Wap to checek whether the string is having only lowercase or not using continue.'''
# s=input('Enter a String: ')

# for i in s:
#     if i.isupper():
#         continue
#     print(i)
'''110.Wap to find the sum square of individual digits of a string.'''
# s=input('Enter a number: ')
# sum=0
# for i in s:
#     if i.isdigit():
#         sum+=int(i)**2
# print(sum)
'''Convert Binary to decimal'''

# bv=int(input('Enter a Value: '))
# dv=0
# p=0
# while bv>0:
#     r=bv%10
#     dv+=r*(2**p)
#     bv//=10
#     p+=1
# print(dv)

'''decimal to Binary'''

# dv=int(input('Enter ur Data:  '))
# res=''
# while dv>0:
#     rem=dv%2
#     res=str(rem)+res
#     dv//=2
# print(res)

'''HCF'''
# num1=int(input("enter the number:  "))
# num2=int(input('ENter the Number: '))

# while num2>0:
#     num1,num2=num2,num1%num2
# print(num1)
'''Longest'''

a=input('Enter the string: ')
r=a.split()
maxi=r[0]
for i in r:
    if len(i)>len(maxi):
        maxi=i
print(maxi)