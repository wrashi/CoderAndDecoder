#encriptanddecript
from tkinter import messagebox, simpledialog, Tk
root = Tk()

Encripting_Codes = {
    "Z":"d",
    "Y":"i",
    "X":"l",
    "W":"j",
    "V":"4",
    "U":"w",
    "T":"o",
    "S":"p",
    "R":"z",
    "Q":"y",
    "P":"3",
    "O":"g",
    "N":"5",
    "M":"t",
    "L":"x",
    "K":"i",
    "J":"0",
    "I":"s",
    "H":"q",
    "G":"7",
    "F":"k",
    "E":"9",
    "D":"f",
    "C":"%",
    "B":"$",
    "A":"?",
    "a": "8",
    'b': ",",
    "c": ".",
    "d": "~",
    "e": "2",
    "f": "{",
    "g": "}",
    "h": "=",
    'i': "_",
    'j': "+",
    'k': "-",
    'l': ")",
    'm': "(",
    'n': "#",
    'o': "6",
    'p': "@",
    'q': "*",
    'r': "^",
    's': ";",
    't': ":",
    'u': "1",
    'v': "<",
    'w': ">",
    'x': "/",
    'y': "&",
    'z': '!',
    ' ': '  ',
}
Decripting_codes = {
    "?": "A",
    "$": "B",
    "%": "C",
    "f": "D",
    "9": "E",
    "k": "F",
    "7": "G",
    "q": "H",
    "s": "I",
    "0": "J",
    "i": "K",
    "x": "L",
    "t": "M",
    "5": "N",
    "g": "O",
    "3": "P",
    "y": "Q",
    "z": "R",
    "p": "S",
    "o": "T",
    "w": "U",
    "4": "V",
    "j": "W",
    "l": "X",
    "i": "Y",
    "d": "Z",
    "8": "a",
    ",": "b",
    ".": "c",
    "~": "d",
    "2": "e",
    "}": "f",
    "{": "g",
    "=": "h",
    "_": "i",
    "+": "j",
    "-": "k",
    ")": "l",
    "(": "m",
    "#": "n",
    "6": "o",
    "@": "p",
    "*": "q",
    "^": "r",
    ";": "s",
    ":": "t",
    "1": "u",
    "<": "v",
    ">": "w",
    "/": "x",
    "&": "y",
    "!": "z",
    ' ': " ",
}

#decript
def decript (lets_go):
    Message = simpledialog.askstring('Message', 'What is your message')
    Part = (" ")
    for  letters in (Message):
        Final_Encription = (Decripting_codes.get(letters))
        Final_Encription = (Part + Final_Encription)
        Part = Final_Encription
    messagebox.showinfo('Your decoded message is',  Part)

#encript
def encript (lets_go):
    Message = simpledialog.askstring('Message', 'What is your message')
    Part = (" ")
    for letter in (Message):
        Final_Encription = (Encripting_Codes.get(letter))
        Final_Encription = (Part + Final_Encription)
        Part = Final_Encription
    messagebox.showinfo('Your coded message is',  Part)

#AskUserWhatTheyWantToDo
What_to_do = simpledialog.askstring('What do you want to do', 'What would you like to do')

def do (command):
    if command == 'code':
        encript ('encripting')
    elif command == 'decode':
        decript ('decipting')
    else:
        messagebox.showinfo('Error', 'Sorry I can only code and decode messages')

do (What_to_do)
