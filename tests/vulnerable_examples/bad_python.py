import hashlib

password = "admin123"

user_input = input("Enter code: ")
eval(user_input)

exec("print('unsafe')")

hashlib.md5(b"password").hexdigest()

api_key = "super-secret-api-key"

github_token = "github_pat_12345678901234567890"

aws_key = "AKIA1234567890ABCDEF"