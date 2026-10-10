questions = [
    "What is the capital of Australia?",
    "Who is known as the Father of the Nation in India?",
    "Which planet is known as the Red Planet?",
    "Which is the largest ocean on Earth?",
    "In which year did World War II end?"
]
options = [
    ("A) Sydney", "B) Melbourne", "C) Canberra", "D) Perth"),
    ("A) Jawaharlal Nehru", "B) Mahatma Gandhi", "C) Subhas Chandra Bose", "D) Bhagat Singh"),
    ("A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"),
    ("A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"),
    ("A) 1942", "B) 1945", "C) 1947", "D) 1950")
]
# Correct answers
answers = ["C", "B", "B", "D", "B"]
score=0
guesses=0
guessed=[]

for question in questions:
    print('************************')
    print(question)
    print('***********************')
    for option in options[guesses]:
        print(option)
    answer=input("Enter your answer: ").upper()
    if answer.isdigit()or answer not in ['A','B','C','D']:
        print("Invalid input")
        continue
    elif answer==answers[guesses]:
        print("Correct!!\nThe correct answer is " + answer)
        score+=5
    else:
        print("Incorrect answer\nThe correct answer is " + answer)
    guessed.append(answer)
    guesses+=1

print("**********RESULT**********")
print('Guesses : ',end='')
for guess in guessed:
    print(guess,end='')
print()
print('Answers : ',end='')
for i in answers:
    print(i,end='')
print()
print(f'your score is {score:^10.2f}')



