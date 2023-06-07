import time
import random

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

quickly = 1

# ===================================================
# GLOBAL VARIABLES
# ===================================================

Monday = (
	' .    _ _    __          __    __',
	' .   | | |  |  |  |\ |  |  \  |__|  \ /  |',
	' .   | | |  |__|  | \|  |__/  |  |   |   .',
	' . '
)

Wednesday = (
	' .           __   __          __   __   __    __',
	' .   | | |  |__  |  \  |\ |  |__  |_   |  \  |__|  \ /  |',
	' .   |_|_|  |__  |__/  | \|  |__  __|  |__/  |  |   |   .',
	' . '
)

Friday = (
	' .    __   __   _ _   __    __',
	' .   |__  |__|   |   |  \  |__|  \ /  |',
	' .   |    | \   _|_  |__/  |  |   |   .',
	' . '
)

GameName = (
	' .           __    __            ___  _ _   _ _    __',
	' .   | | |  |  |  |__|  |_/       |    |   | | |  |__  |',
	' .   |_|_|  |__|  | \   | \       |   _|_  | | |  |__  .',
	' . '
)

# game controlling state variable
keepGoing = False

# GAME/STORY VARIABLES

# DATE (when)
workdays = ['Monday', 'Wednesday', 'Friday']
today = 0

# ITEMS (what?)
inventory = []
itemsForPickUp = {
	'stapler': {'inInventory': False},
	'paper': {'inInventory': False}
}

tasksPerDay = 2
daysWorked = []
AvailableTasks = {
	'a': {
		'nom': 'a',
		'sum': 'Pick up paper.',
		'done': False
	},
	'b': {
		'nom': 'b',
		'sum': 'Pick up stapler.',
		'done': False
	}
}

playerTasks = []

# ===================================================
# FUNCTIONS
# ===================================================

## TIMING

# controls pauses
# to skip pauses, set "quickly" to 1
def pause(drama):
	if drama == 'd1':
		for x in range(1,4):
			if quickly < 1:
				time.sleep(1)
			print(' . ' * x)
		if quickly < 1:
			time.sleep(1)
		print(' .')
	elif drama == 'd2':
		if quickly < 1:
			time.sleep(1)
		print(' .')
		if quickly < 1:
			time.sleep(1)
	elif drama == 'drip':
		if quickly < 1:
			time.sleep(0.33)
	else:
		if quickly < 1:
			time.sleep(1)

## DISPLAY

def pretty(string, spaceAfter = False):
	print(' .   ' + string)
	
	if spaceAfter:
		print()
	pause('')

## STORYLINE

# Game Intro
def intro():
	pause('')
	print(' . ')
	pause('')
	print(' .   The weekend is over.')
	pause('')
	print(' . ')
	pause('')
	print(' .   And you are unprepared for ...')
	pause('')
	print(' . ')
	pause('')

	content = (
		' .   IT\'S TIME FOR WORK*.',
		' . ',
		' .   DISCLAIMER: There is no actual work',
		' .   completed while playing this game.',
		' . '
	)

	for line in GameName:
		print(line)
		pause('drip')

	for line in content:
		print(line)
		pause('drip')
	print()

# Endings

# win
def getRaise():
	pretty('BOSS is impressed and offers you a manager position.')
	pretty('It comes with a raise, but you would have to pick up')
	pretty('more paper and more staplers.')
	print()
	w = ask('Do you want to take the new position? *Y or *N', ['Y', 'YES', 'N', 'NO'])
	if processInput(w):
		print()
		pretty('BOSS is pleased! They welcome you to the team.')
		pretty('They hand you your new business card.')
		pause('d1')
		printBusinessCard()
	else:
		print()
		pretty('BOSS seems understanding, but you can tell they')
		pretty('think it\s a bad career move. Either way, you\'re')
		pretty('content, and you\'ve made it to the end of ...')

# lose
def getFired(excuses = False):
	if excuses:
		pause('d1')
		pretty('BOSS turns to you and says, "THERE IS NO EXCUSE FOR YOU.')
		pretty('We\'re letting you go."')
		pause('d2')
		pretty('You feel {}.' . format('horrified'))
		pretty('Fortunately, You\'ve made it to the end of ...')
	else:
		pause('d1')
		pretty('BOSS turns to you and says, "This is unacceptable.')
		pretty('We\'re letting you go."')
		pause('d2')
		pretty('You feel {}.' . format('pleased'))
		pretty('And you\'ve made it to the end of ...')

# draw
def getPay():
	pretty('Here is money!')
	printPaycheck()

# Determine Which Ending
def winLoseDraw(nap = False):
	daysWorked = today + 1
	tasksCompleted = countTasksDone()
	rating = tasksCompleted / daysWorked

	print()
	pretty('You have worked {} out of 3 days this week.' . format(daysWorked))
	print(' . ')
	pretty('Your rating for the week is ...')
	pause('d1')

	if rating >= tasksPerDay and daysWorked > 1:
		pretty('★ ★ ★ ★  FOUR STARS! You worked hard!', True)
		getRaise()
	elif rating > 0:
		pretty('★ ★ ☆ ☆  TWO STARS! You did work.', True)
		getPay()
	else:
		pretty('☆ ☆ ☆ ☆  NO STARS. You hardly worked.', True)
		print()
		pretty('BOSS is angry with you.')
		print()

		x = ask('Do you want to offer an excuse? *Y or *N', ['Y', 'YES', 'N', 'NO'])
		if x:
			getFired(True)
		else:
			getFired()

# How to Play
def instructions():
	print()
	print()
	print('[*]  HOW TO PLAY: ')
	print()
	pause('')
	print('[*]  Typable commands are shown in uppercase and begin with "*".')
	print()
	pause('')
	print('[*]  When you type the command, do not include the asterisk.')
	print()
	pause('')
	print('[*]  You can type in UPPER or lower or MiXeD case.')
	print()
	pause('')
	print('[*]  When you are done typing the command, press enter.')
	print()
	pause('')

# Print Paycheck
def printPaycheck():
	print('[$]  You have received money.')
	print()
	pretty('Mediocre job! You\'ve come to the end of ...')

# Print Business Card
def printBusinessCard():
	print('[@]  You have received business card.')
	print()
	pretty('Great job! You\'ve come to the end of ...')

## GAME FUNCTIONS

## Randomly Assign Tasks
def assignTasks(today):
	todo = {}
	for num in range(0, tasksPerDay):
		t = random.choice(list(AvailableTasks.keys()))
		todo[str(num)] = AvailableTasks[t].copy()
	playerTasks.append(todo)

def displayTasks():
	if len(playerTasks) > 0:
		for day in range(len(playerTasks)):
			if day == today:
				if len(playerTasks[day]) > 0:
					item = 1
					print('[T]  Today\'s tasks are:')
					for value in playerTasks[day].values():
						if value['done'] == False:
							print('[{}]  ' . format(item) + value['sum'])
							pause('')
							item += 1
						else:
							print('[{}]  ' . format('✔') + value['sum'])
							pause('')
							item += 1
					print()

def completeTask(taskKey):
	if len(playerTasks) > 0:
		for day in range(len(playerTasks)):
			if day == today:
				if len(playerTasks[day]) > 0:
					for key in playerTasks[day].keys():
						if key == taskKey:
							if playerTasks[day][key]['done'] == False:
								playerTasks[day][key]['done'] = True
								print('[C]  You have completed task [{}]!' . format(int(key)+ 1))
								print()

def isTaskDone():
	if len(playerTasks) > 0:
		for day in range(len(playerTasks)):
			if day == today:
				if len(playerTasks[day]) > 0:
					for key, value in playerTasks[day].items():
						if value['nom'] == 'a' and value['done'] == False:
							if 'paper' in inventory:
								completeTask(key)
								break
						elif value['nom'] == 'b' and value['done'] == False:
							if 'stapler' in inventory:
								completeTask(key)
								break

def countTasksDone():
	count = 0
	if len(playerTasks) > 0:
		for day in range(len(playerTasks)):
			if len(playerTasks[day]) > 0:
				for key in playerTasks[day].keys():
					if playerTasks[day][key]['done'] == True:
						count += 1
	return count

def countTasks():
	count = 0
	if len(playerTasks) > 0:
		for day in range(len(playerTasks)):
			if len(playerTasks[day]) > 0:
				for key in playerTasks[day].keys():
					count += 1
	return count

# Ask them a question
def ask(string = '', valid = []):

	print('\n[!]  ACTION NEEDED')
	print('[Q]  ' + string)
	asking = input('[I]  ')

	while asking.upper() not in valid:
		print('[X]  ERROR: You can\'t do that now.')
		print()
		print('\n[!]  ACTION NEEDED')
		print('[Q]  ' + string)
		asking = input('[I]  ')
	return asking

## ACTIONS

# Pick Up Item
def itemUp( name, feedback = False):
	if name.lower() not in inventory:
		if name.upper() == 'PAPER':
			itemsForPickUp['paper']['inInventory'] = True
			inventory.append(name)
			if feedback:
				pretty('You have picked up the paper.')
		elif name.upper() == 'STAPLER':
			itemsForPickUp['paper']['inInventory'] = True
			inventory.append(name)
			if feedback:
				pretty('You have picked up the stapler.')
		isTaskDone()
		return True
	else:
		pretty('You cannot pick that up. You already have it.')
		return False

# Put Down Item
def itemDown( name, feedback = False ):
	if name.lower() in inventory:
		if name.upper() == 'PAPER':
			itemsForPickUp['paper']['inInventory'] = False
			inventory.remove(name)
			if feedback:
				pretty('You have put down the paper.')
		elif name.upper() == 'STAPLER':
			itemsForPickUp['stapler']['inInventory'] = False
			inventory.remove(name)
			if feedback:
				pretty('You have put down the stapler.')
		return True
	else:
		pretty('You cannot put that down. You aren\'t holding it.')
		return False

# Process User input
def processInput(command, feedback = False):
	cmd = command.upper()
	if cmd == 'Y' or cmd == 'YES':
		return True
	elif cmd == 'N' or cmd == 'NO':
		return False
	elif cmd == 'PAPER UP':
		itemUp('paper', feedback)
	elif cmd == 'PAPER DOWN':
		itemDown('paper', feedback)
	elif cmd == 'STAPLER UP':
		itemUp('stapler', feedback)
	elif cmd == 'STAPLER DOWN':
		itemDown('stapler', feedback)
	else:
		return 'none'

# ===================================================
# MAIN
# ===================================================

# main game loop
def main():
	global today, keepGoing

	intro()
	pause('')
	pause('d1')

	print()
	print('[!]  ACTION NEEDED')
	input('[Q]  To read how to play, press the ENTER key.  ')
	instructions()

	b = ask('To begin playing, input *START or *S.', ['START', 'S'])
	if b.upper() == 'START' or b.upper() == 'S':
		keepGoing = True

	# day
	while keepGoing:
		
		while len(inventory) > 0:
			itemDown(inventory[0])

		if today == 0:
			content = Monday
		elif today == 1:
			content = Wednesday
		else:
			content = Friday

		print()
		print('--------------------')
		print()
		pause('')
		pretty('Today is ...')
		pause('')
		for line in content:
			print(line)
			pause('drip')

		pause('')
		pretty('It is time for work.')
		print()
		pause('')

		pretty('You arrive at the office and enter your cubicle.')
		print()
		pause('')

		pretty('You glance at your calendar. You have 2 tasks due today.')
		print()

		assignTasks(today)
		displayTasks()
		
		pretty('You may complete them in any order.')
		print()
		pause('')
		
		while countTasksDone() < countTasks():
			pretty('You can:')
			print('*A   --   pick up paper')
			print('*B   --   put down paper')
			print('*C   --   pick up stapler')
			print('*D   --   put down stapler')
			print('*E   --   take a nap')

			do = ask('What would you like to do?', ['A', 'B', 'C', 'D', 'E'])
			if do.upper() == 'A':
				processInput('paper up', True)
				print()
			elif do.upper() == 'B':
				processInput('paper down', True)
				print()
			elif do.upper() == 'C':
				processInput('stapler up', True)
				print()
			elif do.upper() == 'D':
				processInput('stapler down', True)
				print()
			else:
				print()
				pretty('You took a nap.')
				break

			displayTasks()

		## The end of the day!
		print('[!]  You have made it to the end of today\'s work time.')
		print()
		pause('')
		
		## 
		num = (len(workdays) - 1) - today
		if num > 0:
			print('[!]  You have {} more possible work days this week.' . format(num))
			z = ask('Do you want to work another day? *Y or *N', ['Y', 'YES', 'N', 'NO'])
			if processInput(z) == False:
				keepGoing = False
				winLoseDraw()
				break
			else:
				today = today + 1
		else:
			keepGoing = False
			winLoseDraw()
			break
	
	for line in GameName:
		print(line)
		pause('drip')
	print(' . \n. GOOD BYE\n.')

if __name__ == "__main__":
    main()
