import re
text ='Hi, I am Shirley Hilton. I am his wife.'
m = re.findall(r'hi', text)
if m:
    print m

else:
    print'not match'
print '________________________'

text ='Hi, I am Shirley Hilton. I am his wife.'
m = re.findall(r'i\S', text)
if m:
    print m

else:
    print'not match'
print '________________________'


text ='Hi, I am Shirley Hilton. I am his wife. '
m = re.findall(r'[Hh]i', text)
if m:
    print m

else:
    print'not match'
