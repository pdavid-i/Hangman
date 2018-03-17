from validation import *
from domain import *
from random import *

class Contoller:
    def __init__(self, repo):
        self.repo =repo


    def add_word(self, string):
        try:
            validate_word(string)
        except WordException:
            return False
        word = Word(string)
        self.repo.add(word)
        f = open('file.txt', 'a')
        f.write(string)
        f.write('\n')
        f.close()

    def delete_word(self, string):
        f = open("file.txt", "r")
        lines = f.readlines()
        f.close()
        f = open("file.txt", "w")
        for line in lines:
            if line != string + "\n":
                f.write(line)
        f.close()

    def get_word(self):
        f = open('file.txt' , 'r')
        count = 0
        for line in f:
            count += 1
        number = randint(0, count)
        f.seek(0)
        for line in f:
            if (number == 0):
                return line
            number += -1
        f.close()

    def game_on(self):
        word = self.get_word()
        list = []
        for i in range(len(word) - 1):
            list.append(0)
        #print(word)
        print("The game has started! Good luck! Your word has " + str(len(list)) + " letters!"  )
        self.do_it(word, list)

    def printer(self, word, list):
        for i in range(len(list)):
            if list[i] == 1:
                print(word[i], end=' ')
            else:
                print("_", end=' ')
        print('')

    def do_it(self, word, list):
        ok = 1
        for x in list:
            if x == 0:
                ok = 0
        if ok == 1:
            print("Congratulasions! You have won!")
            return True
        letter = input("Enter a letter: ")
        for i in range(len(word)):
            if word[i] == letter:
                list[i] = 1
        self.printer(word, list)
        return self.do_it(word, list)

    def get_words(self):
        f = open('file.txt', 'r')
        lines = f.readlines()
        f.close()
        return lines

