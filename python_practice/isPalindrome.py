def isPalindrome(s):
    for i in range(len(s)/2):
        if not s[i] == s[len(s)-i-1]:
            return False
            
    return True
s = 'oorroo'
p = isPalindrome(s)
print(p)