# 1
def fToC(number):
   return (number-32)*5/9
def cToF(number):
   return number*9/5 + 32

string = input()
lastLetter = string[len(string)-1]
number = float(string[0:len(string)-1])
if lastLetter =='C':
   print(cToF(number),end = 'F')
if lastLetter =='F':
   print(fToC(number),end = 'C')



# 2
string = input()
lastLetter = string[len(string)-1]
number = float(string[0:len(string)-1])
if lastLetter =='C':
   print(number*9/5 + 32,end = 'F')
if lastLetter =='F':
   print((number-32)*5/9,end = 'C')
