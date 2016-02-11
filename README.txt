System Requirements: 
	pygame 1.9 or greater
	python 2.7.11 or greater

System Restrictions: 
	-Player and bullet movement are based on user's frames per second (fps)
	-Macintosh Systems seem to have performance issues

To run the program: 
	1. cd into the source directory "src"
	2. to run the program enter "python main.py" on the command line

Known Bugs: 
	-When a player's sprite has very high velocity, collissions are interrupted, causing clipping problems. 
	-There are hitbox issues with projectiles. The hitbox only registerse on the top left corner of the sprite. 
	-There are bugs on the ip address and port input screen. The system freezes up when a mouse is hovering over the text input fields. 

How to play the game:
	There are three menus: 
		1. Play
			-The first screen will allow the user to join a game by inputting an ip address and a port number of a server. If a user wants to act as a host, they can click the host button. That host will need to give their ip address and port number to the other users that wish to join his/her lobby. 
			-After joining or hosting the user will be put in a lobby where they will be able to choose their desired team and character. There will also be a chat function where the user can chat with the people in the same lobby. The game will start when the host clicks the start button. 
		2. Options
			-There will be two sliders, one for sound effects and one for music volume. 
		3. Credits 
			-Creators names will be listed here, along with any others that need to be credited for their work. 

	Game rules: 
			-There are 4 classes/wizards to choose from, each have two skills, bound to the left and right 
				-Dank Wizard
				-Void Walker
				-Cleric
				-Gravity Knight 
			-The game mode is Team Deathmatch. The objective is to get a certain amount of kills before the enemy team. 