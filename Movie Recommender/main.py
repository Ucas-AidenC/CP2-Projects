#Aiden Challenger Movie Recommender 
#maybe do this later but i'm lowkey lazy
#Dead Poets Society,Peter Weir,Drama,PG,128,"Robin Williams, Ethan Hawke"
import csv
filters = {}

movies = []

#reading file info
with open ('Movie Recommender/Movies list.csv','r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        movies.append(row)

def filter_movies(movies, filters):
    filtered_movies = movies
    for key, value in filters.items():
        if key == 'Length (min)':
            #sep time filter t 
            filtered_movies = time_filter(filtered_movies, int(value))
        else:
            filtered_movies = [movie for movie in filtered_movies if value.lower() in movie[key].lower()]
    return filtered_movies

def print_movies(movies):
#check for if movies exist 
    if not movies:
        print("no movies found")
        return
#print full movie lis t 
    for movie in movies:
        print(f"Title: {movie['Title']}")
        print(f"Director: {movie['Director']}")
        print(f"Genre: {movie['Genre']}")
        print(f"Rating: {movie['Rating']}")
        print(f"Length: {movie['Length (min)']} min")
        print(f"Notable Actors: {movie['Notable Actors']}\n\n")


def parameters():
 #take parameters from the user for first value 
    print("\n filters: genre, director, length, actors")
    filter1 = input("enter your first filter (genre, director, length, actors): ").strip().lower()
    value1 = input(f"\nwhat do you want to filter for in {filter1}: ").strip().lower()
    filters[filter1] = value1
#second value 
    filter2 = input("enter your second filter (genre, director, length, actors): ").strip().lower()
    value2 = input(f"\nwhat do you want to filter for in {filter2}: ").strip().lower()
    filters[filter2] = value2
    return filters
#filterign for times 
def time_filter(movies, user_time):
    min_time = user_time - 15
    max_time = user_time + 15
    return [movie for movie in movies if min_time <= int(movie['Length (min)']) <= max_time]

#main / choice 
def main():
    while True:
        print("Movie Recommender")
        print("1.print movies(with current parameters)")
        print("2.change filter parameters")
        print("3.print all movies")
        print("4.exit")
        choice = int(input("What would you like to use(1-4)"))
        if choice == 1:
                    if filters:
                        filtered_movies = filter_movies(movies, filters)
                        if filtered_movies:
                            print("recommendations:\n")
                            print_movies(filtered_movies)
                        else:
                            print("\nNo movies found matching your criteria.")
                    else:
                        print("\nNo filter parameters set. Please set filter parameters first.")
        elif choice == 2:
                    filters= parameters()
        elif choice == 3:
                    print("\nFull Movie List:")
                    print_movies(movies)
        elif choice ==4:
                    break
if __name__ == "__main__":
    main()
