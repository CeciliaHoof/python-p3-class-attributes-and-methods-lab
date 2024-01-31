class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.genre = genre
        self.artist = artist

        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
       
    def add_song_to_count():
        Song.count += 1
    
    def add_to_genres(new_genre):
        if new_genre not in Song.genres:
            Song.genres.append(new_genre)
    
    def add_to_artists(new_artist):
        if new_artist not in Song.artists:
            Song.artists.append(new_artist)

    def add_to_genre_count(genre):
        if genre not in Song.genre_count.keys():
            Song.genre_count[genre] = 1
        else:
            Song.genre_count[genre] += 1
    
    def add_to_artist_count(artist):
        if artist not in Song.artist_count.keys():
            Song.artist_count[artist] = 1
        else:
            Song.artist_count[artist] += 1