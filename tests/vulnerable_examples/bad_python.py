import hashlib

password = "admin123"

user_input = input("Enter code: ")
eval(user_input)

exec("print('unsafe')")

hashlib.md5(b"password").hexdigest()