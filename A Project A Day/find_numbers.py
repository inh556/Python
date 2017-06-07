# find all the numbers and combine them to a new string
import re
text = "aAsmr3idd42bgs7332Dlsf23219eAF 2322 29892 121 432" 
# regular expression find all the numbers which length greater equal than 1
nums = re.findall("[0-9]+",text)
# check the output
print nums
# join them together
new_str = ''.join(nums)
# check the type of new string
print type(new_str)
# print new string
print new_str