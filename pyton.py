#!/usr/bin/env python 
# - *- coding: utf- 8 - *-
def Bisiestos():
	x =int(input("año:"))
	y = x % 4
	y100=x% 100
	y400=x%400
	if y ==0:
		print ("Es bisiesto")
	elif y100 ==0:
		print("Es Bisiesto")
	elif y400 ==0:
		print("Es Bisiesto")
	else:
	    print("No es Bisiesto")
    
    		
	
	
Bisiestos()
