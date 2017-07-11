string = ''
for char in 'SPYCODER':
   if 85 >= ord(char) >= 65:
      string = string + chr(ord(char)+ 5)
    
   if 90 >= ord(char) >= 86 :
      string = string + chr(65 + ord(char) - 86)   
print(string)