# Jonathan Shabtai MPCS 51046 (Autumn 2019)

## Memory Trainer
My project is designed to train users primarily in numbers memorization. In order to run the application, please clone the github reporitory to your machine. The application runs on the command-line (Terminal, Shell). You will need to have Python3 installed on your system, and with python run "memorytrainer.py".

The application uses a few 3rd party modules: beautiful soup along with urllib.request for webscraping, pickle to keep information after closing the application, Pandas to work with csv files. You may need to pip install these 3rd party modules to interact fully with my project.

The most interesting parts of my application are the pi_learn and my_number options. They construct for users a system to remember pi or a manually given number with either the user's system, or an automatically generated one. If the user chooses his / her own system, they can use a memory palace of their choice. Creating new 2 digit and 3 digit systems from the terminal is too difficult, so I only added a feature that user's can modify the 3 digit major system dictonary and add entries to it by using the (modify_major) option. Enter a star (\*) if you want the program to give special preferrence to that word. Otherwise, users will have to work with any other program to create a .csv file, and then change in the code the references file that the program is using (currently using nelsonpeg.csv for 2 digit automated systems, JSystem.csv as my own 2 digit PAO system, and major_dictionary.csv for 3 digit dictionary).

To create new palaces, enter (palaces) and follow the prompt. The palace will be pickled for future use.

A few things I had to cut out from the project are: User specific login - I assume only one user per computer. Random words list and user created lists - pretty trivial compared to number memorization, thought it wouldn't add to the value project.

A few points to note: some lines are too long per the nature of the project, and do not confirm with PEP8. However, breaking those line would make the code less readable. The lines are just a bit longer than 79 characters, so I decided to leave them as is.

For farther reading about the subject, I recommend the book "Remember it!" by Nelson Dellis where he covers the subjects in this project extensively.
Readings: [major system](https://en.wikipedia.org/wiki/Mnemonic_major_system), [PAO system](https://artofmemory.com/wiki/Person-Action-Object_(PAO)_System), [memory palaces](https://en.wikipedia.org/wiki/Method_of_loci).
