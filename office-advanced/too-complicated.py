import time
from random import randint
from colorama import init
init()
from colorama import Fore, Back, Style

#
# presenting
# Office Quest
# a text adventure game
# by Miss Jo
#
# March/April 2021
#

# ===================================================
# DEVELOPING VARIABLES
# ===================================================

debug = 0
quickly = 1

# ===================================================
# GLOBAL VARIABLES
# ===================================================

# game controlling state variable
keepGoing = False

# for display
hole = 0
holes = [' ','o','Q','*']

# for detecting commands (and coloring them red)
cmd = '*'

# for breaking up long strings into readable lengths
lineLen = 50

# for managing the Colorama codes
colors = (
	Fore.WHITE + Style.NORMAL,
	Fore.RED + Style.BRIGHT,
	Fore.YELLOW + Style.BRIGHT,
	Fore.GREEN + Style.BRIGHT,
	Fore.CYAN + Style.BRIGHT
)

# GAME/STORY VARIABLES

# DATE (when)
workdays = ['Monday', 'Wednesday', 'Friday']
today = 0

# LOCATIONS (where)
rooms = {
	0: {
		'niceName': 'your cubicle',
		'shortName': 'cubicle',
		'index': 0
	},
	1: {
		'niceName': 'the breakroom',
		'shortName': 'break',
		'index': 1
	},
	2: {
		'niceName': "the BOSS's office",
		'shortName': 'boss',
		'index': 2
	},
	3: {
		'niceName': 'the copyroom',
		'shortName': 'copy',
		'index': 3
	},
	4: {
		'niceName': "your neighbor's cubicle",
		'shortName': 'neighbor',
		'index': 4
	}
}
location = 0

# ITEMS (what?)
inventory = {}
itemsForPickUp = {
	'mug': {
		'location': 0,
		'cangoto': (0, 1),
		'inInventory': False,
		'state': {
			'fillOptions': ('coffee', 'water', 'pens', 'none'),
			'fill': 3,
			'dirty': True
		}
	},
	'pen': {
		'location': 0,
		'cangoto': (0, 1, 2, 3, 4),
		'inInventory': False,
		'state': {
			'works': True
		}
	},
	'stapler': {
		'location': 3,
		'cangoto': (0, 3, 4),
		'inInventory': False,
		'state': {
			'hasStaples': True,
			'jammed': False
		}
	},
	'paper': {
		'location': 3,
		'cangoto': (0, 1, 2, 3, 4),
		'inInventory': False,
		'state': {}
	}
}

interactions = {
	'plant': {},
	'copier': {},
	'sink': {},
	'trashcan': {},
	'shredder': {}
}

tasks = {}
# task name
# in room 0, 1, 2, 3, 4
# with items or people

# ===================================================
# FUNCTIONS
# ===================================================

## TIMING

# controls pauses
# to skip pauses, set "quickly" to 1
def pause(drama, paper = True):
	if drama == 'd1':
		for x in range(1,4):
			if quickly < 1:
				time.sleep(1)
			if paper:
				print(officePaperHole() + '   ' + ('. ' * x))
			else:
				print('. ' * x)
		if quickly < 1:
			time.sleep(1)
		if paper:
			print(officePaperHole())
		else:
			print('')
	elif drama == 'd2':
		if quickly < 1:
			time.sleep(1)
		if paper:
				print(officePaperHole())
		else:
			print('')
		if quickly < 1:
			time.sleep(1)
		print()
	elif drama == 'drip':
		if quickly < 1:
			time.sleep(0.33)
	else:
		if quickly < 1:
			time.sleep(1)

## DISPLAY

## COLORS

# makes the enclosed string print in white
def white(string):
	return colors[0] + string + colors[0]

# makes the enclosed string print in red
def red(string):
	return colors[1] + string + colors[0]

# makes the enclosed string print in yellow (except it looks orange)
def yellow(string):
	return colors[2] + string + colors[0]

# makes the enclosed string print in green
def green(string):
	return colors[3] + string + colors[0]

# makes the enclosed string print in cyan
def blue(string):
	return colors[4] + string + colors[0]

# prints a blank line
def blank(paper = True):
	if paper:
		print(officePaperHole())
	else:
		print('')

# Controls with the "office paper" line has a hole or not
def officePaperHole(letter = ''):
	global hole
	if letter == 'q':
		return blue('| ' + holes[2] + ' |')
	elif letter == 'u':
		return yellow('| ' + holes[3] + ' |')
	else:
		if hole < 1:
			hole = 1
			return '| ' + holes[0] + ' |'
		elif hole > 0:
			hole = 0
			return blue('| ' + holes[1] + ' |')

# Prints lines with "office paper"
# Also breaks long lines up appropriately
# Also find CMDs and makes them red!
def officePaper(string, spaces = False):
	if spaces:
		print(officePaperHole())

	words = string.split()
	charCount = 0
	temp = ""
	tempL = []

	for word in words:
		charCount += len(word)
		if charCount < lineLen:
			if word[0] == '*':
				charCount -= 1
				temp += red(word[1:]) + ' '
			elif word == 'HOT' or word == 'TIP:':
				temp += green(word) + ' '
			else:
				temp += word + ' '
		else:
			tempL.append(temp)
			charCount = len(word)
			if word[0] == '*':
				charCount -= 1
				temp = red(word[1:]) + ' '
			else:
				temp = word + ' '
	tempL.append(temp)
	for line in tempL:
		print(officePaperHole() + '   ' + line)
	
	if spaces:
		print(officePaperHole())
	pause('drip')

## STORYLINE

# View Width Check
def widthCheck():
	print('For the best experience, adjust the width of your viewer.')
	print('* * * * *       You should see ten asterisks all on one line.      * * * * *')
	getit = input("When you're ready to continue, type " + red('C') + " and press enter. " + colors[2] + '\n')
	while getit != 'C' and getit != 'c':
		getit = input(colors[0] + 'Try again. '+ colors[2] + '\n')
	return True

# Game Intro
def intro():
	showPaper = False
	pause('', showPaper)
	blank(showPaper)

	print('The weekend is over.')
	pause('', showPaper)
	pause('', showPaper)

	print("And you are unprepared for ...")
	pause('', showPaper)
	pause('', showPaper)

	blank(showPaper)

	content = (
		' ' * 58,
		' ' * 58,
		' ' * 58,
		' ______     ______   ______   __     ______     ______    ',
		'/\  __ \   /\  ___\ /\  ___\ /\ \   /\  ___\   /\  ___\   ',
		'\ \ \/\ \  \ \  __\ \ \  __\ \ \ \  \ \ \____  \ \  __\   ',
		' \ \_____\  \ \_\    \ \_\    \ \_\  \ \_____\  \ \_____\ ',
		'  \/_____/   \/_/     \/_/     \/_/   \/_____/   \/_____/ ',
		' ' * 58,
		'       ______     __  __     ______     ______     ______ ',
		'      /\  __ \   /\ \/\ \   /\  ___\   /\  ___\   /\__  _\\',
		'      \ \ \/\_\  \ \ \_\ \  \ \  __\   \ \___  \  \/_/\ \/',
		'       \ \___\_\  \ \_____\  \ \_____\  \/\_____\    \ \_\\',
		'        \/___/_/   \/_____/   \/_____/   \/_____/     \/_/',
		' ' * 58,
		' ' * 58,
		' ' * 58,
		'               AN INTENSE* OFFICE ADVENTURE               ',
		' ' * 58,
		'   *intense for a quiet office full of diligent workers   ',
		' ' * 58,
		' ' * 58,
		' ' * 58
	)

	print(blue('i - i') + ' — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —  ' + blue('i - i'))
	for line in content:
		margin = officePaperHole()
		print(margin + '   ' + line + '     ' + margin)
		pause('drip')

# Endings

# win
def getRaise():
	print('You have been working hard! You get a raise!')
	print('*BOSS* is impressed and offers you a manager position.')
	print('It comes with a raise, but you have to do more than stapling pages.')
	print('Do you want to take the new position? y/n')
	print('')
	printBusinessCard()

# lose
def getFired():
	print('You have been hardly working. You get fired!')

# draw
def getPay():
	print('You did some work. Here is money!')
	printPaycheck()

# Determine Which Ending
def winLoseDraw():
	print('You have worked # out of 3 days this week.')
	print('Calculating the ending...')

# How to Play
def instructions():
	print('How to Play')

# Print Paycheck
def printPaycheck():
	print('**** You called the printPaycheck function.')

# Print Business Card
def printBusinessCard():
	print('**** You called the printBusinessCard function.')

## GAME FUNCTIONS

## Randomly Assign Tasks (3 for each day, 3 days total)
def assignTasks():
	print('Tasks!')
	# task name
	# on day 0, 1, or 2
	# in room 0, 1, 2, 3, 4
	# with items or people

# Ask them a question
def ask(string = ''):
	print(officePaperHole('q') + '   ' + colors[4] + string)
	asking = input(officePaperHole('u') + colors[2] + '   ')
	return asking

# Explain WHERE they are
def whereAmI():
	if debug > 0:
		print('**** You called the whereAmI function.')
	officePaper('You are currently in ' + str(rooms[location]['niceName']) + '.')

# Explain WHERE they can go
def showRooms():
	if debug > 0:
		print('**** You called the showRooms function.')
	whereAmI()
	officePaper('You can go to the following rooms: ')
	for room in rooms:
		if rooms.index(room) != location:
			officePaper('  ... ' + room)

# Explain WHAT they have
def printInventory():
	if debug > 0:
		print('**** You called the printInventory function.')
	print(inventory)

# Explain WHAT they can do
def whatCanIDo():
	if debug > 0:
		print('**** You called the whatCanIDo function.')
	officePaper('You can do some options.')

## ACTIONS

# Do something
def verb( do ):
	if debug > 0:
		print('**** You called the verb function.')

# Pick Up Item
def itemUp( name ):
	if debug > 0:
		print('**** You called the itemUp function.')

# Put Down Item
def itemDown( name ):
	if debug > 0:
		print('**** You called the itemDown function.')

# Look Around
def look(loc):
	if debug > 0:
		print('**** You called the look function.')

# Go to
def goTo(loc):
	global location
	if debug > 0:
		print('**** You called the goTo function.')

## Specific Interactions

# in your cubicle, 0
# Trashcan

# in the breakroom, 1
# Sink
# Coffee Maker
# Refrigerator
# Window ?
# Plant

# in the Boss's officePaper, 2
# nothing

# in the copyroom, 3
# Stapler
# Copier
# Shredder

# in your neighbor's cubicle, 4
# nothing

# Process User input
def processInput(command):
	cmd = command.upper()
	if debug > 0:
		print('**** You called the processInput function.')
	if cmd == 'HELP' or cmd =='H':
		instructions()
	else:
		return
	# Explain
	# Pick Up or Put Down
	# Look Around
	# Go To
	# Interact
	

# ===================================================
# MAIN
# ===================================================

# main game loop
def main():
	global today, keepGoing

	print(colors[0])

	runit = True#widthCheck()
	if runit:
		blank(False)
		print(colors[0] + 'Loading Game')
		pause('d1', False)
	
	intro()
	blank()
	pause('')
	pause('d1')
	blank()

	officePaper('To read how to play, type *HELP or *H and press enter. You can access the *HELP menu at any time during the game.', True)
	officePaper('To begin playing, type *START or *S and press enter.', False)
	officePaper('HOT TIP: when you type an answer or command, you can type in UPPER or lower case or MiXeD cAsE. Your choice!', True)
	blank()
	choice = ask('What would you like to do?')

	while choice.upper() not in ['HELP', 'START']:
		officePaper("You can't do that now. Type *HELP or *START and press enter.")
		choice = ask('What would you like to do?')
	if choice.upper() == 'HELP':
		instructions()
	else:
		keepGoing = True

	# day
	while keepGoing:

		blank()
		blank()
		officePaper('Today is {}.'.format(workdays[today]))
		officePaper('It is time for work.')
		pause('')

		officePaper('You arrive at the office and enter your cubicle.')
		pause('')

		print('Your tasks for today are: TASK1, TASK2, and TASK3.')
		
		# what do you want to do?
		# You have completed task #.

		print('You complete three tasks.')

		## The end of the day!
		officePaper('You have made it to the end of the workday.')
		pause('')
		
		## 
		num = (len(workdays) - 1) - today
		if num > 0:
			print('You have {} more possible work days this week.'.format(num))
			print('Do you want to keep working? y/n')
			choice = input()
			if choice == 'n':
				keepGoing = False
				winLoseDraw()
			else:
				today += 1
		else:
			winLoseDraw()
	
	print('THE END.')

main()
