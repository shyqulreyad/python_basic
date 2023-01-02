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
y = 20
z = x < y
print(z)