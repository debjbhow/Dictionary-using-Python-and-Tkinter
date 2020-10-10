from tkinter import *
from PyDictionary import PyDictionary

root=Tk()
root.geometry("250x200")
root.title("Dictionary")

def find_meaning():
    word = e1.get()
    dictionary = PyDictionary(word)
    meaning = dictionary.printMeanings()
    print(meaning)

e1 = Entry(root, font=("times", 15, "bold"))
e1.grid(row=2, column =2)

btn = Button(root, text = "Find Meaning" , command= find_meaning)
btn.grid(row= 4, column= 2)

root.mainloop()