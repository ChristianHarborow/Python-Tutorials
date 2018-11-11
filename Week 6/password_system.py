password = input("Enter password: ")
if len(password) >= 8:
    lower = any(char.islower() for char in password)
    upper = any(char.isupper() for char in password)
    num = any(char.isnumeric() for char in password)
    other = any(not(char.isalnum()) for char in password)
    if lower and upper and num and other:
        print("Password Valid")
    else:
        print("Password Invalid")
else:
    print("Password Invalid")
