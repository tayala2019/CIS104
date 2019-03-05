<<<<<<< HEAD
#Tamishia Ayala
import calculator
import math
import sys 
import os


repeat = True
while repeat:
    print ("\nWhat calculation would you like to perform: \n")
    print ("1: Addition")
    print ("2: Subtraction")
    print ("3: Multiplication")
    print ("4: Division")
    print ("5: Srqt")
    print ("6: Power")
    print ("7: Clear Value")   
    print('\n')  
    choice = input()   
    
             
    if choice == "1":
        Num1 = int(input("Enter your first number: "))
        Num2 = int(input("Enter your second number: "))
        calculator.memoryVal = calculator.add(Num1,Num2)
        print ('Your result is:'+ str(calculator.memoryVal))
        
    elif choice == "2":
        Num1 = int(input("Enter your first number: "))
        Num2 = int(input("Enter your second number: "))
        calculator.memoryVal = calculator.sub(Num1,Num2)
        print ('Your result is:'+ str(calculator.memoryVal))
    elif choice == "3":
        Num1 = int(input("Enter your first number: "))
        Num2 = int(input("Enter your second number: "))
        calculator.memoryVal = calculator.multi(Num1,Num2)
        print ('Your result is:'+ str(calculator.memoryVal))
    elif choice == "4":
        Num1 = int(input("Enter your first number: "))
        Num2 = int(input("Enter your second number: "))
        calculator.memoryVal = calculator.div(Num1,Num2)
        print ('Your result is:'+ str(calculator.memoryVal))
    elif choice == "5":
        Num1 = int(input("Enter your first number: "))
        calculator.memoryVal = calculator.square(Num1)
        print ('Your result is:'+ str(calculator.memoryVal))
    elif choice == "6":
        Num1 = int(input("Enter your first number: "))
        Num2 = int(input("Enter raised to the power of: "))
        calculator.memoryVal = calculator.power(Num1,Num2)
        print ('Your result is:'+ str(calculator.memoryVal))
    elif choice == "7":
        print ('Your result is:'+ str(calculator.clearMem()))
else:
    print ('Invalid choice.')
   
