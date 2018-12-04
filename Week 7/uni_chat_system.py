import random

"""
    Student Support Chat
    
    Validates user email address, allows them to ask questions and gives appropriate responses
"""

__author__ = "Christian Harborow"
__email__  = "u1856364@unimail.hud.ac.uk"
__date__   = "20/11/2018"


def check_domain(email, domain):
    if email.count("@") == 1 and email[0] != "@" and email[email.find("@") + 1:] == domain:
        return True
    return False


def email_username(email):
    return email[:email.find("@")]


def find_word(question, word):
    return word in question


def random_name():
    return random.choice(["Dave", "John", "Sarah", "Abbey"])


def random_answer():
    return random.choice(["Maybe", "Quite possibly", "I am unsure", "I will look into that"])


uni_domain = "pop.ac.uk"
print("Welcome to the University of Poppleton's student support chat")
user_email = input("Please enter your email address: ").lower()

if not check_domain(user_email, uni_domain):
    print("Not a valid university email address, stopping client")
else:
    print("Email address valid")
    print("You have been connected to", random_name())
    username = email_username(user_email)
    while True:
        response = input("What do you need help with " + username + "?: ").lower()
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
            print(random_answer())
        if random.random() < 0.15:
            print("Lost connection to server, stopping client")
            break
