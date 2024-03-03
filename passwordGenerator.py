import string
import random
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digit=string.digits
symbol=string.punctuation

lower_len=int(input("Enter the no of lower case letters :"))
upper_len=int(input("Enter the no of upper case letters :"))
digit_len=int(input("Enter the no of digits letters :"))
symbol_len=int(input("Enter the no of symbols letters :"))

pwd_len=lower_len+upper_len+digit_len+symbol_len
print(pwd_len)
pwd_choices=random.choices(lower,k=lower_len)+random.choices(upper,k=upper_len)+random.choices(digit,k=digit_len)+random.choices(symbol,k=symbol_len)

random.shuffle(pwd_choices)
password="".join(pwd_choices)

print("THE PASSWORD IS : "+password)