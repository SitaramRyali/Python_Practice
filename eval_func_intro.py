#eval function definition and usage.
#resources https://www.geeksforgeeks.org/eval-in-python/

#he eval() method parses the expression passed to it and runs python expression(code) within the program.
from math import *

def secret_function(): 
	return "Secret key is 1234"

def function_creator(): 

	# expression to be evaluated 
	expr = input("Enter the function(in terms of x):") 

	# variable used in expression 
	x = int(input("Enter the value of x:")) 

	# evaluating expression 
	y = eval(expr) 

	# printing evaluated result 
	print("y = {}".format(y)) 

if __name__ == "__main__": 
	function_creator() 
