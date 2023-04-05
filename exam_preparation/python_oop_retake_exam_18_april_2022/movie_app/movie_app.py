from exam_preparation.python_oop_retake_exam_18_april_2022.movie_app.movie_specification.movie import Movie
from exam_preparation.python_oop_retake_exam_18_april_2022.movie_app.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = list()  # stores instances of class Movie
        self.users_collection = list()  # stores instances of class User

    def username_validation(self, value):
        for user in self.users_collection:
            if user.username == value:
                return user

    def register_user(self, username: str, age: int):
        if self.username_validation(username):
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.username_validation(username)
        if not user:
            raise Exception('This user does not exist!')

        if movie in self.movies_collection:
            raise Exception('Movie already added to the collection!')

        if movie.owner.username != username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie not in self.username_validation(username).movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            setattr(movie, key, value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = self.username_validation(username)
        if movie not in user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.username_validation(username)
        if movie in user.movies_owned:
            raise Exception(f'{username} is the owner of the movie {movie.title}!')

        if movie in user.movies_liked:
            raise Exception(f'{username} already liked the movie {movie.title}!')

        movie.likes += 1
        user.movies_liked.append(movie)
        return f'{username} liked {movie.title} movie.'

    def dislike_movie(self, username: str, movie: Movie):
        user = self.username_validation(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        movies_to_display = sorted(self.movies_collection, key=lambda m: (-m.year, m.title))

        return "\n".join(movie.details() for movie in movies_to_display)

    def __str__(self):
        return f"All users: " \
               f"{', '.join(u.username for u in self.users_collection) if self.users_collection else 'No users.'}\n" \
               f"All movies:" \
               f" {', '.join(m.title for m in self.movies_collection) if self.movies_collection else 'No movies.'}"
