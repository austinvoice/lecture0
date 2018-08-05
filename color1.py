# event-driven UI changes

from graphics import *

def handleKey(k, win):
	if k == "r":
		win.setBackground("pink")
	elif k == "w":
		win.setBackground("white")
	elif k == "g":
		win.setBackground("lightgray")
	elif k == "b":
		win.setBackground("lightblue")

def handleClick(pt, win):
	# create an entry for user to type in
	entry = Entry(pt, 10)
	entry.draw(win)

	# go modal: loop until user types <Enter>
	while True:
		key = win.getKey()
		if key == "Return": break

	# undraw the entry and create a draw Text0
	entry.undraw()
	typed = entry.getText()
	Text(pt, typed).draw(win)

	# clear/ignore mouse clicks during the text entry
	win.checkMouse()


def main():
	win = GraphWin("Color Window", 500, 500)

	# event loop: handle key presses and mouse clicks until user presses the "q" key
	while True:
		key = win.checkKey()
		if key == "q": # loop exit
			break

		if key:
			handleKey(key, win)

		pt = win.checkMouse()
		if pt:
			handleClick(pt, win)

	# exit program
	win.close()

main()
