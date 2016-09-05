# Movie Trailer Website
Website containing list of favorite movies that allows the user to watch youtube trailer of movie on clicking the poster image of movie.

## Table Of Content
* Description
* Requirements
* Usage
* Details

### Description
Movie Trailer Website is my first project from **Full Stack Web Developer Nanodegree program**. It focuses on writing server-side code written in Python to store a list of your favorite movies, including box art imagery and a movie trailer URL. It generates a static web page allowing visitors to browse their movies and watch the trailers onclick.

### Requirements
* python >= 2.7
* web browser: any of Safari/Chrome/Firefox/explorer

### Usage
* Run **entertainment_center.py**
* To update the movie list or to creat new instances. Update **entertainment_center.py**
* Edit the **favorite_movies.py** to modify the styling features of front-end page.

### Details
* entertainment_center.py module creates the list of movie objects.
* It passes this list to open_movies_page() function.
* open_movies_page() generates a static web page with the movie title, poster images and youtube URL for each movie in the list.
* Movie class defined in media.py module and contains only one constructor which creates and initialize movie object with a title, poster image URL, trailer youtube URL and along with other movie details.
* User can click on movie poster image to see it's youtube trailer.
