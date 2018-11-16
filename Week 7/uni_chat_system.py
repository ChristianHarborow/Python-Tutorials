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


def find_word(question, word):
    return word in question


operator_names = ["Dave", "John", "Sarah", "Abbey"]
answers = ["Maybe", "Quite possibly", "I am unsure", "I will look into that"]
uni_domain = "pop.ac.uk"
user_email = input("Enter your email address: ")
if not check_domain(user_email, uni_domain):
    print("Email invalid, stopping client")
else:
    print("Email valid")
    print("You have been connected to", random.choice(operator_names))
    username = email_username(user_email)
    print("Hi", username)
    while True:
        response = input("How can I help you?: ").lower()
        if find_word(response, "goodbye"):
            print("Stopping client")
            break
        elif find_word(response, "library"):
            print("The library is closed today")
        elif find_word(response, "wifi"):
            print("WiFi is excellent across campus")
        elif find_word(response, "deadline"):
            print("Your deadline has been extended by two working days")
        else:
            print(random.choice(answers))
        if random.random() < 0.15:
            print("Lost connection to server, stopping client")
            break
