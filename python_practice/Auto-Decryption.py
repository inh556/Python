def getGoodness(decodedString):
   goodness = 0
   for l in decodedString:
      if l == ' ':
         continue
      else:
         goodness += letterGoodness[ord(l)-65]
   return goodness
def decode(encodedMessage,i):
   decodedString = ''
   for l in encodedMessage:   
      if 90 >= ord(l) >= 65+i:
         decodedString = decodedString + chr(ord(l)- i)
      
      elif 65+i-1 >= ord(l) >= 65 :
         decodedString = decodedString + chr(90 - (65+i-1) + ord(l))
      else:
         decodedString += ' '
   return decodedString       

letterGoodness = [0.0817, 0.0149,
	                  0.0278, 0.0425, 0.127, 0.0223,
	                  0.0202, 0.0609, 0.0697, 0.0015,
	                  0.0077, 0.0402, 0.0241, 0.0675,
	                  0.0751, 0.0193, 0.0009, 0.0599,
	                  0.0633, 0.0906, 0.0276, 0.0098,
	                  0.0236, 0.0015, 0.0197, 0.0007]
encodedMessage = input()
goodnessList = []
for i in range(1,27):
   goodnessList.append(getGoodness(decode(encodedMessage,i)))

print(decode(encodedMessage, goodnessList.index(max(goodnessList))+1))