# Jonathan Shabtai MPCS 51046 (Autumn 2019)

## Memory Trainer
My project is designed to train users primarily in numbers memorization. In order to run the application, please clone the github reporitory to your machine. The application runs on the command-line (Terminal, Shell). You will need to have Python3 installed on your system, and with python run "memorytrainer.py".

The application uses a few 3rd party modules: beautiful soup along with urllib.request for webscraping, pickle to keep information after closing the application, Pandas to work with csv files. You may need to pip install these 3rd party modules to interact fully with my project.

The most interesting parts of my application are the pi_learn and my_number options. They construct for  user a system to remember pi or a manually given number with either the user's system, or an automatically generated one. If the user chooses his / her own system, they can use a memory palace of their choice.

To create new palaces, enter (palaces) and follow the prompt. The palace will be pickled for future use. User's can modify their 3 digit major system dictonary and add entries to it by using the (modify_major) option. Enter a star (\*) if you want the program to give special preferrence to that word.

A few points to note: some lines are too long per the nature of the project, and do not confirm with PEP8. However, breaking those line would make the code less readable. The lines are just a bit longer than 79 characters, so I decided to leave them as is.



## Proposal
Brain and memory games are ubiquitous on the internet as of late. Although they are fun and entertaining, they all lack in flexibility and are fixed with their pre-built settings. They do not walk the users through the foundations of developing memory techniques such as memory palaces and systems. They assume that the users have done their work, are proficient, and just look to train, and as a result can frustrate beginners. The learning curve for memorizing a string of numbers or a deck of cards is very steep without proper help.

For my project, I will build a robust memory trainer that assists users in improving their memory in a more effective way, one step at a time. The program will help users build strong foundations for digits memorization utilizing the [major system](https://en.wikipedia.org/wiki/Mnemonic_major_system). Finding good mnemonics using the system can be challenging when starting, and the program will offer suggestions for any digit combination. The program will allow each user to build their own [PAO system](https://artofmemory.com/wiki/Person-Action-Object_(PAO)_System) and then when practicing, offer help in recalling the mnemonics when needed. Specific training on each user’s PAO system will be implemented as well. Another core aspect of the program will be [memory palaces](https://en.wikipedia.org/wiki/Method_of_loci). The users will have the opportunity to manually build their palaces, and once the information they wish to memorize is recorded, it will automatically be placed in the palace, i.e. the program will populate the memory palace, so that the user can review the information very easily.
In a similar fashion to string digit memorization, the program will include: deck memorization, cell phone numbers, personal information, or any individual memory endeavor the user wishes to conquer (like grocery list). A stretch goal is to implement names and faces recall as well.

## Breakdown
The project will be broken down into the following components (modules and classes):
* User specific authentication (User class)
* Memory Palaces for each user (Palace class)
* Memory Systems for each user (Systems class including number mnemonics and PAO’s)
* Personal recall database for each user (Recall class)
* Random Number and Word generator (List_Generator class)
* A quiz module to practice recall for user specific systems (Quiz class)
* A training module (Training class) for:
  * random numbers (time to review and length of string to be indicated by the user)
  * famous number with strictness indicated by user (number of mistakes and time) (pi, e)
  * deck of cards (include cards requested by user)
  * any other memory endeavor costumized by user.

Aside from the itertools and random Built-in modules, the Third-party packages I look to use are:
* [Pyspellchecker](https://pypi.org/project/pyspellchecker/) - to avoid frustrating experience for the user.
* [PyDictionary](https://pypi.org/project/PyDictionary/) - to complete major system suggestions and fetch words for random words list.
* [Pandas](https://pandas.pydata.org/) - to easily work with CSV files where information will be stored, and develop recalling statistics for every user.

I am considering using tkinter, PySide2, or PySimpleGUI for building a native application instead of running everything on the terminal window as a stretch goal.
