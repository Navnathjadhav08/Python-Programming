#for python string is immutable and no char data type are  there
# using format methot we change the str with some info like output,variable

name = "Nath"
age = 20

print('Name of founder is {0} and its age is {1}'.format(name,age))
print('Name of founder is {} and its age is {}'.format(name,age))

"""How It WorksA string can use certain specifications and subsequently, the format
method can be called to substitute those specifications with corresponding arguments
to the format method.
"""

# decimal (.) precision of 3 for float '0.333'
print ('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print ('{name} wrote {book}'.format(name='Swaroop',
 book='A Byte of Python'))