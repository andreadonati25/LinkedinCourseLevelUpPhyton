import re

def palindrome(text):
    rev_text = ''.join(re.findall(r'[a-z]+', text.lower()))
    inv_text = rev_text[::-1]
    return rev_text == inv_text


print(palindrome("hello world"))
print(palindrome("Go hang a salami - I'm a lasagna hog"))
print(palindrome("level"))
print(palindrome("race car"))
