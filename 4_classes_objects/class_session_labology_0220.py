# LABOLOGY SESSION - 2/20
# ------------------------

# Associations and Inheritance

class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.miles_traveled = 0

    def move_forward(self, miles):
        pass

    def read_miles(self):
        pass

    def info(self):
        pass

    def fill_gas(self):
        pass

class ElectricCar:

    def __init__(self, car, battery):
        self.car = car
        self.battery = battery


# ################################## TESTING CODE #########################################
#
# car_1 = Car("Toyota", "4-Runner", 2024, "Black")
# electric_car_1 = ElectricCar(car_1, 120)  #kilowatt hours (120 kWh)

# Lab Task 1:  Music Catalog exercise

class Artist:
    def __init__(self, artist_name):
        self.name = artist_name
        self.albums = []

    def __str__(self):
        album_display = ""

        if self.albums:
            for album in self.albums:
                album_display += ''.join(f'{album.title} (Runtime: {album.runtime} seconds)' + '\n')

        return f"Artist: {self.name}\n" \
               f"\nAlbums:\n{album_display}"

    def __repr__(self):
        return f"Object representation: {self.__class__.__name__}(artist_name={self.name!r})"

    def make_album(self, album_title):
        album = Album(album_title, self)
        self.albums.append(album)

        return album

class Album:
    def __init__(self, album_title, artist):
        self.title = album_title
        self.artist = artist
        self.tracks = []
        self.runtime = 0

    def add_track(self, track_name, track_number, length):
        track = Track(track_name, track_number, length)
        print(repr(track)) # for debugging
        self.tracks.append(track)
        self.runtime += track.length

    def __str__(self):
        track_display = ""

        if self.tracks:
            for track in self.tracks:
                track_display += ''.join(str(track) + '\n')

        return f"Album: {self.title}\n" \
               f"Runtime: {self.runtime} seconds\n" \
               f"Artist: {self.artist.name}\n" \
               f"\nTracks:\n{track_display}"

    def __repr__(self):
        return f"Object representation: {self.__class__.__name__}(album_title={self.title!r}, artist=Artist({self.artist.name!r}))"

class Track:
    def __init__(self, track_name, track_number, length):
        self.number = track_number
        self.name = track_name
        self.length = length

    def __str__(self):
        return f"Track Number: {self.number} " \
               f"Name: {self.name!r} " \
               f"Length: {self.length} seconds"

    def __repr__(self):
        return (f'Object representation: {self.__class__.__name__}'
                f'(track_name={self.name!r}, track_number={self.number}, length={self.length})')

################################# TEST CODE ###########################################

artist_1 = Artist("Prince")
# print(repr(artist_1))
# print(artist_1)
# print("-------------------------------------------------\n")

album_1 = artist_1.make_album("Purple Rain")
# print(artist_1)
# print("-------------------------------------------------\n")

album_1.add_track("Let's Go Crazy", 1, 280)
album_1.add_track("Purple Rain", 9, 521)
print("")
print(repr(album_1))
print(album_1)
print("-------------------------------------------------\n")

album_2 = artist_1.make_album("Diamonds and Pearls")

album_2.add_track("Diamonds and Pearls", 3, 285)
album_2.add_track("Cream", 4, 253)
print("")
print(repr(album_2))
print(album_2)
print("-------------------------------------------------\n")

print(repr(artist_1))
print(artist_1)

