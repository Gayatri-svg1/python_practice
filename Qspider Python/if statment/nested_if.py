# user_name='Gayatri'
# password='Pinkyy'

# u_n=input('Enter the user name: ')
# if u_n==user_name:
#     pss_wd=input('Enter the Password: ')
#     if pss_wd==password:
#         print('Successful login')

#     else:
#         print('Incorrect Password')

# else:
#     print('Invalid username')


'''Program to check if its vowel or not'''
# ch=input('enter the character:  ')
# if ch.isalpha():
#     if ch in [aeiouAEIOU]:
#         print('It is a vowel')

#     else:
#         print('It is a consonant')

# else:
#     print('It is a special character')

'''wap to print last value of a list if the last value of string is palindrome '''

# a=[10,4j+9,'Hello','False','mic','mom']

# if type(a[-1]) == str:
#     if a[-1]==a[-1][::-1]:
#         print('It is a palindrome')

#     else:
#         print('Not a palindrome')
# else:
#     print('Not a string')

''''''
# a=[10,5,15,10,12,14,15]

# lt=eval(input('Enter the list: '))
# if type(lt)==list:
#     if lt[-1]==lt[-1][::-1]:
#         print(lt[-1])
#     else:
#         print('not a palindrome string')
# else:
#     print('last value is not a string in the list')

'''wap to check the middle value inside is odd or not'''

lt=eval(input('Enter the list:  '))
if len(lt)%2==1:
    if lt[len(lt)//2]%2==1:
        print(f'{lt[len(lt)//2]}is even')

    else:
        print(f'{lt[len(lt)//2]}is odd')

else:
    print('No middle Element is Present')
