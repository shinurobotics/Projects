# Interactive welcome screen
print("=" * 40)
print("      WELCOME TO THE STEM QUIZ!      ")
print("=" * 40)

# Personalized user greeting
user_name = input("Please enter your name: ").strip().title()
print(f"\nHello, {user_name}! Let's test your STEM knowledge with 5 questions.\n" + "-" * 40)

score = 0

# Question 1
print("Question 1: What is the chemical symbol for gold?")
print("A) Ag\nB) Au\nC) Pb\nD) Fe")
ans1 = input("Your answer (A/B/C/D): ").strip().lower()
if ans1 == 'b':
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer was B (Au).\n")

# Question 2
print("Question 2: Which planet is known as the Red Planet?")
print("A) Venus\nB) Saturn\nC) Mars\nD) Jupiter")
ans2 = input("Your answer (A/B/C/D): ").strip().lower()
if ans2 == 'c':
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer was C (Mars).\n")

# Question 3
print("Question 3: What is the powerhouse of the cell?")
print("A) Nucleus\nB) Ribosome\nC) Mitochondria\nD) Golgi apparatus")
ans3 = input("Your answer (A/B/C/D): ").strip().lower()
if ans3 == 'c':
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer was C (Mitochondria).\n")

# Question 4
print("Question 4: What gas makes up the majority of Earth's atmosphere?")
print("A) Oxygen\nB) Carbon Dioxide\nC) Nitrogen\nD) Hydrogen")
ans4 = input("Your answer (A/B/C/D): ").strip().lower()
if ans4 == 'c':
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer was C (Nitrogen).\n")

# Question 5
print("Question 5: What is the value of Pi rounded to two decimal places?")
print("A) 3.12\nB) 3.14\nC) 3.16\nD) 3.18")
ans5 = input("Your answer (A/B/C/D): ").strip().lower()
if ans5 == 'b':
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer was B (3.14).\n")

# Final Results
print("=" * 40)
print(f"Quiz finished, {user_name}! Your final score is: {score}/5")
print("=" * 40)
