import random


def check_domain(email, domain):
    if email.count("@") != 1:
        return False
    if email[0] == "@":
        return False
    if email[email.find("@") + 1:] == domain:
        return True
    return False


def email_username(email):
    return email[:email.find("@")]

operator_names = ["Dave", "John", "Sarah", "Abbey"]
uni_domain = "pop.ac.uk"
user_email = input("Enter your email address: ")
if not check_domain(user_email, uni_domain):
    print("Email invalid, stopping client")
else:
    print("Email valid")
    print("You have been connected to", random.choice(operator_names))
    username = email_username(user_email)
    print("Hi", username + ", how can I help you?")
