import time
import random
import sys
import os


def main():
    print("Welcome to the waiting game!")
    start_game()
def start_game():
    # Generate a random number between 2 and 4
    wait_time = random.randint(2, 4)

    print(f"\nYour target time is {wait_time} seconds")

    # Start a timer after user presses enter
    input(" ---Press Enter to Begin---")
    start_time = time.time()

    # Count seconds elapser after user presses enter again
    input(f"\n...Press Enter again after {wait_time} seconds...")  
    end_time = time.time()

    # Calculate the time taken
    elapsed_time = end_time - start_time

    print(f"\nElapsed time: {elapsed_time} seconds")

    # Check if the user waited for the required time
    if round(elapsed_time) == wait_time:
        print("\nCongratulations! You waited for the correct amount of time")
    
    # Check if the user was too slow
    elif elapsed_time > wait_time:
        print(f"({elapsed_time - wait_time} seconds too long)")
    
    # Check if the user was too fast
    else:
        print(f"({wait_time - elapsed_time} seconds too fast)")

    while True:
        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again == "yes":
            start_game()
        elif play_again == "no":
            print("\nThanks for playing!")
            sys.exit()
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'\n")
if __name__ == "__main__":
    main()