# grade 
def grade(score):
    if score > 100 or score < 0:
        print("invalid input. enter from (0-100)")
    elif score >= 90:
        print("A")
    elif score >= 75:
        print("B")
    elif score >= 60:
        print("C")
    else:
        print("F")
score=int(input("enter the score(0-100):"))
grade(score)