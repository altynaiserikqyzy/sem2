from movie import movies

def high_score_movies(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]

# Example usage
if __name__ == "__main__":
    print(f"high_score_movies: {high_score_movies(movies)}")
