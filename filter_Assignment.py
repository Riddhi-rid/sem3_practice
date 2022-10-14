from logging import Filter
from numbers import Number


#1

list1=[1,0,-1,-2,-3]
negative_no=list(filter(lambda x:x<0,list1))
print(negative_no)

#2

number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
odd_no=list(filter(lambda x:x%2!=0,number))
print(odd_no)

#3

str="this is python advance"
list1=list(filter(lambda x: True if x.lower() in "aeiou" else False,str))
print(list1)

#4

str="i am riddhi my birth date is 01-09-2003"
list1=list(filter(lambda x:True if x in "0123456789" else False,str))
print(list1)

#5

list1=[10,-20,-30,-40,-50,-60,-80,90,70,100]
list2=list(filter(lambda x:True if x>0 else False,map(lambda x:x*-1,list1)))
print(list2)