# st=input('Enter a String')
# if len(st)%2==1:
#     print('string contains middle char')
# else:
#     print('String doesnt contain of middle char')

# data=eval(input('Enter the Data: '))
# if isinstance(data,(int,float,complex,bool)):
#     print(f'Entered data {data} is Individual Datatype')
# else:
#     print(f'entered data {data} is collection Datatype')

# data=eval(input('Enter the Data: '))
# if isinstance(data,(set,list,dict)):
#     print(f'Entered data {data} is Mutuable Datatype')
# else:
#     print(f'entered data {data} is Immutable Datatype')
'''to check if memory allocation is same or not'''
# a=45
# b=50
# if a is b:#id(a)==id(b)
#     print('address is same')
# else:
#     print('address is not same')

# '''to check if its homogeneous or hetrogeneous'''
# a=(10,20)
# if type(a[0])==type(a[1]):
#     print('It is Homogenous ')
# else:
#     print('It is hetrogenous')


# z='PRAVIN'
# z=z[len(z)//2]
# print('Middle value',z)

# '''wap to check wehethr the list contains middle value as string or not'''

# a=eval(['Hi',10,'Hello',56,'makan'])
# if a[len(z)//2]=='str':
#     print('Middle value is a String')

# else:
#     print('Middle value isnot sting')

'''check if characte is palindrom or not'''

# char=input('Enter a Char:')
# if char==char[ : :-1]:
#     print(f'{char}')

''' Wap to check whether a char is upper,lower,digit,or special character'''

# a=input('Enter a char: ')
# if a.isupper():
#     print(f'{a}----->is upper')

# elif a.islower():
#     print(f'{a}----->is upper')
# elif a.isdigit():
#     print(f'{a}----->is digit')
# else:
#     print(f'{a}----->is Special character')

'''Wap to buy cosmetic product '''

# st=input('Enter the cosmetics::')
# if st=='lipstick':
#     print('Lipstick is present')

# elif st=='kajol':
#     print('kajol is present')

# elif st=='concelear':
#     print('concelear is present')

# elif st=='eyeliner':
#     print('eyeliner is present')

# elif st=='Foundation':
#     print('Foundation is present')

# elif st=='Primer':
#     print('Primer is present')
 
# elif st=='Mascara':
#     print('Mascara is present')

# elif st=='Blush':
#     print('Blush is present')

# else: print('Item is Missing')

'''wap to buy brand from bar'''

# brand=input('Enter the brand:')
# if brand=='Teachers':
#     print(f'{brand}is present')
# elif brand=='old monk':
#     print(f'{brand}is present')

# elif brand=='KingFisher':
#     print(f'{brand}is present')

# elif brand=='Ram':
#     print(f'{brand}is present')

# elif brand=='corona':
#     print(f'{brand}is present')

# elif brand=='sprite':
#     print(f'{brand}is present')

# else:
#     print('close the bar')

'''trip'''
# amt=int(input('enter the amount:'))
# if amt>=100 and amt<=1000:
#     print('Sleep at home')

# elif amt>=1000 and amt<=2000:
#     print('Trip to Lonavla')

# elif amt>=3000 and amt<=5000:
#     print('Trip to Hampi')

# elif amt>=5000 and amt<=9000:
#     print('Trip to Goa')

# elif amt>=10000 and amt<=15000:
#     print('Trip to manali')

# elif amt>=15000 and amt<=20000:
#     print('Trip to Ladakh')

# elif amt>=20000 and amt<=25000:
#     print('Trip to Rameshwaram')

'''wap to check the char is upper case,convert into lower,
if lower case then convert into upper,
if digit print the reaminder when didvided by 3 and
 if char is  special char print print its ascii value'''

# s=input('Enter a character: ')
# if s.islower():
#     s=s.upper()
#     print('is lower')

# elif s.isupper():
#     s=s.lower()
#     print('is upper')

# elif s.isdigit():
#     print('is a digit',int(s)%3)
# else:
#     print('Is a Special Character',ord(s))

'''wap to check,values lies in which quadrant'''

# x=int(input('Enter a value:'))
# y=int(input('Enter a value:'))

# if x>=0 and y>=0:
#     print('values lie in 1st Quadrant')

# elif x<0 and y<0:
#     print('Value lies in 3rd Quadrant')

# elif y>=0 and x<0:
#     print('Value is present in 2nd quadrant')

# elif y<0 and x>=0:
#     print('Value present in 4th quadrant') 

'''To give output as single digit or double digit or triple digit...etc'''
# num=int(input('Enter a num:  '))
# a=str(num)
# if len(a)==1:
#     print('Integer is Single Digit')
# elif len(a)==2:
#     print('Integer is Double Digit')
# elif len(a)==3:
#     print('Integer is Triple digit')
# else:
#     print('Length is more than 3 digit',len(a))

''' fizz uzz'''
a=int(input('Enter a num:'))

if int(a)%5:
    print('Fizz Fizz')
elif int(a)%7:
    print('Buzz Buzz')
elif int(a)%5 and int(a)%7:
    print('Fizz Buzz')