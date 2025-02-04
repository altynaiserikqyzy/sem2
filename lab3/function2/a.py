from movie import movies

def is_high_score(movie):
    return movie['imdb'] > 5.5

# Example usage
if __name__ == "__main__":
    movie = movies[0]
    print(f"is_high_score({movie['name']}): {is_high_score(movie)}")
