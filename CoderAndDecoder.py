import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import string, random

#	Test Case 1: 
#		Input:	the quick brown fox jumped over the lazy dog
#		Output:	:=2 *1_.- ,^6># {6/ +1)@2~ 6<2^ :=2 (8!& ~6}

#	Global Variables

Encrypting_Codes = {}
characters = list(string.ascii_uppercase) + list(string.ascii_lowercase)
shuffled = characters.copy()
random.shuffle(shuffled)

for index, value in enumerate(characters):
	Encrypting_Codes[characters[index]] = shuffled[index]
print(Encrypting_Codes)

Decrypting_codes = {}
for key, value in Encrypting_Codes.items():
	Decrypting_codes[value] = key

#	Functions

# Function for when the combobox item is chosen
def callbackFunc(event):
	command = comboChoice.get()
	if command == 'Code':
		crypt ('encrypting')
	elif command == 'Decode':
		crypt ('decrypting')
		
#	encryput / decrypt a message
def crypt (lets_go):
	Message = simpledialog.askstring('Message', 'What is your message')
	Part = ("")
	for	 letter in (Message):
		if lets_go == 'encrypting':
			Final_Encryption = (Encrypting_Codes.get(letter))
		else:
			Final_Encryption = (Decrypting_codes.get(letter))
		if Final_Encryption == None:
			print("I don't know '{}'. Passing through…".format(letter))
			Part += letter
		else:
			Part += Final_Encryption
	message = "Your message is\n'{}'".format(Part)
	codeMessage.set(message)
	print(message)

#	Gui Code

app = tk.Tk() 
WINDOWWIDTH = 300
app.geometry('{}x150'.format(WINDOWWIDTH))

#	Label
labelTop = tk.Label(app, text = "What do you want to do?")
labelTop.grid(column=0, row=0)

#	Combobox
comboChoice = ttk.Combobox(app, values=[
	"Code", 
	"Decode"])
comboChoice.grid(column=0, row=1)
comboChoice.bind("<<ComboboxSelected>>", callbackFunc) # Calls the function on selection

#	Message
codeMessage = tk.StringVar()
labelBottom = tk.Label(app, textvariable=codeMessage, wraplength=WINDOWWIDTH-10)
labelBottom.grid(column=0,row=2)

app.mainloop()
