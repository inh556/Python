import random
def get_white_balls():
	return random.sample(range(1,70),5)

def get_red_ball():
	return random.randint(1,26)


for i in range(5):
	list1 = get_white_ball()	
	list1.sort()
	list1.append(get_red_ball())
	print(list1)