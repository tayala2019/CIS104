#Tamishia Ayala
#04/08/2019
import MusicDB 

MusicDB.DisplayMenu()
while(True):

     choice = input("Enter your choice: ") # taking a choice
     if choice == 'add':
          MusicDB.AddSong()
          continue
     elif choice == 'list':  
          MusicDB.SongList()
          continue
     elif choice == 'save':   
          MusicDB.SongSave() 
          continue
     elif choice == 'total':   
          MusicDB.GetTotalSongs() 
          continue
     elif choice == 'info':
          songInput = int(input("Enter the Song Number"))  
          MusicDB.GetSongInformation(songInput) 
          continue
     elif choice == 'help':
          MusicDB.Help()
     elif choice == 'sort':
          MusicDB.SongSort()
     elif choice == 'exit':
          break
     else:
          print("Invalid Choice")  