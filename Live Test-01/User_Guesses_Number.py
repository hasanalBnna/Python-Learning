import random

def user_guesses_number():
    number_to_guess = random.randint(1, 100)
    print("The computer has selected a number between 1 and 100.")
    
    while True:
        try:
            user_guess = int(input("Guess the number (1 to 100): "))
            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            if user_guess < number_to_guess:
                print("Too low!")
            elif user_guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Correct! The number was {number_to_guess}.")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

def computer_guesses_number():
    print("Think of a number between 1 and 100 (input is provided secretly).")
    low = 1
    high = 100
    attempts = 0
    
    while True:
        attempts = attempts + 1
        computer_guess = (low + high) // 2
        print(f"Computer guesses: {computer_guess}")
        
        feedback = input("Your feedback (h for too high, l for too low, c for correct): ").strip().upper()
        
        if feedback == 'h':
            high = computer_guess - 1
        elif feedback == 'l':
            low = computer_guess + 1
        elif feedback == 'c':
            print(f"Computer guessed your number in {attempts} tries!")
            break
        else:
            print("Invalid feedback. Please enter h, l, or c.")

def display_menu():
    print("\nChoose an option:")
    print("1. You guess the number (computer selects)")
    print("2. Computer guesses your number")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            user_guesses_number()
        elif choice == '2':
            computer_guesses_number()
        elif choice == '3':
            print("Good luck!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
