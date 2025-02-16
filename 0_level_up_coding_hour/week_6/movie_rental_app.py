'''
You are creating a movie rental application. Implement a Movie class with the following specifications:

Instance attributes:
- name (string): The title of the movie
- year_made (integer): The year the movie was released
- length (integer): The movie's duration in minutes
- rating (float): A number between 1.0 and 5.0, with 5.0 being the best
- genre (string): The movie's genre (e.g., Action, Comedy, Drama)
- available (boolean): Indicates if the movie is currently available for rent
- times_rented (integer): Tracks how many times the movie has been rented

Instance methods:
- rent_movie(): Marks the movie as rented and increments times_rented
- return_movie(): Marks the movie as available for rent
- get_movie_info(): Returns a formatted string with all movie details
- update_rating(new_rating): Allows updating the movie's rating
- is_popular(): Returns True if the movie has been rented more than 5 times

Test your class works as expected by created 2 or more objects and testing all the instance methods.
Feel free to create additional methods such as set_rating, to play with the objects created.
'''

import random

class Movie:
    # class variables and methods

    # instance variables and methods
    def __init__(self, title=None, year_made=2025, length=0, genre=None):
        self.title = title
        self.year_made = year_made
        self.length = length
        self.genre = genre
        self.rating = None
        self.times_rented = 0
        self.available = True

    def __str__(self):
        return f"MOVIE INFO\n" \
               f"Title: {self.title}\n" \
               f"Year Made: {self.year_made}\n" \
               f"Length: {self.length}\n" \
               f"Genre: {self.genre}\n" \
               f"Rating: {self.rating}\n" \
               f"Times Rented: {self.times_rented}\n" \
               f"Available: {self.available}"

    def rent_movie(self):
        if self.available:
            self.times_rented += 1
            self.available = False
        else:
            print(f"{self.title} is currently unavailable to rent.")

    def return_movie(self):
        self.available = True

    def update_rating(self, rating):
        if self.rating is None:
            self.rating = rating
        else:
            self.rating = float(f"{(self.rating + rating) / 2:.{2}f}")

    def is_popular(self):
        return self.times_rented > 5


#################################  TEST MOVIE APPLICATION  ##################################
movie_1 = Movie("The Big Labowski", 1998, 117, "Comedy")
print(movie_1)
print("")
movie_1.rent_movie()
print(movie_1)
print("")
movie_1.rent_movie()

print('------------------------------------------------------------------')

movie_2 = Movie("Star Wars", 1977, 121, "Science Fiction")
print(movie_2)

for i in range(10):
    movie_2.rent_movie()
    movie_2.return_movie()
    movie_2.update_rating(random.uniform(3, 5))

print("")
print(movie_2)

print('------------------------------------------------------------------')

print(f"{movie_1.title} has been rented {movie_1.times_rented} time(s). Is it popular?: {movie_1.is_popular()}")
print(f"{movie_2.title} has been rented {movie_2.times_rented} time(s). Is it popular?: {movie_2.is_popular()}")