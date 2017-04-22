import song


class Playlist:
    """ A playlist of songs """

    def __init__(self, title):
        """ (Playlist, title) -> NoneType
        
        A Playlist of songs tittled title.
        
        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.title
        'Canadian Artists'
        >>> playlist.songs
        []
        """

        self.title = title
        self.songs = []

    def add(self, song):
        """ (Playlist, Song) -> NoneType
        
        Add song to the playlist.
        
        >>> stompa = song.Song('Serena Ryder', 'Stompa', 3, 15)
        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.add(stompa)
        >>> playlist.songs[0] == stompa
        True
        """

        self.songs.append(song)

    def get_duration(self):
        """ (Playlist) -> tuple of (int, int)
            
        Return the total duration of the playlist as a tuple of minutes and seconds.
        
        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.add(song.Song('Serena Ryder', 'Stompa', 3, 15))
        >>> playlist.add(song.Song('Neil Young', 'Harvest Moon', 5, 3))
        >>> playlist.get_duration()
        (8, 18)
        """

        # Initialize total minutes and seconds variable to zero

        total_minutes = 0
        total_seconds = 0

        for song in self.songs:
            total_minutes += song.minutes
            total_seconds += song.seconds

        # Adding extra seconds to total_minutes

        if total_seconds > 59:
            total_minutes += total_seconds // 60
            total_seconds %= 60

        return total_minutes, total_seconds

    def __str__(self):
        """ (Playlist) -> str
        
        Return string representation of the playlist.
        
        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.add(song.Song('Serena Ryder', 'Stompa', 3, 15))
        >>> playlist.add(song.Song('Neil Young', 'Harvest Moon', 5, 3))
        >>> str(playlist)
        '''Canadian Artists (8:18)
        1. Serena Ryder, Stompa (3:15)
        2. Neil Young, Harvest Moon (5:03)'''
        """

        duration = self.get_duration()
        minutes = str(duration[0])
        seconds = str(duration[1]).rjust(2, '0')

        result = self.title + ' (' + minutes + ':' + seconds + ')'

        song_num = 1
        for song in self.songs:
            result += '\n' + str(song_num) + '. ' + str(song)
            song_num += 1

        return result

if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    playlist = Playlist('Canadian Artists')
    playlist.add(song.Song('Serena Ryder', 'Stompa', 3, 15))
    playlist.add(song.Song('Neil Young', 'Harvest Moon', 5, 3))
    print(playlist)
