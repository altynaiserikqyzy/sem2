from movie import movies

def average_imdb_by_category(movies, category):
    category_movies = [movie for movie in movies if movie['category'] == category]
    
    if not category_movies:  # Если фильмов в категории нет, вернуть 0
        return 0

    return sum(movie['imdb'] for movie in category_movies) / len(category_movies)

# Example usage
if __name__ == "__main__":
    category = "Romance"
    print(f"average_imdb_by_category('{category}'): {average_imdb_by_category(movies, category)}")