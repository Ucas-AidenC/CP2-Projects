#Aiden Challenger Personal Library 

#Each item in the dictionary should have AT LEAST 4 different details about it
#You should be able to update the different items in your dictionary
#There should be the option to print a simple list (Names and authors/artists/director) OR print a detailed list (Contains all the information)

# List for books (editable)
library_books = []

# Set for title checks
book_names = set()


# Book adding function
def add_book():
    title = input("What is the title of the book you want to add? ")
# Compare to see if it already exists
    if title.lower() in book_names:
        print("This book is in the list already.")
        return
    
# Final inputs from user
    author = input("What is the author's name: ").strip()
    year = input("What year was it published: ").strip()
    genre=input("what is the genre of the book: ").strip()
    
    # storing dictionary info 
    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre
    }
     # Add to main list and set
    library_books.append(book)
    book_names.add(title.lower())

# Book removal function (inverse of adding)
def remove_book():
    # title for removeal
    title_r = input("What is the title you want to remove?: ").strip()
    # Check if the book exists
    if title_r.lower() not in book_names:
        print("This book doesn't exist.\n")
        return

    # Find and remove the book
    for book in library_books:
        if book['title'].lower() == title_r.lower():
            library_books.remove(book)
            book_names.remove(title_r.lower())
            print(f"Removed '{book['title']}' from the library.\n")
            return  # Stop loop after removing the book

    print("Book not found.\n")

#upd function 
def update_book():
    title_u = input("What is the title of the book you want to update?: ")
    
    # Check if the book exists
    if title_u.lower() not in book_names:
        print("This book doesn't exist.\n")
        return

    # display current details 
    for book in library_books:
        if book['title'].lower() == title_u.lower():
            print("Current details:")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year: {book['year']}")
            print(f"Genre: {book['genre']}")
#new info taking 
            book['title'] = input("Enter new title (press enter to skip): ") or book['title']
            book['author'] = input("Enter new author (press enter to skip): ") or book['author']
            book['year'] = input("Enter new year (press enter to skip): ") or book['year']
            book['genre'] = input("Enter new genre (press enter to skip): ") or book['genre']
            return




# Search function
def search_book():
    search = input("Enter book title or author to search: ").strip().lower()
    found_books = [book for book in library_books if search in book['title'].lower() or search in book['author'].lower()]
    # Print what's found
    if found_books:
        print("Found books:")
        for book in found_books:
            print(f"{book['title']} by {book['author']}")
    else:
        print("No books found")
    print()

# Display function simple display
def display_simple():
    #check for real books 
    if not library_books:
        print("Nothing exists yet.\n")
        return
    
    #list printing 
    print("Library Books (simple):")
    for book in library_books:
        print(f"{book['title']} by {book['author']}")
    print()

#display complex 
def display_complex():
     #check for real books 
    if not library_books:
        print("Nothing exists yet\n")
        return
    
    #list printing 
    print("Library Books (detailed):")
    for book in library_books:
        print(f"{book['title']} by {book['author']} published in {book['year']} genre: {book['genre']}")
    print()

# main/selection 
def main():
    while True:
        print("Personal Library Program")
        print("1- Add an item")
        print("2- Remove an item")
        print("3- Search for an item")
        print("4- Update item")
        print("5- Display current library(simple)")
        print("6- Display current library(detailed)")
        print("7- Exit")
        choice = input("What would you like to do?: ")
        
        if choice == '1':
            add_book()
                  
        elif choice == '2':
            remove_book()
        
        elif choice == '3':
            search_book()
        
        elif choice == '4':
            update_book()
        
        elif choice == '5':
            display_simple()
        elif choice == '6':
            display_complex()
                  
        elif choice == '7':
            break


if __name__ == "__main__":
    main()
