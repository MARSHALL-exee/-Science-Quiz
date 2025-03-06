import random

print("Welcome to my science quiz")

# Ask the user for their name
user_name = input("What is your name? ")

# Ask the user if they want to play
playing = input(f"Do you want to play, {user_name}? ")

# If the user does not want to play, exit the program
if playing.lower() != "yes":
    quit("Okay, maybe next time!")

print("Okay! Let's play :)")

# Dictionary of science-related questions and their correct answers
questions = {
    "What planet is known as the Red Planet?": "mars",
    "What is the chemical symbol for water?": "h2o",
    "What gas do plants absorb from the atmosphere?": "carbon dioxide",
    "What is the hardest natural substance on Earth?": "diamond",
    "What is the speed of light?": "299792458 meters per second",
    "What is the powerhouse of the cell?": "mitochondria",
    "What is the chemical symbol for gold?": "au",
    "What is the largest planet in our solar system?": "jupiter",
    "What force keeps us on the ground?": "gravity",
    "What is the boiling point of water at sea level?": "100 degrees celsius"
}

# Set to keep track of asked questions to avoid repetition
asked_questions = set()
# Dictionary to store user's answers
user_answers = {}

# Variables to count correct and incorrect answers
correct_count = 0
incorrect_count = 0

# Loop to ask 5 random questions
for _ in range(5):
    # Select a random question and answer from the dictionary
    question, answer = random.choice(list(questions.items()))
    # Ensure the question has not been asked before
    while question in asked_questions:
        question, answer = random.choice(list(questions.items()))
    asked_questions.add(question)
    
    # Ask the user the question and store their answer
    user_answer = input(question + " ")
    user_answers[question] = user_answer
    # Check if the user's answer is correct
    if user_answer.lower() == answer:
        print("Correct!")
        correct_count += 1
    else:
        print("Incorrect!")
        incorrect_count += 1

# Print a summary of the user's answers and the correct answers
print("\nSummary of your answers:")
for question, user_answer in user_answers.items():
    correct_answer = questions[question]
    print(f"Q: {question}")
    print(f"Your answer: {user_answer}")
    print(f"Correct answer: {correct_answer}")
    print()

# Print the total number of correct and incorrect answers
print(f"You answered {correct_count} questions correctly.")
print(f"You answered {incorrect_count} questions incorrectly.")

# Print a final message based on the user's performance
if correct_count == 5:
    print(f"Hurrah, {user_name}! You won!")
else:
    print(f"Better luck next time, {user_name}.")