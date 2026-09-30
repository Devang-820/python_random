
questions = (
    "Which symbol is used to assign a value to a variable?",
    "Which data type is used to store True or False?",
    "Which method adds an item to the end of a list?",
    "Which loop is best when you don't know how many times you need to repeat?",
    "What does len() return?",
    "Which symbol is used for the remainder operator?",
    "Which collection does NOT allow duplicate values?",
    "What is the index of the first item in a Python list?",
    "Which keyword is used to create a condition?",
    "What does input() return by default?"
)

options = (
    ("a. ==", "b. =", "c. !=", "d. +="),
    ("a. int", "b. str", "c. bool", "d. float"),
    ("a. add()", "b. insert()", "c. append()", "d. push()"),
    ("a. for", "b. while", "c. if", "d. print"),
    ("a. The last item", "b. Number of items", "c. The largest item", "d. The data type"),
    ("a. /", "b. //", "c. %", "d. **"),
    ("a. List", "b. Tuple", "c. Set", "d. String"),
    ("a. 0", "b. 1", "c. -1", "d. 2"),
    ("a. when", "b. check", "c. if", "d. condition"),
    ("a. int", "b. float", "c. string", "d. bool")
)

answers = ("b", "c", "c", "b", "b", "c", "c", "a", "c", "c")

guesses = []
score = 0
questions_num = 0

for question in questions:

    print("---------------")
    print(question)

    for option in options[questions_num]:
        print(option)

    guess = input("Enter (a, b, c, d): ").lower()
    guesses.append(guess)

    if guess == answers[questions_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[questions_num]} is the correct answer")

    questions_num += 1

print("---------------")
print(f"Your score is {score}/{len(questions)}")