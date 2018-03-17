from repository import *
from UI import *

def read_cmd():
    cmd = input(">>")
    if cmd == "":
        return read_cmd()
    return cmd

def help():
    print("Welcome to Hangman! Your commands are: \n 1. 'add' - adds a word to the pool with possible words \n 2. \
'delete' - removes a word from the pool with possible words\n 3. 'list' - shows all the wors in the pool \n \
4. 'play' - starts the game \n 5. 'help' - shows the list of commands \n 6. 'exit' - quits the app")

def start():
    repo = Repository()
    control = Contoller(repo)
    commands = {"add":ui_add_word, "play":ui_play, "list":ui_print_words, "delete":ui_delete_word}
    help()
    while True:
        cmd = read_cmd()
        if cmd == 'help':
            help()
        if cmd == "exit":
            return True
        if cmd in commands:
            commands[cmd](control)
        else:
            print("Invalid command!")

start()