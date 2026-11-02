print("    !WELCOME TO QUIZE GAME!")

questions=("How many Element here in periodic table?: ",
           "What is the national colour?: ",
           "What is the national Bird?: ",
           "What is the national Animal?: ")

options=(("A. 110","B. 114","C. 118","D. 120"),
         ("A. Red ","B. Blue","C. Green","D. White"),
         ("A. Parrot","B. Eagle","C. Dove","D. Kingfisher"),
         ("A. Tiger","B. Lion","C. Leoperd","D. Snake"))

answers=("C", "D", "B", "B")
guesses=[]
score=0
question_num=0



for question in questions:
    print("-------------------------------")
    print(question)

    for option in options [question_num]:
        print(option)

    guess=input("Enter(A, B, C, D): ").upper()
    guesses.append(guess)

    if guess== answers[question_num]:
        score +=1
        print("COREECT!")
    else:
        print("INCORECCET!")
        print(f"{answers[question_num]} is the coreccet answer.")

    question_num +=1

print("---------------------------")
print("          RESULTS          ")
print("---------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score=int(score/len(questions)*100)
print(f"Your Score is: {score}%")