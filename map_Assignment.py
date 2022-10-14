#questions
#1
# num=[1,2,3,4,5]
# x=list(map(lambda i:(i+i+i),num))
# print(x)

#3

# def example(s):

#     return s.lower()

# exa=("THIS","IS","TUPLE")

# exam=(tuple(map(example,exa)))

# print(exam)

#4

# import math


# def square(s):
#     return math.sqrt(s)
# num=[4,9,16,25]

# sq=list(map(square,num))

# print(sq)

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


#10

def DICTONARY(d):
    return d.lower()
dict={'a':'RIDDHI','b':'DRISHTI','c':'SHRISTI'}

dic=list(map(lambda x :(x[0],x[1]+'@gmail.com'),dict.items()))

print((dic))