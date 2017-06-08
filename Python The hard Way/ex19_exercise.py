import random
def goal(kick):
	save = random.choice(['left','center','right'])
	print save
	if save != kick:
		print "You lose"
	else: 
		print "Saved!"

kick = random.choice(['left','center','right'])
print kick
goal(kick)
goal('right')
