def AVG_CATEGORY(movies, category):
    filterg = [movie for movie in movies if movie.get('category', '').lower() == category.lower()]
    score   = [movie.get('imdb', 0) for movie in filterg if isinstance(movie.get('imdb', 0), (int, float))]
    return sum(score) / len(score)
