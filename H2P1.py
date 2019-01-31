#Tamishia Ayala
#Date: 01/29/2019
#This program will 1:get users age and add 10 years and 2: convert Farenheit to Celcius

#get user input
sAge = input ("Hello, please enter you age: ")
lAge = int(sAge)
sAgeInTenYears = str (lAge + 10)
print ('In 10 years you will be '+ sAgeInTenYears + ' years old')
print('\n')
print('***********************************************************')
print('\n')
sTemp = input('Please enter temperature in degrees farenheit: ')
lTemp = float(sTemp)

#function to calculate degress Farenheit to celcius
def degreeCel(t):
    c = ((t - 32) * 5 / 9)
    return c

celTemp = degreeCel(lTemp)
print ('The Celcius temperature is '+ str(celTemp))


