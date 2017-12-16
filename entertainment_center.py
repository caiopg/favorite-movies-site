import fresh_tomatoes
from media import Movie

#Creation of favorite movie objects
matrix = Movie("Matrix",
               "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
               "https://www.youtube.com/watch?v=m8e-FF8MsqU")

matrix_reloaded = Movie("Matrix Reloaded",
               "https://upload.wikimedia.org/wikipedia/en/b/ba/Poster_-_The_Matrix_Reloaded.jpg",
               "https://www.youtube.com/watch?v=HVrGMnk5E_M")

matrix_revolutions = Movie("Matrix Revolutions",
               "https://upload.wikimedia.org/wikipedia/pt/9/94/Matrix_revolutions.jpg",
               "https://www.youtube.com/watch?v=NhoaoTZJSX4")

inception = Movie("Inception",
               "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
               "https://www.youtube.com/watch?v=8hP9D6kZseM")

shutter_island = Movie("Shutter Island",
               "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
               "https://www.youtube.com/watch?v=5iaYLCiq5RM")

shutter_island = Movie("Shutter Island",
               "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
               "https://www.youtube.com/watch?v=5iaYLCiq5RM")

interstellar = Movie("Interstellar",
               "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
               "https://www.youtube.com/watch?v=zSWdZVtXT7E")

#Putting all movie objects into list
movies = [matrix, matrix_reloaded, matrix_revolutions, inception, shutter_island, interstellar]

#Creation of html for website
fresh_tomatoes.open_movies_page(movies)