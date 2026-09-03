# Welcome Screen
print("=" * 40)
print("      WELCOME TO THE STEM QUIZ!      ")
print("=" * 40)

# Personalized User Greeting
user_name = input("Please enter your name: ").strip().title()
print(f"\nHello, {user_name}! Let's test your STEM knowledge with 5 questions.\n" + "-" * 40)

# Store questions, options, and correct answers in a list of dictionaries
quiz_questions = [
    {
        "question": "Question 1: What is the chemical symbol for gold?",
        "options": "A) Ag\nB) Au\nC) Pb\nD) Fe",
        "correct": "b"
    },
    {
        "question": "Question 2: Which planet is known as the Red Planet?",
        "options": "A) Venus\nB) Saturn\nC) Mars\nD) Jupiter",
        "correct": "c"
    },
    {
        "question": "Question 3: What is the powerhouse of the cell?",
        "options": "A) Nucleus\nB) Ribosome\nC) Mitochondria\nD) Golgi apparatus",
        "correct": "c"
    },
    {
        "question": "Question 4: What gas makes up the majority of Earth's atmosphere?",
        "options": "A) Oxygen\nB) Carbon Dioxide\nC) Nitrogen\nD) Hydrogen",
        "correct": "c"
    },
    {
        "question": "Question 5: What is the value of Pi rounded to two decimal places?",
        "options": "A) 3.12\nB) 3.14\nC) 3.16\nD) 3.18",
        "correct": "b"
    }
]

score = 0

# Loop through each question automatically instead of repeating code
for item in quiz_questions:
    print(item["question"])
    print(item["options"])
    
    user_answer = input("Your answer (A/B/C/D): ").strip().lower()
    
    if user_answer == item["correct"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The correct answer was {item['correct'].upper()}.\n")

# Final Results
print("=" * 40)
print(f"Quiz finished, {user_name}! Your final score is: {score}/5")
print("=" * 40)
