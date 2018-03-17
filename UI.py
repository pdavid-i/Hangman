from controller import *

def ui_delete_word(controller):
    word = input("Enter word you want to remove: ")
    controller.delete_word(word)

def ui_add_word(controller):
    word = input("Enter word you wish to add: ")
    controller.add_word(word)

def ui_print_words(controller):
    i = 1
    for word in controller.get_words():
        print(str(i) + ". "+ str(word), end='')
        i+=1

def ui_get_word(controller):
    print("The word is: " + controller.get_word())

def ui_play(controller):
    controller.game_on()
