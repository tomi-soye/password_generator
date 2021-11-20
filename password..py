# Import relevant modules

import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%=:?./|~>'*,()<"

character = letters + letters.lower() + numbers + symbols
max_length = 15

password = "".join(random.sample(character, max_length))

print("Password:", password)