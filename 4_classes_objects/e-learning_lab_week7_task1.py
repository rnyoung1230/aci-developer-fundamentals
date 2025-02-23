# e-learning Lab: Classes and Objects
# ------------------------

# Task 1: Create a music catalog --> Practices using Associations

class Artist:
    # Instance variables and methods
    def __init__(self, artist_name=None):
        self.name = artist_name
        self.albums = []

    def __str__(self):
        artist_info = f"Artist Name: {self.name}\n"

        if len(self.albums) > 0:
            artist_info += f"\nAlbums:\n{'\n'.join(str(album) for album in self.albums)}"

        return artist_info

    def make_album(self, album_name=None, album_tracks=None):
        album = Album(self, album_name, album_tracks)
        self.albums.append(album)
        return album

    def record_track(self, track_name=None, number=0, length=0):
        track = Track(self.name, track_name, number, length)
        return track

class Album:
    # Instance variables and methods
    def __init__(self, artist=None, album_name=None, album_tracks=None):
        self.name = album_name
        self.artist = artist # Association
        self.tracks = album_tracks

        runtime = 0
        if album_tracks is not None:
            for track in album_tracks:
                runtime += track.length

        self.runtime = runtime

    def __str__(self):
        return f"Album Name: {self.name}\n" \
               f"Artist: {self.artist.name}\n" \
               f"Total Runtime: {self.runtime} minutes\n" \
               f"\nTracks:\n{'\n'.join(str(track) for track in self.tracks)}\n"

class Track:
    # Instance variables and methods
    def __init__(self, artist_name=None, track_name=None, track_number=0, track_length=0):
        self.artist_name = artist_name
        self.name = track_name
        self.number = track_number
        self.length = track_length

    def __str__(self):
        return f"Track Number: {self.number} " \
               f"Track Name: {self.name} " \
               f"Track Length: {self.length} minutes"

            ################################ TEST CODE ################################
new_artist = Artist("Prince")
print(new_artist)

tracks_a1 = []
track_1 = new_artist.record_track("Let's Go Crazy", 1, 280)
track_9 = new_artist.record_track("Purple Rain", 9, 521)

tracks_a1.append(track_1)
tracks_a1.append(track_9)
print(f"TESTING TRACK CREATION 1\n{'\n'.join(str(track) for track in tracks_a1)}")
print(f"-------------------------------------------------------------\n")

a1 = new_artist.make_album("Purple Rain", tracks_a1)
print(f"TESTING ALBUM CREATION 1\n{a1}")
print(f"-------------------------------------------------------------\n")


tracks_a2 = []
track_3 = new_artist.record_track("Diamonds and Pearls", 3, 285)
track_4 = new_artist.record_track("Cream", 4, 253)

tracks_a2.append(track_3)
tracks_a2.append(track_4)
print(f"TESTING TRACK CREATION 2\n{'\n'.join(str(track) for track in tracks_a2)}")
print(f"-------------------------------------------------------------\n")

a2 = new_artist.make_album("Diamonds and Pearls", tracks_a2)
print(f"TESTING ALBUM CREATION 2\n{a2}")
print(f"-------------------------------------------------------------\n")

print(f"TESTING ARTIST SUMMARY - SHORT\nArtist: {new_artist.name}"
      f"\nAlbums:\n{'\n'.join(f'{album.name} (Runtime: {album.runtime} minutes)' for album in new_artist.albums)}\n")
print(f"-------------------------------------------------------------\n")
print(f"TESTING ARTIST SUMMARY - LONG\n{new_artist}")
