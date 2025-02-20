#Aiden Challenger Movie Recommender 
#maybe do this later but i'm lowkey lazy
#Dead Poets Society,Peter Weir,Drama,PG,128,"Robin Williams, Ethan Hawke"

import csv

movies = []

# read file info
with open('Movie Recommender/Movies list.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        movies.append(row)

#function to make filter work 
def filter_movies(movies, filters):
    filtered_movies = movies
    translation = {
        "genre": "Genre",
        "director": "Director",
        "length": "Length (min)",
        "actors": "Notable Actors"
    }

    for key, value in filters.items():
        column_name = translation.get(key, key) 

        if column_name == 'Length (min)':
            try:
                filtered_movies = time_filter(filtered_movies, int(value))
            except ValueError:
                print(f"Invalid length filter: {value}")
        else:
            filtered_movies = [
                movie for movie in filtered_movies
                if value.lower() in movie.get(column_name, '').lower()
            ]

    return filtered_movies

#printing movies for param 
def print_movies(movies):
#check for if movies exist 
    if not movies:
        print("No movies found")
        return
#actual printing 
    for movie in movies:
        print(f"Title: {movie.get('Title', 'N/A')}")
        print(f"Director: {movie.get('Director', 'N/A')}")
        print(f"Genre: {movie.get('Genre', 'N/A')}")
        print(f"Rating: {movie.get('Rating', 'N/A')}")
        print(f"Length: {movie.get('Length (min)', 'N/A')} min")
        print(f"Notable Actors: {movie.get('Notable Actors', 'N/A')}\n")

def parameters(filters):
#take input from user 
    print("\nFilters: genre, director, length, actors")
    
    filter1 = input("Enter your first filter (genre, director, length, actors): ").strip().lower()
    value1 = input(f"\nwhat do you want to filter for in {filter1}: ").strip().lower()
    filters[filter1] = value1

    filter2 = input("Enter your second filter (genre, director, length, actors): ").strip().lower()
    value2 = input(f"\nwhat do you want to filter for in {filter2}: ").strip().lower()
    filters[filter2] = value2
#bring back filter variable 
    return filters  

#sep function for time
def time_filter(movies, user_time):
    min_time = user_time - 30
    max_time = user_time + 30
    return [movie for movie in movies if min_time <= int(movie.get('Length (min)', 0)) <= max_time]

#main selector 
def main():
    filters = {}
    while True:
        print("\nMovie Recommender")
        print("1. print movies (with current parameters)")
        print("2. change filter parameters")
        print("3. print all movies")
        print("4. exit")
        choice = int(input("what would you like to do (1-4)? "))
        if choice == 1:
            if filters:
                filtered_movies = filter_movies(movies, filters)
                if filtered_movies:
                    print("\nRecommendations:\n")
                    print_movies(filtered_movies)
                else:
                    print("\nNo movies found matching your criteria.")
            else:
                print("\nNo filter parameters set. Please set filter parameters first.")
        elif choice == 2:
            filters = parameters(filters) 
        elif choice == 3:
            print("\nFull Movie List:")
            print_movies(movies)
        elif choice == 4:
            break

if __name__ == "__main__":
    main()
