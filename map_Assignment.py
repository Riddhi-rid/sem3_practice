#questions
#1
num=[1,2,3,4,5]
x=list(map(lambda i:(i+i+i),num))
print(x)

# 2

tup_items=(1,3,7,8,4,5,2,15,6,22,12,89)
x=map(lambda i:i%2==0,tup_items)
print(list(x))


#3

def example(s):

    return s.lower()

exa=("THIS","IS","TUPLE")

exam=(tuple(map(example,exa)))

print(exam)

#4

import math


def square(s):
    return math.sqrt(s)
num=[4,9,16,25]

sq=list(map(square,num))

print(sq)


# 5

from collections import OrderedDict


def remove_duplicate(str1):
    return "".join(OrderedDict.fromkeys(str1))


print(remove_duplicate("patel"))

#6

from msilib.schema import Directory


def table(i):
    return i*5

num=[1,2,3,4,5,6,7,8,9,10]

tab=list(map(table,num))
print(tab)

#7
a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=list(map(lambda x,y:(x+y),a,b))
print(c)


#8
def float(i):
    return int(i)
num=[2.0,3.0,5.0]
x=list(map(float,num))
print(x)

# 9

list=[1,2,3,'a','b','c']
list.reverse()
print(list)

#10

def DICTONARY(d):
    return d.lower()
dict={'a':'RIDDHI','b':'DRISHTI','c':'SHRISTI'}

dic=list(map(lambda x :(x[0],x[1]+'@gmail.com'),dict.items()))

print((dic))