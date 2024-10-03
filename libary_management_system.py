
books = []
users = []

def add_book(book_id, title, author, genre):
    book = {
        'ID': book_id,
        'Title': title,
        'Author': author,
        'Genre': genre,
        'Status': 'Available'
    }
    books.append(book)

def add_user(user_id, name):
    user = {
        'ID': user_id,
        'Name': name,
        'Borrowed Books': []
    }
    users.append(user)

def view_books():
    print("\nAll Books:")
    for book in books:
        print(f"{book['ID']}. \"{book['Title']}\" by {book['Author']} ({book['Status']})")

def search_book(search_term):
    results = [book for book in books if search_term.lower() in book['Title'].lower() or 
               search_term.lower() in book['Author'].lower() or 
               search_term.lower() in book['Genre'].lower()]
    return results

def borrow_book(user_id, book_id):
    user = next((user for user in users if user['ID'] == user_id), None)
    book = next((book for book in books if book['ID'] == book_id), None)
    
    if user and book:
        if book['Status'] == 'Available':
            book['Status'] = 'Checked Out'
            user['Borrowed Books'].append(book_id)
            print(f"You have borrowed \"{book['Title']}\".")
        else:
            print(f"Sorry, the book \"{book['Title']}\" is currently checked out")
    else:
        print("Invalid user ID or book ID")

def return_book(user_id, book_id):
    user = next((user for user in users if user['ID'] == user_id), None)
    book = next((book for book in books if book['ID'] == book_id), None)
    
    if user and book and book_id in user['Borrowed Books']:
        book['Status'] = 'Available'
        user['Borrowed Books'].remove(book_id)
        print(f"You have returned \"{book['Title']}\".")
    else:
        print("Invalid user ID, book ID, or the book was not borrowed by you")

def view_available_books():
    print("\nAvailable Books=")
    for book in books:
        if book['Status'] == 'Available':
            print(f"{book['ID']}. \"{book['Title']}\" by {book['Author']}")

def view_checked_out_books():
    print("\nChecked Out Books=")
    for book in books:
        if book['Status'] == 'Checked Out':
            print(f"{book['ID']}. \"{book['Title']}\" by {book['Author']}")

def main_menu():
    while True:
        print("\nWelcome to the Community Library System!")
        print("----------------------------------------")
        print("Please choose an option:")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View available books")
        print("6. View checked out books")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7)= ")
        
        if choice == '1':
            view_books()
        elif choice == '2':
            search_term = input("Enter the title, author, or genre of the book= ")
            results = search_book(search_term)
            if results:
                print("\nSearch Results=")
                for book in results:
                    print(f"{book['ID']}. \"{book['Title']}\" by {book['Author']} ({book['Status']})")
            else:
                print("No books found")
        elif choice == '3':
            user_id = int(input("Enter your User ID= "))
            book_id = int(input("Enter the Book ID you want to borrow= "))
            borrow_book(user_id, book_id)
        elif choice == '4':
            user_id = int(input("Enter your User ID= "))
            book_id = int(input("Enter the Book ID you want to return= "))
            return_book(user_id, book_id)
        elif choice == '5':
            view_available_books()
        elif choice == '6':
            view_checked_out_books()
        elif choice == '7':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice! Please try again")
add_book(1, "To Kill a Mockingbird", "Harper Lee", "Fiction")
add_book(2, "1984", "George Orwell", "Dystopian")
add_book(3, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
add_user(1, "Alice")
add_user(2, "Bob")
main_menu()
