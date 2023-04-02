class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = list()  # stores instances of class Movie
        self.movies_owned = list()  # stores instances of class Movie

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        output = [f"Username: {self.username}, Age: {self.age}", "Liked movies:"]
        liked_movies_details = [movie.details() for movie in self.movies_liked]
        if not liked_movies_details:
            output.append("No movies liked.")
        else:
            output.extend(liked_movies_details)
        output.append("Owned movies:")
        owned_movies_details = [movie.details() for movie in self.movies_owned]
        if not owned_movies_details:
            output.append("No movies owned.")
        else:
            output.extend(owned_movies_details)
        return "\n".join(output)
