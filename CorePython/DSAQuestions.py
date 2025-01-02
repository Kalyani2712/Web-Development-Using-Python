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

# 1. Check if two strings have common characters
str1 = "hello"
str2 = "world"
common = not set(str1).isdisjoint(set(str2))
print(f"Do the strings have common characters? {common}")  # Output: True

# 2. Convert a list of tuples to a dictionary
lst = [("a", 1), ("b", 2), ("c", 3)]
dictionary = dict(lst)
print(f"Dictionary: {dictionary}")  # Output: {'a': 1, 'b': 2, 'c': 3}

# 3. Sort a dictionary by its values in ascending order
sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1]))
print(f"Sorted Dictionary: {sorted_dict}")  # Output: {'b': 1, 'c': 2, 'a': 3}
