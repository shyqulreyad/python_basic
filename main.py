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

lx = True
ly = False
lz = True
lm = False
print (lx and ly)
print (lx and lz)
print (lx or lz)
print (not lx)
print (ly and lm)

