def checkSum(li):
   sum = 0  
   for num in li:
      for n in num:
         sum = sum + int(n)  
   if sum % 10 == 0:
      return True
   else:
      return False
   
def check(S):
# delete this comment and enter your code here
   li = S.split()
   if len(S) != 19 or len(S) ==0:
      return False
   for num in li:
      if not (num.isdigit() and len(num)) ==4:
            return False
   if checkSum(li):
      return True
   else:
      return False
   
check('0000 000000000000')
check('0000 0000 0000 000')
check('2768 3424 2345 2358')
check('9384 3495 3297 0121')
check('')
check('0000 0000')
check('0123 4567 8902 4568')
check('0123 4567 89AB EFGH')
check('0 0 0 0000000000000') 
check(' 5555 5555 5555 5555')