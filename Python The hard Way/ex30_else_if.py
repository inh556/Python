people = 40
cars = 40
buses = 15
# if statement, if true, run it. or skip it. 
if cars >= people:
	print "We shoud take the cars."
elif cars <= people:
	print "We should not take the cars."
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."
