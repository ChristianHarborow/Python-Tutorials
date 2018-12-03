username = input("Enter Username: ")
student_id = input("Enter Student ID: ")
poor_passwords = ("huddersfield", "justinbieber", "cheese",
                  "canalside", username, student_id)
password_1 = input("Enter Password: ")
password_2 = input("Confirm Password: ")

if password_1 == password_2 and len(password_1) in range(6, 13)\
        and not(password_1 in poor_passwords):
    print("Password Changed")
else:
    print("Password Change Failed")
