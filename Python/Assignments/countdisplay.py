string = "Welcome to python Training"
vowels = "aeiouAEIOU"
vowel_count = {char: string.count(char) for char in vowels if char in string}

print(vowel_count)
