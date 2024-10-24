# importing the built in random library
import random


# the menu function to choose difficulty
def displayMenu():
    print("\nWelcome to Asian Math Games\n")
    print("1. Easy")
    print("2. Intermidiate")
    print("3. Asian")
    level = int(input("\nSelect a difficulty level 1-3: "))
    return level

#  function to give numbers by using random
def randomInt(level):
    if level == 1:  # single digets for ez
        return random.randint(1, 9)
    elif level == 2:  # double digits for intermediatt
        return random.randint(10, 99)
    elif level == 3:  # the last one is hard
        return random.randint(1234, 9999)

# using random.choice to choose 
def decideOperation():
    return random.choice(['+', '-'])

# functuion to make the question
def displayProblem(num1, num2, operation):
    print(f"{num1} {operation} {num2} = ", end="")
    answer = int(input())
    return answer

# is the answer correct function
def isCorrect(num1, num2, operation, answer):
    correct_answer = num1 + num2 if operation == '+' else num1 - num2
    if answer == correct_answer:
        print("Epico")
        return True
    else:
        print("\n Ahah... no")
        print("""
⣠⣀⣤⣶⣶⣶⣶⣤⣤⣤⣤⣄⡀⠀⠀⠀⢀⣀⣀⣤⣤⣤⣶⣶⣶⣶⣬⣒⢦⡀
⡾⠛⠉⠉⢀⣀⣈⣉⣉⣉⣻⠛⠁⠀⠀⠀⠀⠙⢛⣛⣉⣉⣉⣉⣀⠀⠉⠙⠻⢮
⠀⠀⣀⠴⢲⣶⣶⣶⠶⡦⠄⢷⡄⠀⠀⠀⠀⣼⠃⠴⡶⢶⣶⣶⢶⠲⢤⡀⠀⠀
⠀⠘⠓⠤⠼⠿⠿⠿⠥⠽⠄⠘⠀⠀⠀⠀⠀⠘⠂⠼⠥⠽⠿⠿⠿⠤⠖⠛⠀⠀

            wrong

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⡞⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⡤⠤⠶⠞⠋⠁⠀⠀⣸⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀  
              """)
        return False


# function to calculate and grade your scores
def displayResults(score):
    print(f"\nYour final score is: {score} out of 100")
    if score >= 90:
        print("Rank: Asian")
    elif score >= 80:
        print("Rank: A")
    elif score >= 70:
        print("Rank: B")
    elif score >= 60:
        print("Rank: C")
    else:
        print("Rank: F")

# quiz function
def quiz():
    level = displayMenu()
    score = 0
    
    for i in range(10):
        num1 = randomInt(level)
        num2 = randomInt(level)
        operation = decideOperation()

        # First attempt
        answer = displayProblem(num1, num2, operation)
        if isCorrect(num1, num2, operation, answer):
            score += 10
        else:
            # Second attempt
            print("Try again: ", end="")
            answer = int(input())
            if isCorrect(num1, num2, operation, answer):
                score += 5
    
    displayResults(score)

# Main program loop
def main():
    play_again = 'y'
    while play_again.lower() == 'y':
        quiz()
        play_again = input("\nWould you like to play again? (y/n): ")












if __name__ == "__main__":
    main()
