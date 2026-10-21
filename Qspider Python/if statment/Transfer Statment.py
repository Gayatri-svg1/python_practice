# for i in range(1,11):
#     if i==5:
#         break
#     print(i, end=" ")

# a="hello monkey's"
# for i in a:
#     if i=='k':
#         break
#     print(i,end=' ')


# for i in range(1,21):
#     if i%2==0:
#         continue
#     print(i,end=' ')

# a=[10,-20,6,-9,8,-10]
# for i in a:
#     if i<0:
#         continue
#     print(i,end=' ')


# p='python and powerbi'
# for i in p:
#     if i in 'aeiouAEIOU':
#         continue
#     print(i,end=' ') 

a='101101010'
b='110011001'
count=0
for i in a,b:
    if a in b:
        count+=i
        continue
    print(i,end=' ')

a='101101010'
b='110011001'
count=0
for i in a:
    if i=='0':
        continue
    count+=1
print(count)

# a='abc2345!@@#$$'
# for i in a:
#     if i.isalnum():
#         continue
#     print(i,end=' ')

