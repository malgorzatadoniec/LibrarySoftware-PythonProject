#klasa i funkcje
class Library:
    def __init__(self, bookslist, name, borrowedbooks):
        self.booksList = bookslist
        self.name = name
        self.borrowedBooks = borrowedbooks
        self.lendDict = {}


    def displayBooks(self):
        print(f'We have following books in our library {self.name}:' )
        bookDatabase = open(databaseName, 'r')
        print(bookDatabase.read())

    def addBook(self, book):
        with open(databaseName) as bookDatabase:
            self.booksList = [book.strip() for book in bookDatabase]

        if book in self.booksList:
            print('Book already exists')
        else:
            self.booksList.append(book)
            bookDatabase = open(databaseName, 'a')
            bookDatabase.write('\n')
            bookDatabase.write(book)
            print('Book added')

    def lendBook(self, book, user):
        with open(databaseName) as bookDatabase:
            self.booksList = [book.strip() for book in bookDatabase]

        if book in self.booksList:
            with open(BBdatabaseName) as BBDatabase:
                self.borrowedBooks = [book.strip() for book in BBDatabase]

            if book not in self.borrowedBooks:
                self.borrowedBooks.append(book)
                BBDatabase = open(BBdatabaseName, 'a')
                BBDatabase.write('\n')
                BBDatabase.write(book)
                if book not in self.lendDict.keys():
                    self.lendDict.update({book:user})
                print('Book has been lended. Database updated')

            else:
                print(f'Book is already beeing used by {self.lendDict[book]}')
        else:
            print("Apologies! We don't have this book in our library")

    def returnBook(self, book):
        with open(BBdatabaseName) as BBDatabase:
            self.borrowedBooks = [book.strip() for book in BBDatabase]

        if book in self.borrowedBooks:
            with open(BBdatabaseName, 'r') as BBD:
                lines = BBD.readlines()
            with open(BBdatabaseName, 'w') as BBD:
                for line in lines:
                    if line.strip("\n") != book:
                        BBD.write(line)
            self.lendDict.pop(book)
            print('Book returned successfully')
        else:
            print('The book does not exist in the Book Lending Database')

    def displayBorrowedBooks (self):
        if int(len(self.lendDict)) ==0:
            print('No books lended')
        else:
            print('Following books are borrowed:')
            for items in self.lendDict.items():
                print(items)



# Menu użytkownika
def main():
    while(True):
        print(f'Welcome to the {library.name} library. Following are the options:')
        choice = '''
        1. Display Books
        2. Lend a Book
        3. Return a Book
        4. Add a Book
        5. Display Borrowed Books
        '''
        print(choice)

        userinput = input('Press Q to quit and C to continue:')
        if userinput == 'C':
            userChoice = int(input('Select an option to continue:'))
            if userChoice == 1:
                library.displayBooks()
            elif userChoice == 2:
                book = input('Enter the name of the book you want to lend:')
                user = input('Enter the name of the user:')
                library.lendBook(book, user)
            elif userChoice == 3:
                book = input('Enter the name of the book you want to return:')
                library.returnBook(book)
            elif userChoice == 4:
                book = input('Enter the name of the book you want to add:')
                library.addBook(book)
            elif userChoice == 5:
                library.displayBorrowedBooks()
            else:
                print('Please choose a valid option')
        elif userinput == 'Q':
            break
        else:
            print('Please choose a valid option')


# kod dopasowujący bazy danych (pliki) do danej biblioteki
if __name__ == '__main__':
    booksList = []
    databaseName = input('Enter the name of the all books database file with extention:')

    borrowedBooks = []
    BBdatabaseName = input('Enter the name of the borrowed books database file with extention:')


# obiekty
    library = Library(booksList, 'Filia 1', borrowedBooks)
    main()