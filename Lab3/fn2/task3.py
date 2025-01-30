def get_movie_by_cotegory(movies, categories):
    return [movie for movie in movies if movie.get('category', '').lower() == categories.lower()]

def get_movie_names_by_cotegory(movies, categories):
    return [movie['name'] for movie in movies if movie.get('category', '').lower() == categories.lower()]
