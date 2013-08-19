#Main File
import Player.py, Board.py, Game.py, Boats.py, Authentication.Py
login = False

while login == False:
	intial LOGIN
	- if successful, login = True

if login == True: 
	run = True

While Run == True
present choices:
Main Menu:
1.game
2.Change login
3.About (how to Play)
4.Credits
5.Exit (if exit then run = false, break while loop and quit program)

command = int(input("Choice #: "))

if command == 1: 
	ans1 = 1 player or 2 player?
	ans2 = special powers or no?

	run game(ans1, ans2)

if command == 2:
	self.login = Authentication()

if command == 3:
	display howtoplay.txt

if command == 4:
	made by bo arnold
	email: arnol229@gmail.com

if command == 5:
	run == False