import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A Boy's toys come to life",
						"https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
						"https://www.youtube.com%2Fwatch%3Fv%3DKYz2wyBy3kc&usg=AFQjCNEJoSlxDJtzDTMi_7zEW-AOc2Z4MA&sig2=4icOpliOwvDtq-LfTwcnxg&bvm=bv.128617741,d.dGo")

# print(toy_story.storyline)

avatar = media.Movie("Avatar",
						"A marine on an alien planet",
						"https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
						"https://www.youtube.com%2Fwatch%3Fv%3DcRdxXPV9GNQ&usg=AFQjCNHfVhtBllyBLFd0YxZtVNRkrKF6gQ&sig2=qoZJE0keoQLDEWqidMfJ2g")

# print(avatar.poster_image_url)
# avatar.show_trailer()

suicide_sqad = media.Movie("Suicide Sqaud",
						"DC Universe superhero filem",
						"https://upload.wikimedia.org/wikipedia/en/thumb/5/50/Suicide_Squad_%28film%29_Poster.png/220px-Suicide_Squad_%28film%29_Poster.png",
						"https://www.youtube.com%2Fwatch%3Fv%3DCmRih_VtVAs&usg=AFQjCNHLRUXU5utAVVDy6048NDSED_K5ZQ&sig2=Z5nSOM2E_QIUZ75N6YyiLg")

ghostbusters = media.Movie("Ghostbusters 2016",
						"ghosts run wild in New York City",
						"https://upload.wikimedia.org/wikipedia/en/thumb/d/d0/Ghostbusters_2016_film_poster.jpg/220px-Ghostbusters_2016_film_poster.jpg",
						"https://www.youtube.com%2Fwatch%3Fv%3Dw3ugHP-yZXw&usg=AFQjCNFYJJsOX2JMFDHmgGwmYW2N6m30-w&sig2=_ZWxpHYPUH8u7yvoRM_5YQ&bvm=bv.128617741,d.dGo")

bfg = media.Movie("BFG",
						"A big friendly giant, by Roald Dahl",
						"https://upload.wikimedia.org/wikipedia/en/thumb/a/af/The_BFG_poster.jpg/220px-The_BFG_poster.jpg",
						"https://www.youtube.com%2Fwatch%3Fv%3DGZ0Bey4YUGI&usg=AFQjCNFhKabop0VtA8tQiyfmpw5WxkwNQg&sig2=77wA8xCpeX5kXCmMA70W9A&bvm=bv.128617741,d.dGo")

independence_day = media.Movie("Independence Day - Resurgence",
						"SciFi base on same film from 20 years ago, invasion",
						"https://upload.wikimedia.org/wikipedia/en/thumb/5/58/Independence-Day-2-poster.jpg/220px-Independence-Day-2-poster.jpg",
						"https://www.youtube.com%2Fwatch%3Fv%3DRfJgT89hEME&usg=AFQjCNGPQs4uSAgR6kcbSRaiEj93XL6DLw&sig2=P5llW5sYLmFOmXJ0DIQqgQ&bvm=bv.128617741,d.dGo")

movies = [toy_story,avatar,suicide_sqad,ghostbusters,bfg,independence_day]

# fresh_tomatoes.open_movies_page(movies)


#class variables
print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)
print (media.Movie.__name__)
print (media.Movie.__module__)