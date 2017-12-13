import create_website
#from media import Movie
import media

avatar = media.Movie("Avatar","A marine on an alien planet",
	"http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")

toy_story = media.Movie("Toy Story","A story of a boy and his toy that come in life",
	"http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

doctor_strange = media.Movie("Doctor Strange","Doctor Strange est un film americain de super-heros raalisa par Scott Derrickson,\
sorti en 2016. Adapté du personnage du Docteur Strange créé par Steve Ditko,\
c\'est le 14ᵉ film de l'univers cinématographique Marvel et le 2ᵉ de la phase III.",
	"http://cdn2-www.comingsoon.net/assets/uploads/gallery/doctor-strange-1403135280/doctor-strange-empire-subscribers-cover.jpg",
	"https://www.youtube.com/watch?v=HSzx-zryEgM")



Movie = [doctor_strange,American_pie7,avatar,toy_story]
create_website.open_movies_page(Movie)
print()