import task1 as one
import task2 as two
import task3 as three
import task4 as four
import task5 as five

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

a = """
==================
      TASK 1
==================
"""

print(a)

for movie in movies:
    result = one.imdb_high_score(movie)
    print(f"{movie['name']} : {result}")

b = """
===================
      TASK 2
===================
"""

print('\n' + b + '\n')

two.print_movie_imdb_score(two.high_score_list(movies))

c = """
===================
      TASK 3
===================
"""

print ('\n' + c + '\n')

category1 = "Thriller"
category2 = "Romance"

category1_movies = three.get_movie_by_cotegory(movies, category1)
category2_movies = three.get_movie_by_cotegory(movies, category2)

print(f"Movies in the '{category1}' : ")
for movie in category1_movies:
    print(f"--{movie['name']} (IMDb : {movie['imdb']})")

print(f"\nMovies in the '{category2}' : ")
for movie in category2_movies:
    print(f"--{movie['name']} (IMDb : {movie['imdb']})")

cat1_names = three.get_movie_names_by_cotegory(movies, category1)
cat2_names = three.get_movie_names_by_cotegory(movies, category2)

print(f"\nNames of movie in the '{category1}' : ")
for movie in cat1_names:
    print(f"-- {movie}")

print(f"\nNames of movie in the '{category2}' : ")
for movie in cat2_names:
    print(f"--{movie}")

d = """
===================
      TASK 4
===================
"""

print('\n' + d + '\n')

print(f" AVG IMDB : {four.avg_imdb(movies)}")

e = """
===================
      TASK 5
===================
"""

print('\n' + e + '\n')

category = 'Romance'
average  = five.AVG_CATEGORY(movies, category)
print(f"AVG of '{category}' : {average}")

f = """\n
==============================
EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
==============================\n
"""

print(f)
