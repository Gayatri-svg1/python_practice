'''1.wap to check whether the given character is 
uppercase/lowercase/digit/special (with and without using inbuilt function) '''

# a=(input('Enter an value: '))

# if a.isupper():
#     print('it is an upper case charachter')

# elif a.islower():
#     print('it is an lower case charachter')


# elif a.isdigit():
#     print('it is an digit ')


# else:
#     print('it is an special charachter')




# a = input("Enter a character: ")

# if 'A' <= a <= 'Z':
#     print("It is an uppercase character")

# elif 'a' <= a <= 'z':
#     print("It is a lowercase character")

# elif '0' <= a <= '9':
#     print("It is a digit")

# else:
#     print("It is a special character")



'''2.wap to check a data is a 
sequence/iterable/individual data type '''

# a=eval(input('Enter a input: '))
# if isinstance(a,(set,dict)):
#     print('It is Iterable')

# elif isinstance(a,(str,list,tuple)):
#     print('It is a Sequence Datatype')

# else:
#     print('It is a Individual Datatype')

'''3.wap if input is string return its length,else if 
input is list pop element,else 
if input is tuple reverse else invalid input '''

# a=eval(input('Enter a Value: '))
# if isinstance(a,(str)):
#     a=len(a)
#     print('It is a String',a)

# elif isinstance(a,(list)):
#     a=a.pop()
#     print('It is a list')
#     print('removed value is',a)

# elif isinstance(a,(tuple)):
#     a=a[::-1]
#     print('It is a tuple',a)


'''4.wap to check a age belongs to category 0 to 17 child 
and 18 to 30 ur adult,31 to 60 ur men,61 to 100 senior 
citizen,else 
invalid '''

# Age=int(input('Enter ur age: '))
# if Age>=0 and Age<=17:
#     print('You r a child')
# elif Age>=18 and Age<=30:
#     print('You r a adult')

# elif Age>=31 and Age<=60:
#     print('You r a men')

# elif  Age>=61 and Age<=100:
#     print('You r a senior')

'''5.wap to give hike to an employee based on his experience,
u should ask employee date of joining 
exp 0 to 2 years no hike 
and 3 to 5 years 5000rs hike,and 
6 to 8 years 7000 rs and 9 to n years 10000 
rs'''
# doj=int(input('Enter date of Joining:'))
# if doj>=0 and doj<=2:
#     print('No Hike')

# elif doj>=3 and doj<=5:
#     print('Increase Hike by',+5000)

# elif doj>=6 and doj<=8:
#     print('Increase Hike by',+7000)

# elif doj>=9 and doj<=20:
#     print('Hike increaesed by',+10000)


'''6.wap to check which is smallest value among 3 numbers 
a=65  b=34  c=76 '''

# a=65
# b=34
# c=76
# if a>b>c:
#     print('a is smallest')
# elif b>a>c:
#     print('b is smallest')

# elif c>b>a:
#     print('it is largest')

'''7.wap to take marks of 5 sub,calculate the average if 
the average is b/w 90-100 print Distinction 
if 75-89 print first class and if it's 60-74 print 
second class, if 50-59 print Third class,below 50 is 
fail 
note:-->max marks is 100  '''

# s1=float(input('Enter the marks:'))
# s2=float(input('Enter the Marks:'))
# s3=float(input('Enter the Marks:'))
# s4=float(input('Enter the marks:'))
# s5=float(input('Enter the marks:'))

# Average=(s1+s2+s3+s4+s5)/5 
# if Average>=90 and Average<=100 :
#     print('Distinction')
# elif Average>=75 and Average<=89:
#     print('First Class')

# elif Average>=60 and Average<=74:
#     print('Second Class')

# elif Average>=50 and Average<=59:
#     print('Third Class')
# else:
#     print('Fail')


'''8.wap  to check the height of the student and make 
them stand in order '''
# a1=float(input('Height of student1:'))
# a2=float(input('Height of student1:'))
# a3=float(input('Height of student1:'))
# a4=float(input('Height of student1:'))
# a5=float(input('Height of student1:'))
# if a1>a2 and a2>a3 and a3>a4 and a4>a5:
#     print(a1,'is the tallest')
# elif a2>a1 and a1>a3 and a3>a4 and a4>a5:
#     print(a1,'is the tallest')

# height=[]

'''9.wap to check eligibility for marriage '''


# age=int(input('Enter the Age: '))
# if age>18:
#     print('Eligible to Marry')
# else:
#     print('Not Eligible to Marry')


'''10.wap to give discount to customer based on total 
price(p1+p2+p3) 1000 to 3000 price 500 discount and 
3001 to 5000 price 1000 discount more than 5001 price 
1200 discount and less than 1000 price no discount. '''









'''11.wap to check if the given number is even or odd or 
Zero '''

# a=int(input('Enter the num: '))
# if a%2 !=0:
#     print('is odd')
# else:
#   print('is even')


'''12.wap to check signal lights 
color=["red","yellow","green"]'''
# color=input('Enter Signal Light: ')
# # color=["red","yellow","green"]
# if color=="red":
#     print("Stop")
# elif color =="yellow":
#     print("Slow Down")
# elif color==("green"):
#     print("Goooo")

