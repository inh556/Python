def count_times():
	li = []
	while True:
	   line = input()
 	  words = line.split()
 	  for word in words:
 	     li.append(word.lower())
 	  if line.endswith('###'):
  	    li.pop()
   	   break

	num = [0]*len(li)
	for word in li:
	   num[li.count(word)-1]=word

	for i in num[::-1]:
 	  if not i== 0:
  	  	print(i)
   	    break

count_times()