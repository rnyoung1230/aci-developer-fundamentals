# e-learning Lab: Classes and Objects
# ------------------------

# Task 1: Create a music catalog

class Artist:
    # Instance variables and methods
    def __init__(self, artist_name=None):
        self.name = artist_name
        self.albums = []

    def __str__(self):
        return f"\nArtist Name: {self.name}\n" \
               f"Albums:\n{self.albums}\n"

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
        self.artist = artist
        self.tracks = album_tracks

        runtime = 0
        if album_tracks is not None:
            for track in album_tracks:
                runtime += track.length

        self.runtime = runtime

    def __str__(self):
        return f"\nAlbum Name: {self.name}\n" \
               f"Artist: {self.artist.name}\n" \
               f"Total Runtime: {self.runtime} minutes\n" \
               f"\nTracks:\n{'\n'.join(str(track) for track in self.tracks)}"

class Track:
    # Instance variables and methods
    def __init__(self, artist=None, track_name=None, track_number=0, track_length=0):
        self.artist = artist
        self.name = track_name
        self.number = track_number
        self.length = track_length

    def __str__(self):
        return f"Track Number: {self.number} " \
               f"Track Name: {self.name} " \
               f"Track Length: {self.length} minutes"

            ################################ TEST CODE ################################
new_artist = Artist("Prince")

tracks_a1 = []
track_1 = new_artist.record_track("Let's Go Crazy", 1, 280)
track_9 = new_artist.record_track("Purple Rain", 9, 521)

tracks_a1.append(track_1)
tracks_a1.append(track_9)

album_1 = new_artist.make_album("Purple Rain", tracks_a1)

print("")
print("TESTING ALBUM CREATION", album_1)
print(f"-------------------------------------------------------------\n")
print(f"TESTING TRACK CREATION\n{'\n'.join(str(track) for track in tracks_a1)}")
print(f"-------------------------------------------------------------\n")

tracks_a2 = []
track_3 = new_artist.record_track("Diamonds and Pearls", 3, 285)
track_4 = new_artist.record_track("Cream", 4, 253)

tracks_a2.append(track_3)
tracks_a2.append(track_4)

album_2 = new_artist.make_album("Diamonds and Pearls", tracks_a2)

print("TESTING ALBUM CREATION", album_2)
print(f"-------------------------------------------------------------\n")
print(f"TESTING TRACK CREATION\n{'\n'.join(str(track) for track in tracks_a2)}")
print(f"-------------------------------------------------------------\n")

print(f"TESTING ARTIST SUMMARY\nArtist: {new_artist.name}"
      f"\nAlbums:\n{'\n'.join(f'{album.name} (Runtime: {album.runtime} minutes)' for album in new_artist.albums)}")