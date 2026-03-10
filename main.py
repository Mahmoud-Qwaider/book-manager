'''
Pseudo Code:

----- Setup -----
1. Create an empty list called "books"

----- Function: Add Book -----
2. Create a function called "add_book":
   - Print message "Adding New Book"
   - Ask user to enter book title, save it in a variable
   - Ask user to enter author name, save it in a variable
   - Create a dictionary with two keys: "title" and "author"
   - Add this dictionary to the books list
   - Print success message

----- Function: Display Books -----
3. Create a function called "display_books":
   - If the books list is empty:
     * Print "No books available"
     * Stop the function (return)
   - Otherwise:
     * For each book in the list:
       - Print book number + title + author

----- Function: Search Books -----
4. Create a function called "search_books":
   - Ask user to enter book title to search
   - Create an empty list for results
   - For each book in the books list:
     * If the entered text is found in the book title:
       - Add this book to the results list
   - If the results list is empty:
     * Print "No books found"
   - Otherwise:
     * Print all books found in the results list

----- Main Program -----
5. Create a function called "main":
   - Print welcome message
   - Start an infinite loop:
     * Print the menu:
       1. Add book
       2. Display books
       3. Search for book
       4. Exit
     * Ask user to choose a number
     * If choice is 1: call add_book function
     * If choice is 2: call display_books function
     * If choice is 3: call search_books function
     * If choice is 4: print "Goodbye" and stop the loop
     * If wrong number: print error message

----- Run Program -----
6. Call the main function
'''

# Create empty list to store all books
books = []


# Function to add a new book to the collection
def add_book():
    print("-----------------------------------------------------------")
    print(" ------------------- Add a New Book -------------------")
    print("-----------------------------------------------------------\n")

    book_title = input("Enter the book title: ")
    book_author = input("Enter the author name: ")

    # Create dictionary with book info and add to list
    book_dict = {
        "title": book_title,
        "author": book_author
    }
    books.append(book_dict)

    print("\n----------------------------------------------------------------------")
    print(" ------------------- Successfully Added New Book ------------------- ")
    print("----------------------------------------------------------------------\n")


# Function to display all books in the collection
def display_books():
    # Check if list is empty
    if len(books) == 0:
        print("No books available.")
        return

    # Print each book's details
    for index, book in enumerate(books,start=1):
            print(f"{index}. Title: {book['title']} | Author: {book['author']}\n")


# Function to search for books by title
def search_books():
    print(" ------------------- Search for a Book -------------------\n")
    search_title = input("Enter the book title to search: ")

    # Store matching books in this list
    found_books = []

    # Search through all books
    for book in books:
        if search_title.lower() in book['title'].lower():
            found_books.append(book)

    # Display search results
    if len(found_books) == 0:
        print("No books found.")
        return

    print("<--------- Search Results: --------->\n")
    for index, book in enumerate(found_books,start=1):
        print(f"{index}. Title: {book['title']} | Author: {book['author']}\n")


# Main program - displays menu and handles user choices
def main():
    print("\n-----------------------------------------------------------")
    print("  <--------------- Welcome to My Library --------------->  ")
    print("-----------------------------------------------------------\n")

    # Main loop - keeps program running until user quits
    while True:
        print("--- Main Menu ---")
        print("1. Add a book")
        print("2. Display books")
        print("3. Search for books")
        print("4. Quit")

        choice = input("\nEnter your choice (1-4): ")

        # Handle user's menu choice
        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            print("************** Thank you! Goodbye! ************** ")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4. ")


# Start the program
if __name__ == "__main__":
    main()