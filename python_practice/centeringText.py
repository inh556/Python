width = int(input())

# delete this comment and enter your code here
while True: 
   text = input()
   if text =='END':
      break
   leng = len(text)
   p = width - leng
   if p % 2 == 0:
      print('.'*(p//2) + text + '.'* (p//2))
   else:
      print('.'*((p+1)//2)+ text + '.'*((p-1)//2))