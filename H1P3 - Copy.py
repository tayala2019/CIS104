#Tamishia Ayala
#Date: 01/27/2019
#This program will promt the user to enter coin count
#will then display the users input coin count

Pennies = input ('How many pennies do you have (1-cent coins): ')
sPennies = int(Pennies )
Nickels = input ('\nHow many nickels do you have (5-cent coins): ')
sNickels= int(Nickels)
Dimes = input ('\nHow many dimes do you have (10-cent coins): ')
sDimes= int(Dimes)
Quarters = input ('\nHow many quarters do you have (25-cent coins): ')
sQuarters= int(Quarters)
Halfdollars = input ('\nHow many half dollars do you have (50-cent coins): ')
sHalfdollars= int(Halfdollars)
OneDollars = input ('\nHow many dollars do you have (100-cent coins): ')
sOneDollars = int(OneDollars)
print('------------------------------------------------------------------\n')

if sPennies ==1:
    print ('\nYou have '+str(sPennies)+' penny.')
else:
    print ('\nYou have '+str(sPennies)+' pennies.')
#end pennies
#------------------------------------------------------------------------------
if sNickels == 1:
    print ('\nYou have '+str(sNickels)+' nickel.')
else:
    print ('\nYou have '+str(sNickels)+' nickels.')
#end nickels
#------------------------------------------------------------------------------
if sDimes==1:
    print ('\nYou have '+str(sDimes)+' dime.')
else:
    print ('\nYou have '+str(sDimes)+' dimes.')
#end nickels
#------------------------------------------------------------------------------
if sQuarters ==1:
    print ('\nYou have '+str(sQuarters)+' Quarter.')
else:
    print ('\nYou have '+str(sQuarters)+' Quarters.')
 #end quarters
#------------------------------------------------------------------------------
if sHalfdollars==1:
    print ('\nYou have '+str(sHalfdollars)+' half dollar.')
else:
    print ('\nYou have '+str(sHalfdollars)+' half dollars.')
 #end half dollars
#------------------------------------------------------------------------------
if sOneDollars ==1:
    print ('\nYou have '+str(sOneDollars)+' dollar.')
else:
    print ('\nYou have '+str(sOneDollars)+' dollars.')
 #end half dollars
#------------------------------------------------------------------------------
def sSumCoinAcount (a,b,c,d,e,f):
    sCoinSum=((1.0 * f) + (0.50 * e) + (0.25 * d) + (0.10 * c) +(0.05 * b )+(0.01 * a))
    return '${:,.2f}'.format(sCoinSum)

print('\nThe value of all your coins: '+str(sSumCoinAcount(sPennies,sNickels,sDimes,sQuarters,sHalfdollars,sOneDollars)))

