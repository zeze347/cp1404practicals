"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random
def main():
    score = float(input("Enter score: "))
    judgment_result(score)
    print(judgment_result(score))

def judgment_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"
main()
random_score = random.randint(1,100)
print(random_score)
print(judgment_result(random_score))

