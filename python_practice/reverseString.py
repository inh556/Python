# Similarly, you can use string[x:y:2] to get the substring with characters x, x+2, x+4

# means from string[x] ending to string[4] (not included) step size is 2

# like the example 1 below

# ... or string[y:x:-1] to get a reversed part of a string (where y > x).
# With a for loop, another way to accomplish a decreasing range is reversed(range(x, y))
#  which goes from y-1 to x in decreasing order.
string = 'wolaizidalaoyuandedifang'
# example 1
print(string[2:10:2])

# example 2
print(string[24:0:-1]) # result gnafidednauyoaladizialo not include first letter 'w'

# example 3 result gnafidednauyoaladizialow
for x in range(len(string)-1,-1,-1):  # print all letter from the last to first
     print(string[x], end = '')
     
# example 4  result gnafidednauyoaladizialow; same as example 3
for x in string[::-1]:
     print(x, end = '')
     
# same as example 3 & 4
for x in reversed(string):
           print(x, end='')