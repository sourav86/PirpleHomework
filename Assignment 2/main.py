"""
Assignment #2 : it displays the value of song's name,artist name and writer name
via function
"""

#Return song name
def song():
    song = "My Heart Will Go On"
    return song

#Return artist name
def artist():
    artist = "Celine Dion"
    return artist

#Return writer name
def writer():
    writer = "James Horner"
    return writer


#Take user choice
#Either song or artist or writer is allowed as value
choice = input('\n\n Enter your choice(***only song,artist and writer allowed as choice) : ')

if choice.lower() == 'song' :
    print(song())
elif choice.lower() == 'artist':
    print(artist())
elif choice.lower() == 'writer':
    print(writer())
else:
    print("Invalid Choice ! Provide proper choice and execute again")
