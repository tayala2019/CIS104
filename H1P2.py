#Tamishia Ayala
#Date: 01/27/2019
#This program will prompt the user to enter miles and then convert the user input (miles)to kilometers


sMiles = input ('Enter miles: ')
float_KMs = float (sMiles)

def sMilestoKilometers (x):
    c = 1.609  * x
    return c

Kilom = sMilestoKilometers(float_KMs)
print ('Kilometers are ' + str(Kilom))
