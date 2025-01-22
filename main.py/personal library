#Aiden Challenger Personal Library 

#Stores all items in a list
#Function to add a new item
#Function to search the items
#Function to remove an item
#Function that runs the code (displays the menu options inside and calls the functions inside of a while True loop)
#Project must include
#easy to understand variable and function names
#Pseudocode comments explaining what the code is doing
#Good use of white space to keep items separate and easy to read/find
#Have at least 2 people test your code before submission!

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
    author = input("What is the author's name: ")
    year = input("What year was it published: ")
    
# Combine all info
    book = [title, author, year]
    
    # Add to main list and set
    library_books.append(book)
    book_names.add(title.lower())

# Book removal function (inverse of adding)
def remove_book():
# Input on what to remove
    title_r = input("What is the title you want to remove?: ")
    
# Check if the book exists
    if title_r.lower() not in book_names:
        print("This book doesn't exist.\n")
        return

# Remove book from list
    for book in library_books:
        if book[0].lower() == title_r.lower():
            library_books.remove(book)
            book_names.remove(title_r.lower())
            break


# Search function
def search_book():
    search = input("Enter book title or author to search: ").strip().lower()
    found_books = [book for book in library_books if search in book[0].lower() or search in book[1].lower()]
#print what's found 
    if found_books:
        print("Search Results:")
        for book in found_books:
            print(f"{book[0]} by {book[1]} ({book[2]})")
    else:
        print("No books found matching the search query.")
    print()

# Display function
def display():
#check for real books 
    if not library_books:
        print("Nothing exists yet.\n")
        return
#print books
    print("Library Books:")
    count = 1  
    for book in library_books:
        print(f"{count}. {book[0]} by {book[1]} ({book[2]})")
        count += 1  
    print()

# Have user select what they want to use
def main():
    while True:
        print("Personal Library Program")
        print("1- Add an item")
        print("2- Remove an item")
        print("3- Search for an item")
        print("4- Display current library")
        print("5- Exit")
        choice = input("What would you like to do?: ")
        
        if choice == '1':
            add_book()
                  
        elif choice == '2':
            remove_book()
        
        elif choice == '3':
            search_book()
        
        elif choice == '4':
            display()
        
        elif choice == '5':
            break

if __name__ == "__main__":
    main()
