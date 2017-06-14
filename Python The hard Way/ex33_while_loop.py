# while_loop 
i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	i += 1
	print "Number now: ", numbers
	print "At the bottom i is %d" % i
print "The numbers:"
for num in numbers:
	print num
print "-------------------------"

# for_loop & range()
numbers = []
for i in range(6):
	print "At the top i is %d" % i
	numbers.append(i)
	print "Number now: ", numbers
	print "At the bottom i is %d" % i
print "The numbers:"
for num in numbers:
	print num

# function
def getnumber(num):
	i = 0
	while i < num:
		print "At the top i is %d" % i
		numbers.append(i)
		i += step
		print "Number now: ", numbers
		print "At the bottom i is %d" % i
print "The numbers:"
numbers = []
num = 6
getnumber(num)
for num in numbers:
	print num
