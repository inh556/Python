print "Opening the file..."
target = open('filename.txt','w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I am going to ask you for three lines."

line1 = raw_input("line1")
line2 = raw_input('line2')
line3 = raw_input('line3')
print 'I am going to write these to the file.'

target.write("%s\r%s\r%s" % (line1, line2,line3))
# target.write('\n')
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write('\n')

print 'And finally, we close it'
target.close()
