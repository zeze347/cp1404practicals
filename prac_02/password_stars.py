def get_password():
    password = input("Enter your password: ")
    return password

def check_password(password):
    while len(password) <= 10:
        print("*" * len(password))
        password = input("Enter your password: ")

password = get_password()
check_password(password)

