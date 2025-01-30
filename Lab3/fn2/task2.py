import task1 as one

def high_score_list(movies):
    high_imdb_list = []
    for movie in movies:
        if one.imdb_high_score(movie):
            high_imdb_list.append(movie)

    return high_imdb_list

def print_movie_imdb_score(movies):
    for movie in movies:
        print(f"{movie['name']} | {movie['imdb']}")
