from movie import movies

def movies_by_category(movies, category):
    return [movie for movie in movies if movie['category'] == category]

# Example usage
if __name__ == "__main__":
    category = "Romance"
    print(f"movies_by_category('{category}'): {movies_by_category(movies, category)}")
