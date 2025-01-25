def check_character(s, char):
    return sum(1 for c in s if c == char)

print(check_character('Order of the Phoenix', 'o'))  # Expected output: 2

