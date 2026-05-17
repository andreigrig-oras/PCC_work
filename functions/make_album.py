def make_album (artist_name, album_name, no_songs=None):
    album={"artist":artist_name, "name":album_name}
    if no_songs:
        album['number']=no_songs
    return album

while True:
    print("Enter 'q' at any time to exit the application!")
    art=input ("What is the name of the artist?\n")
    if art == "q": break
    nam=input ("What is the name of the album:?\n")
    if nam == "q": break
    print (f"Your album details are as follows:{make_album(art,nam)}")