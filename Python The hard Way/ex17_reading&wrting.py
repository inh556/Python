from sys import argv
from os.path import exists
script, from_file, to_file = argv


# print "Coping from %s to %s" %(from_file, to_file)
# how to do these two on one line ?

# in_file = open(from_file)
# indata = in_file.read()
# indata = open(from_file).read()


# print "The input file is %d bytes long" % len(indata)
# print "Does the ouput file exist? %r" %(exists(to_file))
# print "Ready, hit RETURN to continue, CTR-C to abort."
# raw_input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print "Alright, all done."
# out_file.close()

#  with syntax no need to close 
with open(to_file, 'w') as out_file:
	out_file.write(open(from_file).read())
# it should be closed after running the code
open(to_file, 'w').write(open(from_file).read())
