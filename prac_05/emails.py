"""
Program: emails.py
Estimate: 20 minutes
Actual: 30 minutes
"""

def get_name(email):
    name_list = email.split("@")[0]
    parts = name_list.split(".")
    name = " ".join(parts).title()
    return name


email = input("Email:").strip()
email_to_name = {}
while email != "":
    name = get_name(email)
    get_choice = input(f"Is your name {name}? (Y/n)")
    if get_choice.upper() == "Y" or get_choice == "":
        email_to_name[email] = name
    else:
        name = input("Name:")
        email_to_name[email] = name
    email = input("Email:")
for email, name in email_to_name.items():
    print(f"{name} ({email})")
