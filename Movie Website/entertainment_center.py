import fresh_tomatoes
import media

train_your_dragon = media.Movie("How to train your dragon",
                       "A hapless young Viking who aspires to hunt dragons becomes the unlikely friend of a young dragon himself, and learns there may be more to the creatures than he assumed.",
                       "Dean DeBlois, Chris Sanders",
                       "http://ia.media-imdb.com/images/M/MV5BMjA5NDQyMjc2NF5BMl5BanBnXkFtZTcwMjg5ODcyMw@@._V1_SY1000_CR0,0,672,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=VEcM3rbnwQ4")
big_hero = media.Movie("Big Hero 6",
                     "The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada, who team up with a group of friends to form a band of high-tech heroes.",
                     "Don Hall, Chris Williams",
                    "http://ia.media-imdb.com/images/M/MV5BMDliOTIzNmUtOTllOC00NDU3LWFiNjYtMGM0NDc1YTMxNjYxXkEyXkFqcGdeQXVyNTM3NzExMDQ@._V1_SY1000_CR0,0,699,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=z3biFxZIJOQ")
frozen = media.Movie("Frozen","When the newly crowned Queen Elsa accidentally uses her power to turn things into ice to curse her                         home in infinite winter, her sister, Anna, teams                              up with a mountain man, his                           playful reindeer, and a snowman to change the weather condition.",
                          "Chris Buck, Jennifer Lee",
                          "http://ia.media-imdb.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=-WdC4DaYIeQ")
findingnemo = media.Movie("Finding Nemo",
                        "After his son is captured in the Great Barrier Reef and taken to Sydney, a timid clownfish sets out on a journey to bring him home.",
                        "Andrew Stanton, Lee Unkrich",
                        "http://ia.media-imdb.com/images/M/MV5BOTdhMTQzNTMtNTkwZC00ZTAwLTgwMmEtNGJhOGViYWNhMTc4XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_SY1000_CR0,0,702,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=2zLkasScy7A")
batman_killingjoke = media.Movie("Batman: The Killing Joke",
                           "As Batman hunts for the escaped Joker, the Clown Prince of Crime attacks the Gordon family to prove a diabolical point mirroring his own fall into madness.",
                            "Sam Liu",
                           "http://ia.media-imdb.com/images/M/MV5BODcxYTc5NmQtZTZjNS00MjRiLTgxMjQtN2VhYjY2YjdmMzYzXkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_SY1000_CR0,0,849,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=VeNi4PfNMqI")
justice = media.Movie("Justice League",
                      "The world's finest heroes found the Justice League in order to stop an alien invasion of Earth.",
                      "Jay Oliva",
                      "http://ia.media-imdb.com/images/M/MV5BMTQ1ODc1MTMwNl5BMl5BanBnXkFtZTgwNDgyMjU5MDE@._V1_.jpg",
                      "https://www.youtube.com/watch?v=q3F9ASSsHUk")

movies = [train_your_dragon, big_hero, frozen, findingnemo, batman_killingjoke, justice]
fresh_tomatoes.open_movies_page(movies)
