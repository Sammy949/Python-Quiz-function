score = 0
def quiz(question, answer):
    global score
    if question.lower() == answer.lower():
        print("Correct")
        score = score + 1
    else:
        print("Wrong")
        print(f"The correct answer is {answer}")

question1 = input("What is my Name? ")
quiz(question1, "Samuel")

question2 = input("How old am I? ")
quiz(question2, "13")

print(f"Your score is {score}")