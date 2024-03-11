class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        self.song_add()
        self.genre_add(genre)
        self.artists_plus(artist)
        self.genre_add_count(genre)
        self.artist_plus_count(artist)

    @classmethod
    def song_add(cls):
        cls.count += 1

    @classmethod
    def genre_add(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def artists_plus(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def genre_add_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def artist_plus_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1