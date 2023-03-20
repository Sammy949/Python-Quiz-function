score = 0
def quiz(question, answer):
    global score
    if question.lower() == answer.lower():
        print("Correct")
        score = score + 1
    else:
        print("Wrong")
        print(f"The correct answer is {answer}")

question1 = input("What is the capital of the United States of America? ")
quiz(question1, "Washington DC")

question2 = input("Who is the present ruler of England? ")
quiz(question2, "King Charles III")

print(f"Your score is {score}")
print("Thanks for checking it out. samy01.netlify.app")
