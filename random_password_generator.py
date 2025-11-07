import random
import string

passlen=10
charvalues=string.ascii_letters + string.digits + string.punctuation

password=""
for i in range(passlen):
    password += random.choice(charvalues)
print("Your password is:",password)