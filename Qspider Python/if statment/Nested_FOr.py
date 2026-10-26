# for i in range(1,7,2):
#     for j in range(10,20,2):
#         print(i,j)

# for i in range(1,5):
#     for j in range(2,7):
#         for k in range(4,6):
#             print(i,j,k)


'''a=[100,200,350,450]  output=[1000,900,750,650]'''
# a=[100,200,350,450]
# out=[]
# for i in a:
#     s=0
#     for j in a:
#         s=s+j
#     out.append(s-i)
# print(out)

'''a=['Python','outswing',10,45,4j+9,True,'Java','Network',False,92.5]
output={'Python':'PyThOn','Outswing':'OuTsWiNg','Java':'JaVa','Network':'NeTwOrK'}
'''
# z=a=['Python','outswing',10,45,4j+9,True,'Java','Network',False,92.5]
# out={}

# for i in z:
#     if type(i)==str:
#         st=''
#         for j in range(len(i)):
#             if j%2==0:
#                 st=st+i[j].upper()
#             else:
#                 st=st+i[j]
#         out[i]=st
# print(out)

'''
a=[100,200,300,250,450,150,750]
s=300
o/p=[[100,200,250,150],[450,750]]
'''
# a=[100,200,300,250,450,150,750]

# s=300
# l=[]
# m=[]
# for i in a:
#     if i<300:
#         l+=[i]
#     if i>300:
#         m+=[i]
# print([l,m])

'''Input:-'Rohit Sharma' 
Output:-{'Rohit':'oi','Sharma':'aa'}'''

# z='ROHIT SHARMA'
# s=z.split()
# out={}
# for i in s:
#     st=''
#     for j in i:
#         if j in 'AEIOUaeiou':
#             st+=j
#         out[i]=st
# print(out)