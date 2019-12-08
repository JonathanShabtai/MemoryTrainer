import random
import time
import os
from threading import Timer
import pandas as pd
import re
import card_deck
import pickle
#  import gc

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
        print('The application offers a comprehensive memory training.')
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
                         '4. Random digits recall (enter random) \n'
                         '5. PAO recall (enter PAO) \n'
                         '6. Work on your palaces (enter palaces) \n'
                         '7. Modify the 3 digit major dictionary (enter modify_major) \n'
                         '8. Your number quick Mnemonic Generation (enter my_number) \n'
                         '9. Deck recall (enter cards) \n'
                         'quit to quit \n').lower()
            while True:
                if game == 'msp':
                    self.msp()
                elif game == 'pi_learn':
                    self.learn('pi')              
                elif game == 'pi':
                    self.pi_recall()
                elif game == 'random':
                    self.random_digits()
                elif game == 'pao':
                    self.pao()
                elif game == 'palaces':
                    p = MemoryPalace('somePalace')
                    p.palaces_menu()
                elif game == 'modify_major':
                    self.modify_major()
                elif game == 'my_number':
                    self.learn('num')
                elif game == 'review':
                    self.review()
                elif game == 'cards':
                    d = card_deck.Deck()
                    d.deck_recall()
                elif game == 'quit':
                    quit()

                if self.afterpractice() == 'repeat':
                    os.system('clear')
                    continue
                else:
                    os.system('clear')
                    break
            self.menu()


    def afterpractice(self):
        """ Repeat or menu options for user """
        print('\nThis concludes the current practice.')
        print('If you would like to repeat it, enter (repeat).')
        answer = input('Otherwise, enter (main_menu) and you will be returned to the main menu.\n').lower()
        return answer

    def msp(self):
        """ Practice major system knowledge using the major_dictionary.csv file. """

        major_helper = {
        '0': ['s', 'z'],
        '1': ['t', 'd', 'th'],
        '2': ['n'],
        '3': ['m'],
        '4': ['r'],
        '5': ['l'],
        '6': ['j', 'ch', 'sh'],
        '7': ['c', 'k', 'g', 'q', 'ck'],
        '8': ['v', 'f', 'ph'],
        '9': ['p', 'b']
        }

        print('Here is a quick reminder of how the major system is structured: ')
        print(pd.DataFrame.from_dict(major_helper, orient='index'))
        print('To learn more, visit: https://en.wikipedia.org/wiki/Mnemonic_major_system')
        df = pd.read_csv('major_dictionary.csv', index_col=0)
        d = df.to_dict('split')
        d = dict(zip(d['index'], d['data']))

        number_of_questions = int(input('How many numbers would you like to be quizzed on? '))

        correct_count = 0
        for _ in range(number_of_questions):
            random_number = random.randrange(0, 1000, 1)
            while True:
                random_word = random.choice(d[random_number])
                if isinstance(random_word, str):
                    random_word = random_word.rstrip(',')
                    if random_word in ['Sorry', 'no', 'results.' ,':(']: #  Some number do not have a match
                        random_number = random.randrange(0, 1000, 1) #  Pick another number for the user
                    else:
                        break
            print(random_word)
            answer = input('What is the associated number? ')
            if int(answer) == random_number:
                print('Very good!\n')
                correct_count += 1
            else:
                print(f'Not correct! The correct answer was {random_number}.\n')

        print(f'You scored {correct_count} out of {number_of_questions}.')


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

    def learn(self, pi_or_num):
        """
        Learning digits of pi using either the user's PAO table, or a randomly generated words.
        This method is also used for a user entered number.
        """

        if pi_or_num == 'pi':
            with open('pi.txt') as f:
                lines = f.readlines()

            pi = ""
            for line in lines:
                pi += line.strip()

            digits_len = int(input('Please enter how many digits do you plan to review: '))

        elif pi_or_num == 'num':
            pi = input('Enter your number')
            digits_len = len(pi)

        segments_of_recall = int(input('How many digits would you like to review at a time (2 or 3)? '))
        own_or_automated = input('Own numbers system or Automated (O / A)? ').lower()
        memory_palace_y_n = input('With palace (Y / N)? ').lower()

        with_palace = False
        if memory_palace_y_n == 'y':
            with_palace = True
            print('Available are: ')
            p = MemoryPalace('somePalace')
            p.print_all_palaces()
            memory_palace = input('Pick one: ')
            list_of_rooms = p.print(memory_palace)
            

        if own_or_automated == 'o':
            segments_of_recall = 2
            j = 1
            counter = 0
            for i in range(0, digits_len, segments_of_recall):
                correct = str(pi[i:(i+segments_of_recall)])
                if not with_palace:
                    print(f'{correct}: {self.pao_helper(int(correct), j)}')
                else:
                    if j == 1:
                        try:
                            print(f'Room for next 3 segments: {list_of_rooms[counter]}.')
                            print(f'{correct}: {self.pao_helper(int(correct), j)}')
                        except IndexError:  # Out of rooms in the palace
                            print(f'{correct}: {self.pao_helper(int(correct), j)}')
                    else:
                        print(f'{correct}: {self.pao_helper(int(correct), j)}')
                j += 1
                if j == 4:  # Reset counter j for pao_helper use
                    j = 1
                    counter += 1  # Move to the next room

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
                df = pd.read_csv('nelsonpeg.csv', index_col=0)  # Using recommended system from Remember it! book
                d = df.to_dict('split')
                d = dict(zip(d['index'], d['data']))

                for i in range(0, digits_len, segments_of_recall):
                    words = []
                    correct = str(pi[i:(i+segments_of_recall)])
                    for word in d[int(correct)]:
                        if isinstance(word, str):  # Do not print nan values from the pandas table
                            words.append(word.rstrip(','))
                    print(f'{random.choice(words)}')


    def random_digits(self):
        # add try block for bad user input
        length_of_sequence = input('Please enter the length of string you wish to recall: ')
        segments_of_recall = int(input('How many digits would you like to recall at a time? '))

        sequence = ''

        #  Generate the random number to memorize
        for i in range(int(length_of_sequence)):
            j = random.randrange(0, 10, 1)
            sequence += str(j)

        sec = input('How many seconds would you need to review the number? ')
        sec = int(sec)

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

        os.system('clear')

        print(f'Please recall the number, {segments_of_recall} digits at a time. ')

        mistakes = 0
        correct = 0
        mistakes_list = []
        you_guessed = []

        for i in range(0, len(sequence), segments_of_recall):
            guess = input(f'Enter the next {segments_of_recall} digits. ')
            if guess == sequence[i:i+segments_of_recall]:
                print('Nice!')
                correct += 1
            else:
                print('Wrong, you can review at the end. ')
                mistakes += 1
                you_guessed.append(guess)
                mistakes_list.append(sequence[i:i+segments_of_recall])

        print(f'You had {mistakes} segment mistakes. You got {correct} correctly!')

        review = input('Would you like to review the mistakes? Y / N: ').lower()
        if review == 'y':
            for your_guess, correct_guess in zip(you_guessed, mistakes_list):
                print(f'You guessed {your_guess}')
                print(f'The answer was {correct_guess}')
        else:
            return


    def review(self):
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


    def modify_major(self):
        """ Review of the major system for each user. """
        df = pd.read_csv('major_dictionary.csv', index_col=0)
        d = df.to_dict('split')
        d = dict(zip(d['index'], d['data']))

        number = input('Which number would you like to review? type main_menu to return. \n')
        while number != 'main_menu':
            words = []
            for word in d[int(number)]:
                if isinstance(word, str):  # Do not print nan
                    if word not in ['Sorry', 'no', 'results.' ,':(']:
                        words.append(word)
            print(words)
            add_to_dict = input('Would you like to add to that number?'
                                'N / if yes, then enter your word. Add * to make it a favorite: ').lower()
            if add_to_dict != 'n': #  Fix this first thing
                print(str(len(words)) + ' is the len')
                df.at[int(number), str(len)] = add_to_dict
                df.to_csv('major_dictionary.csv')
                d = df.to_dict('split')
                d = dict(zip(d['index'], d['data']))

            number = input('Which other number would you like to review? type main_menu to return. ')


    def pao_helper(self, num, position):
        f = pd.read_csv('JSystem.csv', delimiter=',')
        positionDict = {
            1: 'P',
            2: 'A',
            3: 'O'
        }
        return (f.loc[num, positionDict[position]])


    def pao_quiz(self):
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

class MemoryPalace:
    """
    Memory Palace class to enable constructing new palaces, or using existing ones.
    """
    def __init__(self, palace):
        self.palace = palace

    def palaces_menu(self):
        answer = input('Would you like to create a new palace (new), delete (del), modify (mod), or visit (visit)? ').lower()
        if answer == 'new':
            new_palace = input('We are set to create a new palace. What would be the name of it? ')
            p = MemoryPalace(new_palace)
            locations_number = input('How many locations? ')
            p.create(int(locations_number))
        elif answer == 'visit':
            print('Available are: ')
            current = MemoryPalace('somePalace')
            current.print_all_palaces()
            visit = input('Which palace would you like to visit? ')
            current = MemoryPalace(visit)
            current.print(visit)
        elif answer == 'del':
            print('Available are: ')
            current = MemoryPalace('somePalace')
            current.print_all_palaces()
            del_palace = input('Which palace would you like to delete? ')
            current = MemoryPalace(del_palace)
            current.delete_palace(del_palace)
        elif answer == 'mod':
            print('Available are: ')
            current = MemoryPalace('somePalace')
            current.print_all_palaces()
            mod = input('Which palace would you like to modify (add locations to)? ')
            current = MemoryPalace(mod)
            current.mod(mod)

    def use_palace(self, name_of_palace, i=None):
        palace = self.load(name_of_palace)
        return palace

    def print_all_palaces(self):
        """ Reminds the user of all of the available memory palaces. """
        for file in os.listdir(os.getcwd()):
            if '.pickle' in file:
                print(file[:-7])

    def load(self, name_of_palace):
        pickle_in = open(name_of_palace + '.pickle', 'rb')
        palace = pickle.load(pickle_in)
        return palace

    def save(self, new_palace):
        print(str(self.palace))
        pickle_out = open(str(self.palace) +'.pickle', 'wb')
        pickle.dump(new_palace, pickle_out)
        pickle_out.close()

    def create(self, size):
        new_palace = []
        for i in range(size):
            location = input('Enter next location: ')
            new_palace.append(location)
        self.save(new_palace)

    def print(self, name_of_palace):
        #current_palace = load(self)
        list_of_rooms = []
        for i, room in enumerate(self.use_palace(name_of_palace)):
            print(f'{i+1}. {room}')
            list_of_rooms.append(room)
        return list_of_rooms

    def delete_palace(self, name_of_palace):
        path = os.getcwd()
        os.remove(path + '/' + name_of_palace + '.pickle')

    def mod(self, name_of_palace):
        to_modify = self.load(name_of_palace)
        room = ''
        location = input('Enter next location (type stop to stop): ')
        while location != 'stop':
            to_modify.append(location)
            location = input('Enter next location (type stop to stop): ')
        self.save(to_modify)


def main():
    os.system('clear')
    a = Application()
    a.greetings()
    a.menu()


if __name__ == '__main__':
    main()
