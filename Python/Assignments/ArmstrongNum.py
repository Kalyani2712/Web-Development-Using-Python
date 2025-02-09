num = int(input("Enter a number: "))
order = len(str(num))
sum_of_digits = sum(int(digit) ** order for digit in str(num))

print(num == sum_of_digits)
# Output: Enter a number: 153
# True
# Enter a number: 33
# False