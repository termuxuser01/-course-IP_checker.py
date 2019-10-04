class Song:
    def __init__(self, tittle, artist=None, duration=0):
        self.tittle = tittle
        self.duration = duration
        if artist == None:
            self.artist = Artist("various artists")
        else:
            self.artist = artist

class Album:
    def __init__(self, year=0, name=None):
        self.tracks = {}
        self.year = year

    def add_track(self, song, track_no=None):
        if track_no == None:
            self.tracks[len(self.tracks + 1)] = song.tittle
        else:
            self.tracks[track_no] = song.tittle




class Artist:
    def __init__(self, name, bday=None):
        self.name = name
        self.bday = bday
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def get_alnums(self):
        for a in self.albums:
            print(a)


if __name__ == "__main__":
    welcome = Song("welcome")

    print(welcome.artist.name)

    a = Album(1997, "a7x")

    a.add_track(welcome, 5)
    # print(a.tracks)

    welcome.artist.add_album(a)

    welcome.artist.get_alnums()