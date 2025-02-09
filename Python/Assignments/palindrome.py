def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

string = input("Enter a string: ")
print(is_palindrome(string))
# Output:
# Enter a string
# madam
# True
# Enter a string
# hello
# False