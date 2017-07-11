string = ''
for char in 'HUD':
   if 90 >= ord(char) >= 71:
      string = string + chr(ord(char)- 6)
    
   if 70 >= ord(char) >= 65 :
      string = string + chr(90 - 70 + ord(char))
print(string)