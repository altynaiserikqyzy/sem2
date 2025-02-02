import random

def guess_the_number():
    number_to_guess = random.randint(1, 20)  
    attempts = 0 

    print("Hello! What is your name?")
    player_name = input()  

    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")

    while True:
        print("Take a guess.")
        guess = input()  
        
        try:
            guess = int(guess)  
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1 

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {player_name}! You guessed my number in {attempts} guesses!")
            break  

if __name__ == "__main__":
    guess_the_number()