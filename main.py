import fresh_tomatoes   #Build a HTML page, use function "open_movies_page"
import define_class     #Create a class named "Movie"

inception = define_class.Movie("Inception",
                               "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                               "https://www.youtube.com/watch?v=E1iqGiX0lSg")
interstellar = define_class.Movie("Interstellar",
                                  "https://upload.wikimedia.org/wikipedia/zh/b/bc/Interstellar_film_poster.jpg",
                                  "https://www.youtube.com/watch?v=Df7IEKqimOY")
the_expendables = define_class.Movie("The Expendables",
                                     "https://upload.wikimedia.org/wikipedia/en/7/76/Expendablesposter.jpg",
                                     "https://www.youtube.com/watch?v=KoULwHrm1vg")

movie_list = [inception, interstellar, the_expendables]     #Use a list to save instances of class 'Movie'
fresh_tomatoes.open_movies_page(movie_list)                 #Open a page, need a list of movies