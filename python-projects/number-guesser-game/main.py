import random

def generate_random_number():
    secret_number = random.randint(1, 100)

    return secret_number
    
def main():
    print("Welcome to the Number Guesser Game!")
    print("I have selected a random number between 1 and 100.")

    # generate random number
    secret_number = generate_random_number()

    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            user_input = input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess or q to exit: ")
            if user_input.lower() == 'q':
                print("Thanks for playing!")
                break
            guess = int(user_input)

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break

        if attempts == max_attempts:
            print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.")
            break

if __name__ == "__main__":
    main()