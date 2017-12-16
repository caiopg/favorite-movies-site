import fresh_tomatoes
from media import Movie

'''This python file creates a html with my favorite movies.'''

# Start creation of favorite movie objects

# Creation of Matrix Movie object: title, poster url, trailer url
matrix = Movie("Matrix",
               "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # NOQA
               "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# Creation of Matrix Reloaded Movie object: title, poster url, trailer url
matrix_reloaded = Movie("Matrix Reloaded",
               "https://upload.wikimedia.org/wikipedia/en/b/ba/Poster_-_The_Matrix_Reloaded.jpg",  # NOQA
               "https://www.youtube.com/watch?v=HVrGMnk5E_M")

# Creation of Matrix Revolutions Movie object: title, poster url, trailer url
matrix_revolutions = Movie("Matrix Revolutions",
               "https://upload.wikimedia.org/wikipedia/pt/9/94/Matrix_revolutions.jpg",  # NOQA
               "https://www.youtube.com/watch?v=NhoaoTZJSX4")

# Creation of Inception Movie object: title, poster url, trailer url
inception = Movie("Inception",
               "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",  # NOQA
               "https://www.youtube.com/watch?v=8hP9D6kZseM")

# Creation of Shutter Island Movie object: title, poster url, trailer url
shutter_island = Movie("Shutter Island",
               "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",  # NOQA
               "https://www.youtube.com/watch?v=5iaYLCiq5RM")

# Creation of Interstellar Movie object: title, poster url, trailer url
interstellar = Movie("Interstellar",
               "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",  # NOQA
               "https://www.youtube.com/watch?v=zSWdZVtXT7E")

# End of creation of favorite movie objects

# Putting all movie objects into list
movies = [
    matrix,
    matrix_reloaded,
    matrix_revolutions,
    inception,
    shutter_island,
    interstellar
]

# Creation of html for website
fresh_tomatoes.open_movies_page(movies)
