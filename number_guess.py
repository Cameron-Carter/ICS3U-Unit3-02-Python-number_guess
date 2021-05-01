#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on April 2021
# This program lets the user guess a number from 1-10

import constants


def main():
    # This function lets the user guess a number from 1-10

    # Input
    guessed_number = int(input("Guess a number from 1-10: "))

    # Process
    if guessed_number == constants.ANSWER:
        print("\nCorrect! You guessed it!")
    if guessed_number != constants.ANSWER:
        print("\nIncorrect! You guessed wrong.")

    # Output
    print("\nDone.")


if __name__ == "__main__":
    main()
