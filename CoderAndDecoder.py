#encriptanddecript
from tkinter import messagebox, simpledialog, Tk
root = Tk()

#	Test Case 1: 
#		Input:	the quick brown fox jumped over the lazy dog
#		Output:	:=2 *1_.- ,^6># {6/ +1)@2~ 6<2^ :=2 (8!& ~6}

Encripting_Codes = {
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
	'l': "(",
	'm': ")",
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
	' ': ' ',
}
Decripting_codes = {
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
	Part = ("")
	for	 letter in (Message):
		Final_Encription = (Decripting_codes.get(letter))
		if Final_Encription == None:
			print("I don't know '{}'. Skipping…".format(letter))
		else:
			Part += Final_Encription
	messagebox.showinfo('Your decoded message is',	Part)

#encript
def encript (lets_go):
	Message = simpledialog.askstring('Message', 'What is your message')
	Part = ("")
	for letter in (Message):
		Final_Encription = (Encripting_Codes.get(letter))
		if Final_Encription == None:
			print("I don't know '{}'. Skipping…".format(letter))
		else:
			Part += Final_Encription
	messagebox.showinfo('Your coded message is',  Part)

#AskUserWhatTheyWantToDo
What_to_do = simpledialog.askstring('What do you want to do', 'What would you like to do')

def do (command):
	if command == 'code':
		encript ('encripting')
	elif command == 'decode':
		decript ('decipting')
	else:
		messagebox.showinfo('Error', 'Error')

do (What_to_do)

