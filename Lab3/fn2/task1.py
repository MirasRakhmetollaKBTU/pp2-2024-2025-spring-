def imdb_high_score(movie):
    imdb_score = movie.get('imdb', 0)
    return imdb_score > 5.5
