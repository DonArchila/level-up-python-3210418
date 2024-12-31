import time
import random
import sys
import os


def main():
    print("Welcome to the waiting game \n")
    start_game()
def start_game():
    # Generate a random number between 2 and 4
    wait_time = random.randint(2, 4)

    print(f"Your task is to wait for {wait_time} seconds\n")

    # Start a timer after user presses enter
    input("Press Enter to start the timer\n")
    start_time = time.time()

    # Count seconds elapser after user presses enter again
    input("Press enter again after you have waited for the required time")  
    end_time = time.time()

    # Calculate the time taken
    elapsed_time = round(end_time - start_time)

    # Check if the user waited for the required time
    if elapsed_time == wait_time:
        print("Congratulations! You waited for the correct amount of time")
    # Check if the user was too slow
    if elapsed_time > wait_time:
        print(f"You waited for {elapsed_time} seconds.  That's {elapsed_time - wait_time} seconds too long")
    # Check if the user was too fast
    if elapsed_time < wait_time:
        print(f"You waited for {elapsed_time} seconds.  That's {wait_time - elapsed_time} seconds too short")

    while True:
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again == "yes":
            start_game()
        elif play_again == "no":
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'\n")
if __name__ == "__main__":
    main()