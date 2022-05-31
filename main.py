import string
from tkinter import *
from tkinter import messagebox
import random

class psswrd_maker:
    
    def __init__(self, master):

        #creating my box here
        #realised too late that maybe i shouldn't have done this in init but in a seperate class?
        #tried to fix it but that ruined the program, so it's stuck in init i guess
        #entry had to be packed seperate, otherwise i couldn't use the .get() function (remember this!!)

        self.master = master

        self.master.geometry('400x100')
        self.master.title('Cengizhans Password Generator')

        self.name = Entry(master)
        self.name.pack()

        self.generator = Button(master, text='press to generate password', command=self.generate).pack()

        self.leave = Button(master, text='press here to quit', command=self.leave).pack()

        master.mainloop()

    def leave(self):
        #simple way to quit app (don't need it but i like it)
        quit()

    def writeinnote(self, name, password):

        #wrote evrything to a txt file for convienence and because i can't get the password in the tkinter box
        #turned everything into a single string to make it look better and convienence
        all = 'name: ' + name + ' ' + 'password: ' + password + '\n'

        new = open('passwords.txt', 'a+')
        new.write(all)
        
        #wrote a messagebox because the program is a little buggy sometimes (god knows why)
        #if the message is not shown im certain something went wrong (i hope)
        messagebox.showinfo(title='succes!', message="written to text file 'passwords.txt'")

    def create_params(self, alllist='*'):

        #create characters used in the password
        #left out some characters because users sometimes confuse them (see bannlist)

        self.alllist = alllist
        lowerlist = list(string.ascii_lowercase)
        upperlist = list(string.ascii_uppercase)
        letterlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        charlist = ['!', '@', '#', '$', '%']

        alllist = list(lowerlist + upperlist + letterlist + charlist)

        bannlist = ['o', 'O', 'l', 'i', 'I']

        for i in alllist:
            if i in bannlist:
                alllist.remove(i)

        return alllist

    def generate(self):
        #make an empty list for a word to later change it to a full string

        TheWord = []
        parameters = self.create_params()

        #add 16 chars in a list and convert it to string
        #there's probably a better way to do this but this is the way i know

        for i in range(16):
            secret_letter = random.choice(parameters)
            makestr = str(secret_letter)
            TheWord.append(makestr)

        self.word = ''

        for i in TheWord:
            self.word += i

        #get the name entry to connect it to a password
        self.entry1 = self.name.get()

        #start writing values to file for later use
        self.writeinnote(self.entry1, self.word)

#create window seperate because that was easier
window = Tk()
psswrd_maker(window)