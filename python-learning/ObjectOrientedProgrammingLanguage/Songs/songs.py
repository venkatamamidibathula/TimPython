class Song():
    """ Songs class for defining the objects inside the class Song.
        Attributes:
            title(str): The title of song which is a string attribute
            artist(Artist): The artist which itself is an Artist objects
            duration(int): The duration of song or the time it plays for
    """

    def __init__(self, title,artist,duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

class Album():
    """This class represents an album class
       Attributes:
            name(str)= name of Album
            year(int) = year value which is integer
            artist(Artist) = Artist object if none specified it will be various artists
            tracks[] = list of tracks
    """
    def __init__(self,name,year,artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "various artists"
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """ Adds a song to list of Songs
            if position is not specified it will be appended to list of Songs
            if position is specified it will be inserted at the position at which it was specified
            Args:
                song(Song): A song to add.
                position(Optional[int]): If specified the song will be added to that position if not it will be appended at the end of songs list
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(poistion,song)

class Artist():
    """This class defines the artist where he has a name and an album
        Attributes:
            name(str): name of the artists
            album(list[Album]): List of all the albums that the artist has
    """
    def __init__(self, name):
        self.name = name
        self.albums = []
    def add_album(self,album):
        """ This method accepts album for each artists and appends it to album
            Attributes:
                album(Album): Album object to be appended to albums list
        """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    arist_list = []
    with open('albums.txt','r') as albums:
        for line in albums:
            artist_field,album_field,year_field,song_field=tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field,album_field,year_field,song_field)
            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                new_artist.add_album(album_field)
                arist_list.append(new_artist)
                new_artist = Artist(artist_field)




if __name__== '__main__':
    load_data()
