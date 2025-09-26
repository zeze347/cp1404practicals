name = input("Enter name:")
menu = """(H)ello
(G)oodbye
(Q)uit"""
print(menu)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello",name)
    elif choice == "G":
        print("Goodbye",name)
    else:
        print("invalid message")
    print(menu)
    choice = input(">>> ").upper()
print("Finshed.")