"""Generates a random number and asks the user to guess it."""
import random

def main():
    """Asks the user to guess a randomly 
    generateed number and gives feedback"""
    number = random.randint(1,100)
    while True:
        try:
            guess = int(input("Enter a guess: "))
            if guess < number:
                print("Number too low")
            elif guess > number:
                print("Number too high")
            else:
                break
        except ValueError:
            print("invalid input")
    print(f"Congratulations, you guessed the number {number}")


if __name__ == '__main__':
    main()
