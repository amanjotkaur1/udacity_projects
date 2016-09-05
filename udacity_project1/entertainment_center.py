import favorite_movies
import media 

# creating instance for first movie
toy_story=media.Movie("Toy Story", "Story of a young boy who love toys",
                "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# creating instance for second movie
avatar=media.Movie("Avatar",
                "Story of a Marine veteran, that volunteers to go as avatar driver.",
                "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                "https://www.youtube.com/watch?v=d1_JBMrrYw8")

# creating instance for third movie
three_idiots=media.Movie("3 Idiots",
                "A man makes contribution to engineering field.",
                "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                "https://www.youtube.com/watch?v=K0eDlFX9GMc")

# creating instance for fourth movie
Twilight=media.Movie("Twilight",
                "love story of vampire and human",
                "http://vignette3.wikia.nocookie.net/twilightsaga/images/1/14/"
                "Twilight_Poster.jpeg/revision/latest?cb=20160531135758",
                "https://www.youtube.com/watch?v=edLB6YWZ-R4")

# creating instance for fifth movie
life_of_pi=media.Movie("Life of Pi",
                "Story of a boy who survives in lifeboat with a tiger",
                "https://upload.wikimedia.org/wikipedia/en/5/57/Life_of_Pi_2012_Poster.jpg",
                "https://www.youtube.com/watch?v=mZEZ35Fhvuc")

# creating instance for sixth movie
Ice_Age=media.Movie("Ice Age",
                "Movie of the time back when the Earth was being overrun by glaciers",
                "https://upload.wikimedia.org/wikipedia/en/a/a9/Ice_Age.jpg",
                "https://www.youtube.com/watch?v=cMfeWyVBidk")

# creating movies list
movies = [toy_story, avatar, three_idiots, Twilight, life_of_pi, Ice_Age]

# passing movies list to open_movies_page function
favorite_movies.open_movies_page(movies)

