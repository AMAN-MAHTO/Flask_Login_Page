import string
s=input("Enter string: ")

#removing all special character or extra space
#making string all character lower
spacial_char=string.punctuation
for z in spacial_char:
    s=s.replace(z,"")
s=s.lower().replace(" ","")

def ispalindrome(s):
    return s == s[::-1]

if ispalindrome(s):
    print("String is a Palindrome")
else:
    print('String is not a Palindrome')

# another way
# l=len(s)  # l is the no. of charecters
# rindex= l-1  
# index=0
# while index <= (l-1)/2:
#     if s[index]==s[rindex]:
#         index+=1
#         rindex-=1
#     else:
#         print('String is not a Palindrome')
#         break
# else:
#     print('String is a Palindrome')