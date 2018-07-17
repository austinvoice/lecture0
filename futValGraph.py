# Future value of an investment shown in a graph

from graphics import *

def main():
	# Introduction
	print("This program plots the growth of a 10-year investnment.")

	# Get principal and interest rate
	principal = float(input("Enter the intial principal: "))
	apr = float(input("Enter the annualized rate: "))

	#Create a graphics window with labels on left edge
	win = GraphWin('Investment Growth Chart', 320, 240)
	win.setBackground('White')
	Text(Point(20, 230), '0.0K').draw(win)
	Text(Point(20, 180), '2.5K').draw(win)
	Text(Point(20, 130), '5.0K').draw(win)
	Text(Point(20, 80), '7.5K').draw(win)
	Text(Point(20, 30), '10.0K').draw(win)

	# Draw bar for initial principal
	height = principal * .02
	bar = Rectangle(Point(20, 230), Point(65, 230-height))
	bar.setFill('green')
	bar.setWidth(2)
	bar.draw(win)


main()
