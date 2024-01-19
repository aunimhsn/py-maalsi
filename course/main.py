from string import ascii_uppercase, ascii_lowercase

upper_lst = [*ascii_uppercase]
print(upper_lst)

# Seconde soluce
print([ord(letter) for letter in list(ascii_lowercase)])
