class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.genres.append(genre)
        Song.artists.append(artist)
        Song.add_to_genres()
        Song.add_to_artists()
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        unique_genres = []
        for genre in cls.genres:
            if genre not in unique_genres:
                unique_genres.append(genre)
        cls.genres = unique_genres

    @classmethod
    def add_to_artists(cls):
        unique_artists = []
        for artist in cls.artists:
            if artist not in unique_artists:
                unique_artists.append(artist)
        cls.artists = unique_artists

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1