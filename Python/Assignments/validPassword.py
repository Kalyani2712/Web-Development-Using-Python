def check_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "@$!%*?&"

    length = 0
    for char in password:
        length += 1
        if 'A' <= char <= 'Z':
            has_upper = True
        if 'a' <= char <= 'z':
            has_lower = True
        if '0' <= char <= '9':
            has_digit = True
        for s in special_chars:
            if char == s:
                has_special = True

    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Valid Password"
    else:
        return "Invalid Password"

# Taking user input
user_password = input("Enter your password: ")
print(check_password(user_password))

#   Output:
#   Enter your password: Abc@1234
#   Valid Password
#   Enter your password: abc123
#   Invalid Password