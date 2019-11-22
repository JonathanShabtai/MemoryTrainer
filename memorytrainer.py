import random
import time


class User:
    """
    Will develop a user class to keep track of all the users using the program.
    Every user will have a unique folder with their own memory palaces and memory systems
    """
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password

class MemoryPalace:
    """
    Memory Palace class to enable constructing new palaces for users
    """
    pass


def pi_recall():
    # import sys, os
    # import curses - trying to read one character at a time

    # add try block for bad user input

    with open('pi.txt') as f:
        lines = f.readlines()

    pi = ""
    for line in lines:
        pi += line.strip()

    digits_len = int(input('Please enter how many digits do you plan to recall: '))
    segments_of_recall = int(input('How many digits would you like to recall at a time? '))

    for i in range(0, digits_len, segments_of_recall):
        digits = str(input('Enter the next digit of pi: '))
        correct = str(pi[i:(i+segments_of_recall)])
        if digits != correct:
            print(f'Error, the correct digits were: {pi[i:(i+segments_of_recall)]}')
            break
        else:
            pass # In case of a mistake, need to add options for review
def deck_recall():
    pass

def random_words():
    pass

def random_digits():

    # add try block for bad user input

    length_of_sequence = input('Please enter the length of string you wish to recall: ')

    sequence = ''

    for i in range(int(length_of_sequence)):
        j = random.randrange(0, 10, 1)
        sequence += str(j)

    print(sequence)
    print('Now recall.')
    print(len(sequence))

    segments_of_recall = int(input('How many digits would you like to recall at a time? '))

    mistakes = 0
    mistakes_list = []
    you_guessed = []
    for i in range(0, len(sequence), segments_of_recall):
        guess = input(f'Enter the next {segments_of_recall} digits. ')
        if guess == sequence[i:i+segments_of_recall]:
            print('Nice!')
        else:
            print('Keep going...')
            mistakes += 1
            you_guessed.append(guess)
            mistakes_list.append(sequence[i:i+segments_of_recall])

    print(f'You had {mistakes} segment mistakes. You got {len(sequence) - mistakes * segments_of_recall} correctly!')

    review = input('Would you like to review the mistakes? Y / N')
    if review == 'Y':
        for your_guess, correct_guess in zip(you_guessed, mistakes_list):
            print(f'You guessed {your_guess}')
            print(f'The answer was {correct_guess}')

def main():
    game = input('Would like to recall random digits, or pi? Enter pi / random: ').lower()
    if game == 'pi':
        pi_recall()
    elif game == 'random':
        random_digits()

if __name__ == '__main__':
    main()
