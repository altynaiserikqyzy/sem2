from movie import movies

def average_imdb_score(movies):
    return sum(movie['imdb'] for movie in movies) / len(movies)

# Example usage
if __name__ == "__main__":
    print(f"average_imdb_score: {average_imdb_score(movies)}")
