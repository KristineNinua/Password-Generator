import random
import string

def generate_password(length = 12, use_letters = True, use_digits = True, use_symbols = True):
    if length < 8:
        raise ValueError('Password length should be at least 4 characters.')

    letter_pool = string.ascii_letters if use_letters else ''
    digit_pool = string.digits if use_digits else ''
    symbol_pool = string.punctuation if use_symbols else ''

    all_characters = letter_pool + digit_pool + symbol_pool

    if not all_characters:
        raise ValueError("At least one character set must be selected.")

    password_chars = []
    if use_letters:
        password_chars.append(random.choice(letter_pool))
    if use_digits:
        password_chars.append(random.choice(digit_pool))
    if use_symbols:
        password_chars.append(random.choice(symbol_pool))

    remaining_length = length - len(password_chars)
    password_chars += random.choices(all_characters, k=remaining_length)

    random.shuffle(password_chars)

    password = ''.join(password_chars)
    return password


print(generate_password(length=17))