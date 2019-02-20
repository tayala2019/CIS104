import calculator
import math
import sys 
import os


repeat = True
while repeat:
    print ("What calculation would you like to perform: ")
    print ("1: Addition")
    print ("2: Subtraction")
    print ("3: Multiplication")
    print ("4: Division")
    print ("5: Srqt")
    print ("6: Power")
    print ("7: Quit")   
       
    #Capture the menu choice.
    choice = input()   
             
    if choice == "1":
        Num1 = int(input("Enter your first number: "))
        Num2 = int(input("Enter your second number: "))
        print ('Your result is:'+ str(calculator.add(Num1,Num2)))
    elif choice == "2":
        Num1 = int(input("Enter your first number: "))
        Num2 = int(input("Enter your second number: "))
        print ('Your result is:'+ str(calculator.sub(Num1,Num2)))
    elif choice == "3":
        Num1 = int(input("Enter your first number: "))
        Num2 = int(input("Enter your second number: "))
        print ('Your result is:'+ str(calculator.multi(Num1,Num2)))
    elif choice == "4":
        Num1 = int(input("Enter your first number: "))
        Num2 = int(input("Enter your second number: "))
        print ('Your result is:'+ str(calculator.div(Num1,Num2)))
    elif choice == "5":
        Num1 = int(input("Enter your first number: "))
        print ('Your result is:'+ str(calculator.square(Num1)))
    elif choice == "6":
        Num1 = int(input("Enter your first number: "))
        Num2 = int(input("Enter raised to the power of: "))
        print ('Your result is:'+ str(calculator.power(Num1,Num2)))
    elif choice == "7":
        print ('Your result is:'+ str(calculator.clearMemory()))
else:
    print ('Choice is invalid.')
   
