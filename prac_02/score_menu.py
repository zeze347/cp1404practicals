def main():
    menu = """G - Get a valid score
    P - Print result 
    S - Show stars
    Q - Quit"""
    score = get_valid_score()
    print(menu)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            judgment_result(score)
            print(judgment_result(score))
        elif choice == "S":
            print_star(score)
        else:
            print("Invalid choice.")
        print(menu)
        choice = input(">>>").upper()
    print("Thank you.")

def get_valid_score():
    score = int(input("Enter your score: "))
    while score < 0 or score > 100:
        score = int(input("Please enter a valid score: "))
    return score

def judgment_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_star(score):
    print("*" * score)

main()