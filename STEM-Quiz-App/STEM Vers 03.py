import random

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
        "question": "Question: What is the chemical symbol for gold?",
        "options": "A) Ag\nB) Au\nC) Pb\nD) Fe",
        "correct": "b"
    },
    {
        "question": "Question: Which planet is known as the Red Planet?",
        "options": "A) Venus\nB) Saturn\nC) Mars\nD) Jupiter",
        "correct": "c"
    },
    {
        "question": "Question: What is the powerhouse of the cell?",
        "options": "A) Nucleus\nB) Ribosome\nC) Mitochondria\nD) Golgi apparatus",
        "correct": "c"
    },
    {
        "question": "Question: What gas makes up the majority of Earth's atmosphere?",
        "options": "A) Oxygen\nB) Carbon Dioxide\nC) Nitrogen\nD) Hydrogen",
        "correct": "c"
    },
    {
        "question": "Question: What is the value of Pi rounded to two decimal places?",
        "options": "A) 3.12\nB) 3.14\nC) 3.16\nD) 3.18",
        "correct": "b"
    }
]

# Randomize the question order every time the game runs
random.shuffle(quiz_questions)

score = 0
question_number = 1

# Loop through each question automatically with randomized order
for item in quiz_questions:
    print(f"--- Question {question_number} of 5 ---")
    print(item["question"])
    print(item["options"])
    
    # Case-insensitive answer checking (.strip().lower())
    user_answer = input("Your answer (A/B/C/D): ").strip().lower()
    
    # Real-time score tracking and instant feedback
    if user_answer == item["correct"]:
        print("Correct!✅\n")
        score += 1
    else:
        print(f"Incorrect❌ .The correct answer was {item['correct'].upper()}.\n")
        
    question_number += 1

# Final Percentage Score Calculation
Percentage = (score / 5) * 100

# Performance Evaluation System
if Percentage == 100:
    performance = "Outstanding! You're a true STEM genius!"
elif Percentage >= 80:
    performance = "Great job! You have a strong grasp of STEM subjects!"
elif Percentage >= 60:
    performance = "Good effort! Keep exploring and learning STEM concepts."
else:
    performance = "Keep practicing! STEM always take time to master."

# Completion Message and Final Results
print("=" * 40)
print(f"Quiz Finished, {user_name}!")
print(f"Final Score: {score}/5 ({Percentage:}%)")
print(f"Evaluation: {performance}")
print("=" * 40)
print("Thank you for playing the STEM Quiz!")
