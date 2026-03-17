# ============================================================
# AI & Technology Quiz Game
# Author: Arpit Pareek | Shrimadhopur, Rajasthan, India
# Purpose: Demonstrates lists, functions, loops, conditionals
#          and data analysis in Python
# Topic: Artificial Intelligence & Cognitive Science
# ============================================================

import random
import time

# ---- QUIZ DATA ----
questions = [
    {
        "question": "What does AI stand for?",
        "options": ["A) Automatic Intelligence", "B) Artificial Intelligence", "C) Advanced Integration", "D) Automated Input"],
        "answer": "B",
        "explanation": "AI = Artificial Intelligence — machines that simulate human thinking!"
    },
    {
        "question": "Which programming language is most popular for AI?",
        "options": ["A) Java", "B) C++", "C) Python", "D) Ruby"],
        "answer": "C",
        "explanation": "Python is #1 for AI due to its simple syntax and powerful libraries!"
    },
    {
        "question": "What is 'Machine Learning'?",
        "options": [
            "A) Machines fixing themselves",
            "B) Computers learning from data without being explicitly programmed",
            "C) Programming a robot",
            "D) A type of computer virus"
        ],
        "answer": "B",
        "explanation": "Machine Learning allows computers to learn patterns from data!"
    },
    {
        "question": "What is 'Cognitive AI'?",
        "options": [
            "A) AI that only does math",
            "B) AI that understands human thinking and behaviour",
            "C) AI in video games",
            "D) AI that controls robots"
        ],
        "answer": "B",
        "explanation": "Cognitive AI focuses on understanding human mind, decisions, and behaviour!"
    },
    {
        "question": "What is 'Neural Network' in AI?",
        "options": [
            "A) Computer networks",
            "B) A system inspired by the human brain",
            "C) Internet connection",
            "D) A type of database"
        ],
        "answer": "B",
        "explanation": "Neural networks are inspired by how neurons work in the human brain!"
    },
    {
        "question": "What does 'Deep Learning' do?",
        "options": [
            "A) Makes computers think deeply",
            "B) Uses multiple layers of neural networks to learn complex patterns",
            "C) A meditation app for computers",
            "D) Studies ocean data"
        ],
        "answer": "B",
        "explanation": "Deep Learning uses layered neural networks to process complex data like images and speech!"
    },
    {
        "question": "Which country is a world leader in AI and Robotics research?",
        "options": ["A) India", "B) Brazil", "C) Japan", "D) Canada"],
        "answer": "C",
        "explanation": "Japan leads globally in robotics, human-computer interaction, and AI research!"
    },
    {
        "question": "What is 'Natural Language Processing' (NLP)?",
        "options": [
            "A) Learning new languages",
            "B) AI understanding and processing human language",
            "C) Nature photography",
            "D) Scientific word processing"
        ],
        "answer": "B",
        "explanation": "NLP enables AI to understand, interpret, and generate human language!"
    },
    {
        "question": "What is a 'chatbot'?",
        "options": [
            "A) A social media app",
            "B) An AI program that simulates human conversation",
            "C) A type of video game",
            "D) A messaging service"
        ],
        "answer": "B",
        "explanation": "Chatbots use NLP and AI to simulate human-like conversations!"
    },
    {
        "question": "What is 'Recursion' in programming?",
        "options": [
            "A) Repeating a loop forever",
            "B) A function that calls itself to solve smaller problems",
            "C) A type of database query",
            "D) Copy-pasting code"
        ],
        "answer": "B",
        "explanation": "Recursion = a function calling itself! Used in algorithms like Fibonacci and Factorial."
    }
]

# ---- FUNCTIONS ----

def display_welcome():
    print("\n" + "="*55)
    print("     AI & TECHNOLOGY QUIZ GAME")
    print("     Built by Arpit Pareek | Rajasthan, India")
    print("="*55)
    print("Test your knowledge about AI, Python, and Technology!")
    print("="*55)

def ask_question(q, number, total):
    print(f"\nQuestion {number}/{total}:")
    print(f"  {q['question']}")
    print()
    for option in q['options']:
        print(f"  {option}")
    print()
    
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        print("Please enter A, B, C, or D only!")

def check_answer(user_answer, correct_answer, explanation):
    if user_answer == correct_answer:
        print("\n✅ CORRECT! Well done!")
        print(f"   {explanation}")
        return True
    else:
        print(f"\n❌ Wrong! Correct answer was: {correct_answer}")
        print(f"   {explanation}")
        return False

def show_score(score, total):
    percentage = (score / total) * 100
    print("\n" + "="*55)
    print("           QUIZ COMPLETE! FINAL RESULTS")
    print("="*55)
    print(f"  Score: {score}/{total} ({percentage:.1f}%)")
    print()
    
    # Grade based on score
    if percentage == 100:
        grade = "🏆 PERFECT SCORE! Outstanding!"
    elif percentage >= 80:
        grade = "🥇 Excellent! You know AI well!"
    elif percentage >= 60:
        grade = "🥈 Good job! Keep learning!"
    elif percentage >= 40:
        grade = "🥉 Not bad! Study more about AI!"
    else:
        grade = "📚 Keep studying — you'll get there!"
    
    print(f"  Grade: {grade}")
    print("="*55)
    
    # Data Analysis
    print("\n📊 PERFORMANCE ANALYSIS:")
    print(f"  Correct answers:   {score}")
    print(f"  Incorrect answers: {total - score}")
    print(f"  Accuracy:          {percentage:.1f}%")
    
    if percentage < 70:
        print("\n💡 TIP: Study more about:")
        print("  - Artificial Intelligence basics")
        print("  - Machine Learning and Deep Learning")
        print("  - Python programming concepts")
        print("  - Cognitive AI and NLP")

def play_quiz(shuffle=True):
    display_welcome()
    
    name = input("\nEnter your name: ").strip()
    if not name:
        name = "Player"
    
    print(f"\nWelcome, {name}! Let's begin...")
    time.sleep(1)
    
    # Shuffle questions for variety
    quiz_questions = questions.copy()
    if shuffle:
        random.shuffle(quiz_questions)
    
    score = 0
    total = len(quiz_questions)
    
    for i, question in enumerate(quiz_questions, 1):
        user_answer = ask_question(question, i, total)
        
        if check_answer(user_answer, question['answer'], question['explanation']):
            score += 1
        
        time.sleep(0.5)
    
    show_score(score, total)
    
    print(f"\nThank you for playing, {name}!")
    print("Keep learning about AI — the future belongs to those who understand it!")
    print("\n- Arpit Pareek | Aspiring AI Researcher | Rajasthan, India")

def main():
    play_quiz()
    
    while True:
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again in ['yes', 'y']:
            play_quiz()
        elif again in ['no', 'n']:
            print("\nGoodbye! Keep exploring AI! 🚀")
            break
        else:
            print("Please enter yes or no.")

if __name__ == "__main__":
    main()
