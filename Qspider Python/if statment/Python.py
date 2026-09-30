# '''1.wap to check the number is odd (take user input)

# a=int(input('Enter the num: '))
# if a%2 !=0:
#     print('is odd')
# 1.wap to check the number is even (take user input)
# a=int(input('Enter the num: '))
# if a%2 ==0:
#     print('is even')

# '''wap to check if the student has scored 70% print "good luck "(take user input)'''
# Score=int(input('Enter the score: '))
# if Score>=70:
#     print('Good Luck')


# '''wap to check if the student has scored 70% print "good luck "(take user input)'''
# score=int(input('Enter the score: '))
# if score>=70:
#     print('Goood Luck')

''' wap to check which number is greater using if condition a=98 b=67 '''

# a=98
# b=67
# if a>b:
# print('a is greater than b')

# '''wap to check if the given string has even length of character 
# s="hey guys you all are Osam"'''

# s="hey guys you all are Osamm"
# if len(s)%2==0:
#     print('Length is even')

# ''' wap to check if the given number is divisible by 5 (take user input)'''
# Num=int(input('Enter a num: '))
# if Num%5==0:
#     print('It is Divisible by 5')

# ''' 7.wap to check if the given programming is present in the list 
# p=["java","python","c","c++","RUBy","golang"]'''

# p=["java","python","c","c++","RUBy","golang"]
# char=str(input('Enter the char:'))
# if char in p:
#     print('Word is present in the list')

# '''8.wap to check eligible to vote take user 
# input as a age '''

# Age=int(input('Enter ur age: '))
# if Age>=18:
#     print('You r elegible to vote')

# '''9.wap to check if the given number is positive take user input '''
# Num=int(input('Enter a Num:'))
# if Num>0:
#     print('Its Positive')

# '''10.wap to check if the given string is palindrome (take user input)'''

# Stri=input('enter a word: ')
# if Stri==Stri[::-1]:
#     print('It is Palandrome')

# '''11.wap to check if the first letter in the given string is consonant 
# s="Lahari is a good student" '''

# s="Lahari is a good student"
# if s[0] not in "AEIOUaeiou":
#     print("Consonant")

# '''12.wap to check the given string is uppercase or not (take user input) '''

# a=input('Enter a String: ')
# if a.isupper:
#     print('It is Upper')


# '''13.wap to check the given value is string'''

# a=input('Enter a String: ')
# if type(a)==str:
#     print('Its a string')

# '''14.wap to display "Python Coding" if the number is greater than 1 and less than 5 '''

# a=int(input('enter a string:'))
# if a>1 and a<5:
#     print('Python Programing')

# '''15.wap to check whether given number is negative and print "its negative guys"'''
# Num=int(input('Enter a Num:'))
# if Num<0:
#    print('Its Negative Guys')

# '''16.wap to check whether given input is divisible by 2 and 6 if condition is True 
# ,convert the given number to complex number.(take user input)'''

# b=int(input('Enter a Number :  '))
# if b%2==0 and b%6==0:
#     print('true',complex(b))
 
# '''17.wap to check whether the given number is even or not,if even store the value inside the list '''
# a=int(input('Enter the number: '))

# if a%2==0:
#     l=[a]
#     print(f'{l}its even')#To add list

# '''19.wap to check whether a given value is divisible by 5 and 7,if the value is 
# divisible then display the square of the values (take user input) '''

# w=int(input('Enter a num: '))
# if w%5==0 and w%7==0:
#     print('Is divisible by 5 and 7',w**2)

# '''20.wap to check whether a given value is present in between 45 and 200 and the number 
# should be divisible by 4 and 5 ,if satisfied,display the ascii characters (take 
# user input)'''

# num = int(input("Enter a number: "))

# if num >= 45 and num <= 200 and num % 4 == 0 and num % 5 == 0:
#     print("The number is between 45 and 200 and divisible by 4 and 5")
#     print("ASCII character:", chr(num))


# '''21.wap to checking if a string contains a substring string="hello world" 
# sub_string="world"'''

# string = "hello world"
# sub_string = "world"
# if sub_string in string:
#     print("Substring is present")

# '''22.wap to check whether a character is in the alphabet or not,if it is alphabet,store the 
# value inside  a dict(key as a character and value as a ascii value)'''

# a=(input('enter a char: '))
# if a.isalpha():
#     b={a:ord(a)}
#     print('it is alphabet',b)

'''23.wap to check whether a character is in uppercase or not,if uppercase,convert to 
lowercase and store the value inside the dictionary (character as key and ascii as value) take user input '''

h=(input('enter a char: '))
if h.isupper():
    h=h.lower()#lower is to convert into lower case
    b={h:ord(h)}
    print('it is Uppercase',b)