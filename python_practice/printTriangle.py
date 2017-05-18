print ' a number'
num = input()

for i in range(num):
    for j in range(num):
        if i >=j:
            print '*',
        else:
            print ' ',
    print


for i in range(num):
    for j in range(num):
        if j < (num-1)-i:
            print ' ',
        else:
            print '*',
    print

