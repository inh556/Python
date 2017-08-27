totalAmount = 3100
num = 10.0
totalShare = 0.00
cost = 0.0
for i in range(1,6):
	num = num*(1.0-0.1)
	totalShare += (i*310)/num
	cost += 310*i
	print("After %d 10%% down, the NewPrice is %.3f, the averageCost is %.3f" %(i,num, cost/totalShare))