def avg_imdb(movies):
    score = [movie.get('imdb') for movie in movies if isinstance(movie.get('imdb'), (int, float))]
    return sum(score) / len(score)
