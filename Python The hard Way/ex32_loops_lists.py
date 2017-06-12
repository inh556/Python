# list is a good way to store the result of a loop

the_count = [1,2,3,4,5]
fruits = ['apples', 'aoanges','pears','apricots']
change = [1,'pennies', 2,'dimes',3,'quarters']

for number in the_count:
	print "This is the count %d" % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit

for i in change:
	print "I got %r" %i

elements = []

for i in range(0,6):
	print "Adding %d to the list." % i
	elements.append(i)

for i in elements:
	print "Element was: %d" % i

elements[0] = 100
print elements
print elements.pop(-1)
print min(elements)
print len(elements)
elements.remove(3)
print elements

