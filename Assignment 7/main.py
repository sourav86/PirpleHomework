"""
List down the attributes of my favorite song and print their values using dictionaries
"""
#Create a dictionary variable
FavSongAttributes = {}
#Favorite Song Name
FavSongAttributes["song"] = "My Heart Will Go On"

#Singer Name
FavSongAttributes["artist"] = "Celine Dion"

#Song Writer Name
FavSongAttributes["writer"] = "James Horner"

#Song Release Date
FavSongAttributes["releaseDate"] = "December 8, 1997"

#Song Recorded Date
FavSongAttributes["recordedDate"] = "May 22, 1997"

#Song Genre
FavSongAttributes["genre"] = "Pop"

#Release Type
FavSongAttributes["releaseType"] = "Single"

#Album Name
FavSongAttributes["albumName"] = "Let's Talk About Love"

#Song Duration in Seconds
FavSongAttributes["durationInSeconds"] = 311

#No of Copies Sold World Wide
FavSongAttributes["noOfCopiesSold"] = 18000000

#Name of the awards won by this song
FavSongAttributes["awardsWon"] = "Academy Awards, Golden Globe Awards, Satellite Awards"

#Describes the spectrum of emotions in music 
FavSongAttributes["valence"] = "Happy to Sad"

#Song Rating
FavSongAttributes["rating"] = 9.5

#Printing all the attributes and values as key and value combinition

for key in FavSongAttributes:
    print("Key = {} and Value = {} ".format(key,FavSongAttributes[key]))


def ValidateUserGuess(Key,Value):
    if Key in FavSongAttributes:
        if (str(FavSongAttributes[Key]) == str(Value)):
            return True
        else:
            return False
    else:
        return False
_key = input("Provide key: ")
_value = input("Provide key value: ")
print(ValidateUserGuess(_key,_value))






