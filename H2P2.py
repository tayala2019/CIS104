#Tamishia Ayala
#Date 01/29/2019
#This program will prompt the user book information
import datetime
import time

#get user input
sBookTitle = input('Please enter the title of the book: ')
lBookTitle = str (sBookTitle)
sBookAuthor = input('Please enter the book author: ')
lsBookAuthor = str (sBookAuthor)
sBookPublished = input('What year was the book published: ')
lBookPublished = int (sBookPublished)
sBookPages = input('Please enter the number of pages in the book: ')
lBookPages = int (sBookPages)

#function to calculate the age of the book
def getBookAge (x):
    sGetYear = datetime.datetime.today().year
    c = sGetYear - x
    if c < 10 :
        return ('\nThis book is younger than 10 years old.\n')
    else:
        return ('\nThis book is at least 10 years old.\n')
    
print (str(getBookAge(lBookPublished)))
#End Function getBookAge


#function to get number of pages in the book
def getBookPages (x):
     
    
    if x < 100 :
        return ('This book is a short book.\n')
    elif x >= 100 and x <= 300 :
        return ('This book is a medium book.\n')
    else: 
        return ('This book is a long book.\n')
  
print (str(getBookPages(lBookPages)))
 #End Function getBookPages  