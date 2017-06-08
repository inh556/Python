# this one is like scripts with argv

def print_two(*args):
	arg1,arg2 = args
	print "arg1: %r, arg2:%r" %(arg1,arg2)

# that *args is actually pointless, we can do this

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2:%r" %(arg1,arg2)
	
# this one takes one argument

def print_one(arg1):
	print "arg1:%r" % arg1

def print_none():
	print "I got nothin."

print_two("zed","shaw")
print_two_again("zed","shaw")
print_one("first!")
print_none()