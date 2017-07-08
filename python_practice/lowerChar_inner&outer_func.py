def lowerChar(char):
   if ord(char) >= 65 and ord(char) <= 90:
      return chr(ord(char) + 32)
   else:
      return char
# then define lowerString(string)
def lowerString(string):
   result = ''
   leng = len(string)
   for i in range(leng):
      result =result + lowerChar(string[i])
   return result