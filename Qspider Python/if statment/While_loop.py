'''1-->WAP TO PRINT ALL THE VALUES PRESENT AT EVEN INDEX FROM THE GIVEN LIST ONLY IF IT IS A FLOAT
NUMBER----->A=['SINA',2.2,3.4,4J+9,5.6,70,'HELLO']'''

A = ['SINA', 2.2, 3.4, 4J+9, 5.6, 70, 'HELLO']
i=0
res=()
while i<len(A):
    if i%2==0 and type(A[i])==float:
        res+=(A[i],)
    i+=1
print(res)
'''2-->WAP TO CONVERT ALL THE LOWER CASE CHAR TO UPPER CASE CHAR IN A STRING---->I/P='mAnoJ',O/P='MANOJ' '''

# s ='mAnoJ'
# i=0
# res=''
# while i<len(s):
#     if s[i].islower():
#         res=res+s[i].upper()
#     else:
#         res=res+s[i]
#     i+=1
# print(res)
'''3-->WAP TO FETCH ALL THE STRING DATA ITEMS PRESENT INSIDE A LIST ONLY IF THE LEN OF STRING IS GREATER THAN 5.--->TAKE USER INPUT.'''
# L=eval(input("Enter a list: "))
# i=0
# while i<len(L):
#     if type(L[i])==str and len(L[i])>5:
#         print(i)
#     i+=1
    
'''4-->WAP TO EXTRACT ALL THE UPPERCASE CHAR PRESENT AT MULTIPLE OF 3RD INDEX IN A GIVEN STRING ONLY IF ITS ASCII VALUE IS EVEN.--->TAKE USER INPUT.'''
# s=input("Enter a string: ")
# i=0

# while i<len(s):
#     if i%3==0:
#         if s[i].isupper(): 
#             if ord(s[i])%2 == 0:
#                 print(s[i])
#     i+= 1
'''5-->Find the sum of ASCII values of all special characters'''

# s=input("Enter a string: ")
# i=0
# total=0

# while i<len(s):
#     if not s[i].isalnum():
#         total+=ord(s[i])
#     i+=1

# print(total)

'''6-->WAP TO REPLACE SPACE BY UNDERSCORE IN A GIVEN STRING.--->
I/P='HELLO HAI HARISH'
O/P='HELLO_HAI_HARISH' '''

# s='HELLO HAI HARISH'
# i=0
# res=''
# while i<len(s):
#     if s[i]==' ':
#         res+='_'
#     else:
#         res+=s[i]
#     i+=1

# print(res)

'''7-->WAP TO COUNT THE NUMBER OF OCCURENCE OF A SPECIFIED CHAR IN A GIVEN STRING.
I/P='ANUSHKA SHARMA' IF 'A' IS APECIFIED CHAR-->O/P=4'''

# s='ANUSHKA SHARMA'
# char=input("Enter a character: ")
# i=0
# count=0

# while i<len(s):
#     if s[i]==char:
#         count+=1
#     i+=1

# print(count)


'''8-->WAP TO FIND FACTORS OF A GIVEN NUMBER.
I/P=12
O/P=[1,2,3,4,6,12]'''

# n=int(input("Enter a number: "))
# i=1
# L=[]

# while i<=n:
#     if n%i==0:
#         L+=[i]
#     i+=1

# print(L)


'''9-->WAP TO FIND ALL SINGLE VALUE DATATYPE IN A GIVEN LIST.-->TAKE USER INPUT'''

# L=eval(input("Enter a list: "))
# i=0

# while i<len(L):
#     if type(L[i]) in (int,float,complex,bool):
#         print(L[i])
#     i+=1


'''10-->WAP TO FIND SUM OF ALL THE INTEGER NUMBERS WHICH ARE DIVISIBLE BY 3 AND 7 FROM THE RANGE BETWEEN 10 TO 100.'''

# i=10
# total=0

# while i<=100:
#     if i%3==0 and i%7==0:
#         total+=i
#     i+=1

# print(total)


'''Toggle string'''

# a=input('Enter a String: ')
# i=0
# while i<len(a):
#     i=a.swapcase()
#     print(i)
# i+=1

# r=input('Enter a String: ')
# i=0
# res=''
# while i<len(r):
#     if 'A'<=r[i]<='Z':
#         res=res+chr(ord(r[i])+32)
#     elif 'a'<=r[i]<='z':
#         res=res+chr(ord(r[i])-32)
#     else:
#         res=res+r[i]
#     i+=1
# print(res)

# if u want to convert from lower to uppercase then(-32) and to convert from uppercase to lower case(+32)

# st=input('Enter String: ')
# i=0
# out=''
# while i<len(st):
#     out=st[i]+out
#     i+=1
# print(out)

'''factorial'''
# n=int(input("Enter a number: "))
# i=1
# L=[]

# while i<=n:
#     if n%i==0:
#         L=[i]+L#l.append(i)
#     i+=1

# print(L)

'''sum of Perfect Number'''

# a=int(input('Enter a Number: '))
# i=1
# res=0
# while i<a:
#     if a%i==0:
#         res=res+i 
#     i+=1
# if a==res:
#     print(f'{a} is a perfect Number')
# else:
#     print('Not a Perfect Number')


# zensar plsql,city,trigger(sql),
'''Prime Number'''
# n=int(input('Enter a Number: '))
# i=1
# count=0
# while i<=n:
#     if n%i==0:
#         count=count+1
#     i+=1
# if count==2:
#     print(f'{n}--->is a Prime Number')
# else:
#     print(f'{n}---->is not Prime')

# a=['x','y','z']
# b=[10,20,30]

# d={}
# i=0
# while i<len(a):
#     d[a[i]] = b[i]###i.update({d[i]:b[i]})
#     i+=1
# print(d)

'''wap to reverse a number without slicing or typecasting'''

# last didigt====floor 
# n=int(input('Enter the Number: '))
# temp=0
# while n>0:
#     l_d=n%10
#     temp=(temp*10)+l_d
#     n=n//10
# print(temp)

'''To find palindrome without slicing or typecasting'''

# n=int(input('Enter the Number: '))
# b=n
# temp=0
# while n>0:
#     l_d=n%10
#     temp=(temp*10)+l_d
#     n=n//10
# if temp==b:
#     print(f'{b}---->is a palindrome')
# else:
#     print(f'{b}----->not a Palindrome')


'''Addition of digits inside a number'''

# n=int(input('Enter the Number: '))
# temp=0
# while n>0:
#     l_d=n%10
#     temp=temp+l_d
#     n=n//10
# print(temp)

''''''
# a='123456789'
# out='135792468'
# a = '123456789'
# i=0
# even=''
# odd=''
# while i<len(a):
#     if int(a[i])%2==0:
#         even+=a[i]
#     elif int(a[i])%2==1:
#         odd+=a[i]
#     i+=1
# print(even+odd)

'''sum of digit and their cube'''
# n=int(input('Enter the Number: '))
# sum=0
# while n>0:
#     l_d=n%10
#     sum=sum+l_d
#     n=n//10
# print(sum)-----------not done


'''Armstrong Number'''

# n=153
# a=n
# s=str(n)
# l=len(s)
# sum=0
# while n>0:
#     l_d=n%10
#     sum=sum+l_d**l
#     n=n//10
# if sum==a:
#     print(f'{a}is a Armstrong')
# else:
#     print(f'{a}is not a Armstrong')


'''*******************Diserium****************'''
# n=153
# a=n
# s=str(n)
# l=len(s)
# sum=0
# while n>0:
#     l_d=(n%10)
#     sum=sum+l_d**l
    
#     n=n//10
# if sum==a:
#     print(f'{a} is a diserium')
# else:
#     print(f'{a} is not a diserium')----------->Not done
'''1st digit if number'''
# n=468
# print(n//100)

# while n>9:#to print 1st number,,,to print 2nd digit use 99
#     n=n//100
