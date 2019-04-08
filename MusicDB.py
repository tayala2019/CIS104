#Tamishia Ayala
#04/08/2019

import json
import os.path

#class genre (Enum)
	#  Blues = 1
   # Country = 2
	 # Electronic = 3
	 # Folk = 4
	 # HipHop = 5
	 # Jazz = 6
	 # Latin = 7
	 # Pop = 8

song = {}
songAdded = False
  # function to display the main Menu
def DisplayMenu():
    print("Select operation.")
    print("add – Add a new song to the database")
    print("list – List the songs in the database")
    print("save – Save the songs to the database")
    print("sort – Sort the songs to the database")
    print("total – Get total number of songs in the database")
    print("info – Get the information about a particular song in the database")
    print("help – Display a menu explaining the commands to the users")
    print("exit – Exit the program")


# function to add the song 
def AddSong():
  global songAdded 
  songAdded = True
  global song

  # Taking input for song title and checking should not exceed 64 char
  song_title = input("Please enter song title : ")  
  while True :
    if(len(song_title) <=64):
      print('\n')
      break
    else:
      print("Title cannot exceed 64 characters")
      song_title = input("Please enter song title : ")

   # Taking input for Artist and checking should not exceed 32 char
  artist = input("Enter Artist: ")  
  while True:
    if (len(artist) <=32):
      print('\n')
      break
    else:
      print("Artist cannot exceed 32 characters ")
      artist = input("Enter Artist: ")

   # Taking input for Album and checking should not exceed 64 char
  album = input("Enter Album: ") 
  while True :
    if (len(album) <= 64):
      print('\n')
      break
    else:
      print("Album cannot exceed 64 chracters ")
      album = input("Enter Album: ")

  track_number = int(input("Enter the Track_number: "))   # input for track number
  released_year = int(input("Enter the Released_year: ")) #input for released year
  genre = input("Enter Genre: ")      #input for Genre

  # create a song record
  song = dict(Song_title = song_title, Artist = artist, Album = album, Track_number = track_number, Released_year = released_year, Genre = genre) 



   # function for listing the song
def SongList():
  if(os.path.exists('Song_DB.json')):  # checking is there any song in the database
    songs_list = json.load(open('Song_DB.json'))
    print("The list of Songs are: " , songs_list)
  else:
    print("Song database doesn't exist")

#function to sort the song
def SongSort():
  if(os.path.exists('Song_DB.json')):  
    songs_list = json.load(open('Song_DB.json'))
    songs_list = sorted(songs_list, key=lambda k: k.get('Song_title', 0), reverse=False)
    print("The  sorted list are: " , songs_list)
    
   #function to save the song
def SongSave():
  global song
  global songAdded
  if(songAdded):
    # array to store songs
    songArr = []
    #Check if File exist before opening and loading the data

    if(os.path.exists('Song_DB.json')):
      with open('Song_DB.json') as f:
        # Load the existing songs from file
        data = json.load(f)
        # Add those songs to the song Array
        for songdata in data:
          songArr.append(songdata)  

    # Now add the new song to the existing songs in the song array
    songArr.append(song)

    with open('Song_DB.json', 'w') as f:
      json.dump(songArr, f)
  
    song = {}
  else:
    print("Please add a song first")
  
  songAdded = False


# Function for Help Menu
def Help():
  DisplayMenu()


  #Function to get total song
def GetTotalSongs():
  print("Song Path:::",os.path)
  if(os.path.exists('Song_DB.json')): # checking is there a song in the database and calculate count
    songs_list = json.load(open('Song_DB.json'))
    print("Total songs in database::",len(songs_list))
  else:
    print("Song database doesn't exist")
 
  #Function to get song information
def GetSongInformation(songNumber):
  if(songNumber > 8 or songNumber < 1):
    print("Enter a correct Song Number to get the information")
  else:  
    if(os.path.exists('Song_DB.json')):
      songs_list = json.load(open('Song_DB.json'))
      print(songs_list[songNumber-1])
    else:
      print("Song database doesn't exist")