import random
print 'Input numbers m & n, 1<=m<=n '
m = input('m = ')
n  = input('n = ')
if n >=m>=1:
    random_numberlist = random.sample(range(1,n+1), m)
    random_numberlist.sort()
    print random_numberlist
else:
    print 'Error, check if n >=m>=1'
