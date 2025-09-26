"""Q. 2. Write a version of a palindrome recognizer that also accepts
phrase palindromes such as : Was it a rat I saw? or Dammit, I'm mad!
Note that punctuation, capitalization, and spacing are usually ignored."""
str = "Was it a rat I saw"
str1 = "DammitImmad"
l_str1 = str1.lower()
print(l_str1)
rev_str1 = l_str1[::-1]
print(rev_str1)
print(l_str1 == rev_str1)
str2=str.strip()
l_str1 = str2.lower()
cleaned_str1 = ''.join(char for char in l_str1 if char.isalnum())
print(cleaned_str1)
rev_str1 = cleaned_str1[::-1]
print(rev_str1)
print(cleaned_str1 == rev_str1)

import re

def is_palindrome(phrase):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_phrase = re.sub(r'[^a-zA-Z0-9]', '', phrase.lower())
    return cleaned_phrase == cleaned_phrase[::-1]

# Test cases
print(is_palindrome("Was it a rat I saw"))  # Output: True
print(is_palindrome("Dammit, I'm mad!"))    # Output: True
print(is_palindrome("race a car"))          # Output: False