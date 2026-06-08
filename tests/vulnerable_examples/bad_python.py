import hashlib
import os
import pickle
import subprocess

password = "admin123"

user_input = input("Enter code: ")
eval(user_input)

exec("print('unsafe')")

hashlib.md5(b"password").hexdigest()

api_key = "super-secret-api-key"

github_token = "github_pat_12345678901234567890"

aws_key = "AKIA1234567890ABCDEF"

subprocess.run(user_input, shell=True)

os.system(user_input)

pickle.loads(user_input)

query = "SELECT * FROM users WHERE username = '" + user_input + "'"

jwt_secret = "super-secret-jwt-key"