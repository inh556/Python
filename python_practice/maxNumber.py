print 'input three numbers'
num1 = input()
num2 = input()
num3 = input()
if num1 > num2:
    if num1 > num3:
        print num1
    else:
        print num3
if num1 < num2:
    if num2 > num3:
        print num2
    else:
        print num3
