import re
text ='Hi, I am Shirley Hilton. I am his wife.'
m = re.findall(r'hi', text)
if m:
    print m

else:
    print'not match'
print '________________________'

text ='Hi, I am Shirley Hilton. I am his wife.'
m = re.findall(r'\bHi\b', text)
if m:
    print m

else:
    print'not match'
print '________________________'


text ='Hi, I am Shirley Hilton. I am his wife. I am high'
m = re.findall(r'[Hh]i', text)
if m:
    print m

else:
    print'not match'
