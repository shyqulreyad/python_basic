import keyword
my_name = 'shyqulreyad'
#strings with single quote in it should be define with "" quote
title = "it's nice to learn python"
print(title)
#strings with multiple line should be define with tripple quote
heading = '''it's a multiple line 
heading
like i can add more line into this'''
#when we have single or double quote in string we have to use tripple quote like
example = ''' it's a good "practice" '''
print(example)
print(heading)
print('hi',my_name)
a, b, c = 10, True, 1
print(b)
print(a)
print(c)
res = a + c
print (res)
print(id(res))
print(keyword.kwlist)
print(type(True))

x= 10
y = -20
z = x < y
print(z)
g= None
print(type(g))
print(g)
print(id(g))
#arithmetic operators
print (4-12)
print(4*2)
print(13.56%4.56 )
print(20**3.7)
print(10 // 2.5)
print(-5 // 2 )

#relational operators
print (x < y)
print(x > y)
cx = 'H'
cy = 'p'
print(ord(cx))
print(ord(cy))
ax = 'Hitttt'
ay = 'hi'
#on stirng comparision it compare unicode of the char
print(ax > ay)
bx = 'aa'
by = 10
# this comparision is not available
#print(bx> by)
print('H' == 72)

#logical operation
#AND
#True and True => True
#True and False => False
#False and True => False
#False and False => False

#OR
#True or True => True
#True or False => True
#False of True => True
#False or False => False

#NOT
#not ture = false
#not false = true

lx = False
ly = False
lz = True
lm = False
print (lx and ly)
print (lx and lz)
print (lx or lz)
print (not lx)
print (ly and lm)

#input function
# xi = input('enter value')
# print(xi)
# print (type(xi))
#
# a = input('enter first value ')
# b = input('enter second value')
#input function always return string so to convert it into integer or float we can use int() & float() to avoid error we can use eval() function
# print(eval(a) + eval(b))
#output or print function
print('hi reyad \n' *10)
#control statements
if lx :
    print('hi there ')
else :
    print('bye')

# n = eval(input('enter any number'))
# if n > 0 :
#     print('value is greater than Zero')
# elif n== 0:
#     print('value is zero')
# else :
#     print('value is smaller than zero')
# print('end of program')

#range function

x =range(5)
print(x)
print(type(x))
print(x[3])

y = range(5,10)
print(y)
print(y[3])
xl = range(2,10,2)
print(xl[2])
#range function always work on integer
xc = range(10, 0, -1 )
#for loop
for i in xl:
    print(i)
print(xc[4])
# n = int(input('enter value:'))
#
# i =1
# while i<=n:
#     print(i)
#     i = i+1

#for loop
# name = input('enter your name')
# for ch in name:
#     print(ch)
#break and continue
l = [10, 45, 87, 2 ,5 ,22,20,44,16]
# n= int(input('enter search key'))
#
# for i in l:
#     if i == n:
#         print('found')
#         break

for i in l:
    if i%2 == 0:
        continue
        #once the condition is true. the loop will escape the blow print code
    print(i)

# for loop
l = [10, 3, 34, 65, 90, 12, 36, 20]
for i in l:
    if i%2 == 0:
        print(i, 'is an even value')
    else:
        print(i, 'is an odd value')
#list
l = [10, 'hello',3.5]
print(l)
l[1] = 'hi'
print(l)
l2 = l+[43,45]
l2.insert(2,'hello')
l2.append(90)
l2.extend(['hi there',000.3])
print(l2)
del(l2[5])
print(l2)
l3 = l2[2:6]
print(l3)
my_str = 'f,m,e,q,a,n,e'
str = my_str.split(",")
print(str)
print(len(str))
str.sort()
print(str)
str.reverse()
print(str)
my_num = '10,20,11,9,3,6,4,8'
num = my_num.split(',')
print(num)

l10= [10, 45, 87, 2 ,5 ,22,20,44,16]
print(sum(l10))
print(min(l10))
print(max(l10))
print( 45 in l10)
print( 45 not in l10)