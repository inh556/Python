a = 'a'
b = 'hell'
c = True and a or b
print c
d = False and a or b
print d
 
a = ''
b = 'hell'
c = True and a or b
print c
d = False and a or b
print d

a = ''
b = 'hell'
c = True and [a ]or [b]
print c
d = False and [a] or [b]
print d
 

a = ""
b = "hell"
c = (True and [a] or [b])[0]
print c
