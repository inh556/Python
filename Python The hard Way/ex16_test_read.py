from sys import argv

script, filename = argv

text = open(filename)
data = text.read()
print data
text.close()
