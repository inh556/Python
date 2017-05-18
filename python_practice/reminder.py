# a number within 1000 divided by 3 or 5 or 7, the reminder of them all is 2.

for i in range(1000):
    #if i %3 ==2 and i %5 ==2 and i % 7 ==2:
    if i % 105 ==2:
        print i
