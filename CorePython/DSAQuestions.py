# 1. Check if a string is a palindrome (ignoring spaces and case)
# Program :
def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello"))  # False
print(" ---------------------------------------------------")
# 2.Check if two strings are anagrams:
# Program :
def are_anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

print(are_anagrams("Listen", "Silent"))  # Output: True
print(are_anagrams("Hello", "World"))   # Output: False

print("---------------------------------------------------")
# 3.Find the first non-repeating character in a string
# Program :
def first_non_repeating(s):
    s = s.lower()
    for char in s:
        if s.count(char) == 1:
            return char
    return None

print(first_non_repeating("swiss"))  # Output: w
print(first_non_repeating("aabbcc"))#Output:None