import string
import string, random


upper = string.ascii_uppercase
lower = string.ascii_lowercase
digit = string.digits
punc = string.punctuation

userInput = int(input("Enter the length of the password: "))
_password = ""

for i in range(int(userInput/4)):
  password = random.choices(upper)+random.choices(lower)+random.choices(digit)+random.choices(punc)
  print(password)
  _password = _password + "".join(password)

print(_password)
len(_password)
