import random
import time

print("=" * 40)
print("      WELCOME TO THE STEM QUIZ!      ")
print("=" * 40)

user_name = input("Please enter your name: ").strip().title()
print(f"\nHello, {user_name}! Let's test your STEM knowledge.\n" + "-" * 40)

# Questions organized by category
science_questions = [
    {
        "question": "What is the chemical symbol for gold?",
        "options": "A) Ag\nB) Au\nC) Pb\nD) Fe",
        "correct": "b",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": "A) Venus\nB) Saturn\nC) Mars\nD) Jupiter",
        "correct": "c",
    },
    {
        "question": "What is the powerhouse of the cell?",
        "options": "A) Nucleus\nB) Ribosome\nC) Mitochondria\nD) Golgi apparatus",
        "correct": "c",
    },
    {
        "question": "What gas makes up the majority of Earth's atmosphere?",
        "options": "A) Oxygen\nB) Carbon Dioxide\nC) Nitrogen\nD) Hydrogen",
        "correct": "c",
    },
    {
        "question": "What happens to the electrical resistance of a typical metal wire when its temperature increases??",
        "options": "A) Decreases\nB) Increases\nC) Becomes Zero\nD) Remains Constant",
        "correct": "b",
    }
]

math_tech_questions = [
    {
        "question": "What is the value of Pi rounded to two decimal places?",
        "options": "A) 3.12\nB) 3.14\nC) 3.16\nD) 3.18",
        "correct": "b",
    },
    {
        "question": "What does 'CPU' stand for in computing?",
        "options": "A) Central Process Unit\nB) Central Processing Unit\nC) Computer Power Utility\nD) Core Programming Unit",
        "correct": "b",
    },
    {
        "question": "What is the square root of 144?",
        "options": "A) 11\nB) 12\nC) 13\nD) 14",
        "correct": "b",
    },
    {
        "question": "In binary, what decimal number does '1010' represent?",
        "options": "A) 8\nB) 10\nC) 12\nD) 14",
        "correct": "b",
    },
    {
        "question": "Which simple machine is commonly used to lift heavy objects using a wheel and rope?",
        "options": "A) Lever\nB) Wedge\nC) Screw\nD) Pulley",
        "correct": "d",
    }
]

# Replay loop so you can play multiple rounds
while True:
    # 1. Choose difficulty
    print("Difficulty Levels:")
    print("1) Easy   (20s limit, 1x points)")
    print("2) Medium (12s limit, 2x points)")
    print("3) Hard   (8s limit,  3x points)")
    diff_choice = input("Choose difficulty (1/2/3): ").strip()

    if diff_choice == "2":
        difficulty_name = "Medium"
        time_limit = 12
        points_per_correct = 2
    elif diff_choice == "3":
        difficulty_name = "Hard"
        time_limit = 8
        points_per_correct = 3
    elif diff_choice == "1":
        difficulty_name = "Easy"
        time_limit = 20
        points_per_correct = 1
    else:
        print("Invalid, Try again")
        break

    # 2. Choose category
    print("\nCategories:")
    print("1) Science")
    print("2) Math & Tech")
    print("3) All STEM")
    cat_choice = input("Choose category (1/2/3): ").strip()

    if cat_choice == "1":
        category_name = "Science"
        questions = science_questions.copy()
    elif cat_choice == "2":
        category_name = "Math & Tech"
        questions = math_tech_questions.copy()
    elif cat_choice == "3":
        category_name = "All STEM"
        questions = science_questions + math_tech_questions
    else:
        print("Invalid, Try again")
        break
    
  # Keep rounds to 5 questions max
    random.shuffle(questions)
    questions = questions[:5]

    score = 0
    correct_answers = 0
    question_number = 1

    print(f"\nStarting {category_name} ({difficulty_name}) - {time_limit}s per question!\n" + "-" * 40)

    for item in questions:
        print(f"--- Question {question_number} of {len(questions)} ---")
        print(item["question"])
        print(item["options"])

        # 3. Timer system using start and end timestamps
        start_time = time.time()
        user_answer = input("Your answer (A/B/C/D): ").strip().lower()
        time_taken = time.time() - start_time

        if user_answer == item["correct"]:
            correct_answers += 1
            if time_taken <= time_limit:
                score += points_per_correct
                print(f"Correct! ✅ ({time_taken:.1f}s) +{points_per_correct} pts\n")
            else:
                half_points = points_per_correct / 2
                score += half_points
                print(f"Correct, but overtime! ⏱️ ({time_taken:.1f}s > {time_limit}s) +{half_points} pts\n")
        else:
            print(f"Incorrect ❌ ({time_taken:.1f}s). The correct answer was {item['correct'].upper()}.\n")

        question_number += 1

    # Results
    Percentage = (correct_answers / len(questions)) * 100
    print("=" * 40)
    print(f"Quiz Finished, {user_name}!")
    print(f"Correct: {correct_answers}/{len(questions)} ({Percentage:.0f}%)")
    print(f"Score: {score} pts | Difficulty: {difficulty_name} | Category: {category_name} | {Percentage}%")
    print("=" * 40)
    retry = input("Wanna Try Again?\n" "Yes or No\n").lower()
    if retry == "yes":
        continue
    else:
        break
        print(f"\nThank you for playing the STEM Quiz, {user_name}!")
