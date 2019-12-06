import random
import time
import os
from threading import Timer
import pandas as pd
import re


class Application:
    """
    A class used to run the application 
    Attributes: The class itself is a list, so no attributes necessary.
    Methods: menu, major, afterpractice, random_digits_with_major, pi_recall, pi_learn, random_digits, 
    """
    def __init__(self):
        pass

    def greetings(self):
        print('Welcome to my memory trainer!')
        print('The application offers practicing many aspects of training.')
        print('It can test your major system knowledge, practice random digit'
              'recall, construct a memory palace, etc... Here is the menu:')
        print('--------')

    def menu(self):
        """
        Present the main menu of the application to the user.
        """
        while True:
            print('Main menu:')
            game = input('1. Major System Practice (enter MSP) \n'
                         '2. Pi Learn (enter pi_learn) \n'
                         '3. Pi recall (enter pi) \n'
                         '4. Random digits recall (enter random)\n'
                         'quit to quit\n').lower()
            while True:
                if game == 'pi':
                    self.pi_recall()
                elif game == 'pi_learn':
                    self.pi_learn()
                elif game == 'random':
                    self.random_digits()
                elif game == 'cards':
                    d = Deck()
                    d.deck_recall()
                elif game == 'r':
                    self.review()
                elif game == 'test':
                    self.testing()
                elif game == 'test2':
                    self.testing2()
                elif game == 'quit':
                    quit()
                if self.afterpractice() == 'repeat':
                    os.system('clear')
                    continue
                else:
                    os.system('clear')
                    break
            self.menu()

    def major(self):
        """
        Review the major system for each user.
        """
        df = pd.read_csv('major_dictionary.csv', index_col=0)
        d = df.to_dict('split')
        d = dict(zip(d['index'], d['data']))

        number = input('Which number would you like to review? q to quit. ')
        while number != 'q':
            words = []
            for word in d[int(number)]:
                if isinstance(word, str):  # Do not print nan
                    words.append(word)
            print(words)
            add_to_dict = input('Would you like to add to that number?'
                                'N / if yes, then enter your word: ').lower()
            if add_to_dict != 'n':
                pass
            number = input('Which other number would you like to review?')

    def afterpractice(self):
        print('This concludes the current practice.')
        answer = input('If you would like to repeat it, enter repeat. Otherwise, enter quit and you will be returned to the main menu.\n').lower()
        return answer

    def random_digits_with_major(self):
        df = pd.read_csv('major_dictionary.csv', index_col=0)
        d = df.to_dict('split')
        d = dict(zip(d['index'], d['data']))

        p = MemoryPalace('Aparetment')

        sequence = []
        for i in range(9):
            j = random.randrange(0, 10, 1)
            sequence += str(j)
        sequence = ''.join(sequence)
        print(sequence)
        sequence = re.findall('...?', sequence)
        print(sequence)
        for i, chunk in enumerate(sequence):
            words = []
            for word in d[int(chunk)]:
                if isinstance(word, str):  # Do not print nan values
                    words.append(word.rstrip(','))
            if p.use_palace(i):
                print(f'{p.use_palace(i)}: {random.choice(words)}')
            else:
                print(f'{random.choice(words)}')
        answer = input('Would you like to see other options'
                       'for any of the above numbers? Y / N: ').lower()
        if answer == 'y':
            self.major()

    def pi_recall(self):
        """
        # import sys, os
        # import curses - trying to read one character at a time
        # add try block for bad user input
        """

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
                pass  # In case of a mistake
        # need to add options for review

    def pi_learn(self):
        """
        Learning digits of pi using either the user's PAO table, or a randomly generated words.
        """

        with open('pi.txt') as f:
            lines = f.readlines()

        pi = ""
        for line in lines:
            pi += line.strip()

        digits_len = int(input('Please enter how many digits do you plan to review: '))
        segments_of_recall = int(input('How many digits would you like to review at a time? '))
        own_or_automated = input('own or own_or_automated?: O / A').lower()

        if own_or_automated == 'o':
            j = 1
            for i in range(0, digits_len, segments_of_recall):
                correct = str(pi[i:(i+segments_of_recall)])
                print(f'{correct}: {pao_helper(int(correct), j)}')
                j += 1
                if j == 4:
                    j = 1

        elif own_or_automated == 'a':
            if segments_of_recall == 3:
                df = pd.read_csv('major_dictionary.csv', index_col=0)
                d = df.to_dict('split')
                d = dict(zip(d['index'], d['data']))

                for i in range(0, digits_len, segments_of_recall):
                    words = []
                    correct = str(pi[i:(i+segments_of_recall)])
                    for word in d[int(correct)]:
                        if isinstance(word, str):  # Do not print nan values from the pandas table
                            words.append(word.rstrip(','))
                    print(f'{random.choice(words)}')
            elif segments_of_recall == 2:
                df = pd.read_csv('nelsonpeg.csv', index_col=0)
                d = df.to_dict('split')
                d = dict(zip(d['index'], d['data']))

                for i in range(0, digits_len, segments_of_recall):
                    words = []
                    correct = str(pi[i:(i+segments_of_recall)])
                    for word in d[int(correct)]:
                        if isinstance(word, str):  # Do not print nan values from the pandas table
                            words.append(word.rstrip(','))
                    print(f'{random.choice(words)}')

    def random_digits():
        # add try block for bad user input
        length_of_sequence = input('Please enter the length of string you wish to recall: ')

        sequence = ''

        for i in range(int(length_of_sequence)):
            j = random.randrange(0, 10, 1)
            sequence += str(j)

        sec = 5

        def timeout():
            """ using threaing for a recall timer """
            print('Time is up!')

        # starting the timer
        t = Timer(sec, timeout)
        t.start()

        print(sequence)
        print(f'Now recall. You have {sec} seconds to work on it!')  # Add timer and erase the sequence

        # join as time is up
        t.join()

        print('*******')
        os.system('clear')

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


class User:
    # PICKLED OBJECT
    """
    Will develop a user class to keep track of all the users using the program.
    Every user will have a unique folder with their own memory palaces and memory systems
    """
    def __init__(self, user_id):
        self.user_id = user_id

    def greeting(self):
        print(f'Hello, {self.user_id}!')

    def load_systems(self):
        pass


class MemoryPalace:
    """
    Memory Palace class to enable constructing new palaces for users
    """
    def __init__(self, palace):
        self.palace = palace

    def use_palace(self, i):
        palace_test = ['Trash cans', 'Bottom of stairs', 'First floor', 'Entrance to apartment']
        return palace_test[i]


# Building a deck of cards as shown in week 4 of class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
        suits = ['spades', 'diamonds', 'clubs', 'hearts']
        self._cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self._cards)

    def show_order(self):
        for card in self._cards:
            print(card)

    def show_order_begginer(self):
        """ only face cards reaveled"""
        cards_to_memorize = []
        for card in self._cards:
            if card.rank in ['J', 'Q', 'K', 'A']:
                print(card)
                cards_to_memorize.append(str(card))
        return cards_to_memorize

    def deck_recall(self):
        """ Beginner friendly verson of faces only. Need to add user choice of how many cards to include"""
        d = Deck()
        d.shuffle()
        print('Start from only face cards.')
        memorize = d.show_order_begginer()
        print(memorize)

        for card in memorize:
            guess = input('Next card? ')
            if card == guess:
                pass
            else:
                print('wrong')
                break


def review():
    print(pd.read_csv('JSystem.csv', delimiter=','))
    f = pd.read_csv('JSystem.csv', delimiter=',')
    while True:
        for _ in range(5):
            number = random.randrange(0, 100, 1)
            print(number)
            print(f.loc[[number]])
        q = input('Enter q to quit: ')
        if q == 'q':
            break

def pao_helper(num, position):
    f = pd.read_csv('JSystem.csv', delimiter=',')
    positionDict = {
        1: 'P',
        2: 'A',
        3: 'O'
    }
    return (f.loc[num, positionDict[position]])


def testing():
    f = pd.read_csv('nelsonpeg.csv', delimiter=',')
    while True:
        number = random.randrange(0, 20, 1)
        print(number)
        peg = input('What is the peg? ')
        print(f['Peg'][number])
        if peg == str(f['Peg'][number]):
            continue
        else:
            pass
        print(f.loc[[number]])
        q = input('Enter q to quit: ')
        if q == 'q':
            break


def testing2():
    f = pd.read_csv('JSystem.csv', delimiter=',')
    while True:
        number = random.randrange(0, 100, 1)
        print(number)
        peg = input('Who is the person? ')
        # print(f['N'][number])
        pao_helper(number, random.randrange(1, 4, 1))
        if peg == str(f['N'][number]):
            continue
        else:
            pass
        # print(f.loc[[number]])
        q = input('Enter q to quit: ')
        if q == 'q':
            break


def create_system():
    pass  # use pandas DataFrame to convert from dictionary


def main():
    os.system('clear')
    j = User('Jonathan')
    a = Application()
    a.greetings()
    a.menu()

if __name__ == '__main__':
    main()
