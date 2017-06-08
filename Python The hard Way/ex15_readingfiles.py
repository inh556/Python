# import module 
from sys import argv
# variable hold arguments that user will pass to script
script, filename = argv
# open the file
txt = open(filename)

print "Here is your file %r: " % filename
# read the content 
print txt.read()
txt.close()

# print "Whichi file do you wanna open?"
# filename = raw_input()

# print "The file you wanna open is: %s?" % filename
# pass the arg and open it
# txt_again = open(filename)
# print txt_again.read()
# txt_again.close()