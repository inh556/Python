needle = input()
haystack = input()
leng1 = len(needle)
leng2 = len(haystack)
counter = 0
i = 0
while i + leng1 <= leng2:     
     if haystack[i:i+leng1] == needle:
        counter +=1
     i =i +1
print(counter)