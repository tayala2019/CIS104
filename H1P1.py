#Tamishia Ayala
#Date: 01/27/2019
#This program  prompts the user for a few bits of information about themselves and outputs a greeting to the console

firstName = input ('Please enter your first name:  ');
lastName = input ('\nPlease enter your last name: ');
age = input ('\nPlease enter your age: ');
intAge =int(age)

def return_age(x):
 c =  7 * x
 return c

sConfidenceInProgrammers = input ('\nPlease express your confidence in programmers between 0-100%: ');
float_confidence = float (sConfidenceInProgrammers)
def sConfidence(x):
    if x < 51:
        return "\nI agree, programmers cant be trusted.\n"
    if x > 51:
        return "\nWriting good code takes hard work.\n"

    
sDogYears= return_age(intAge)
sConfProg = sConfidence(float_confidence)
#print (sDogYears);
print ('\nHello ' +firstName +' '  +lastName + ' nice to meet you! You might be \n' + age+' in human years, but in dog years you are '+str(sDogYears)+'.' );
print (str(sConfProg))



