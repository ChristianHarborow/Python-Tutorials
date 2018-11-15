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

email = "fred@pop.ac.uk"
domain = "pop.ac.uk"
if check_domain(email, domain):
    print(email, "is valid at", domain)
else:
    print(email, "is not valid at", domain)

print("Username:" + email_username(email))
