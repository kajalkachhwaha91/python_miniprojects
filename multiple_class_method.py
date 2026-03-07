class Songs:
    def __init__(self, name):
        self.name = name
        self.songs = [] 

    def add_songs(self, song):
        self.songs.append(song)
    
    def show_song(self):
        print("Songs in the playlist:")
        for song in self.songs:
            print(song)
    
    def delete_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"{song} has been removed from the playlist.")
        else:
            print(f"{song} is not in the playlist.")

s1 = Songs("My Playlist")
s1.add_songs("Song 1")
s1.add_songs("Song 2")  
s1.show_song()
s1.delete_song("Song 1")
s1.show_song()