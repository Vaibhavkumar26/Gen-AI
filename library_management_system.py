import json


class Book:
    def __init__(self, title, book_id, author, total_copies):
        self.title = title
        self.book_id = str(book_id)
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies


class Library:
    def __init__(self):
        self.book_list = {}
        self.load_records()

    def add_books(self, book):
        if book.book_id in self.book_list:
            print("Book already exists")
        else:
            self.book_list[book.book_id] = book
            print("Book added successfully")

    def search_books(self, book_id):
        book = self.book_list.get(str(book_id))

        if book:
            print("Title:", book.title)
            print("Book ID:", book.book_id)
            print("Author:", book.author)
            print("Available copies:", book.available_copies)
        else:
            print("Book not found")

    def issue_books(self, book_id):
        book = self.book_list.get(str(book_id))

        if book:
            if book.available_copies > 0:
                book.available_copies -= 1
                print("Book issued successfully")
            else:
                print("Book is not available")
        else:
            print("Book not found")

    def return_books(self, book_id):
        book = self.book_list.get(str(book_id))

        if book:
            if book.available_copies < book.total_copies:
                book.available_copies += 1
                print("Book returned successfully")
            else:
                print("All copies are already in the library")
        else:
            print("Book not found")

    def display_available_books(self):
        found = False

        for book in self.book_list.values():
            if book.available_copies > 0:
                print(
                    book.title,
                    book.book_id,
                    book.author,
                    book.available_copies
                )
                found = True

        if not found:
            print("No books available")

    def save_records(self):
        records = []

        for book in self.book_list.values():
            records.append({
                "title": book.title,
                "book_id": book.book_id,
                "author": book.author,
                "total_copies": book.total_copies,
                "available_copies": book.available_copies
            })

        with open("book_records.json", "w") as file:
            json.dump(records, file, indent=4)

        print("Records saved successfully")

    def load_records(self):
        try:
            with open("book_records.json", "r") as file:
                records = json.load(file)

            for record in records:
                book = Book(
                    record["title"],
                    record["book_id"],
                    record["author"],
                    record["total_copies"]
                )

                book.available_copies = record["available_copies"]
                self.book_list[book.book_id] = book

        except FileNotFoundError:
            pass


def main():
    library = Library()

    while True:
        print("\n----- LIBRARY MANAGEMENT SYSTEM -----")
        print("1. Add books")
        print("2. Search books")
        print("3. Issue books")
        print("4. Return books")
        print("5. Display available books")
        print("6. Save records")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            book_id = input("Enter book ID: ")
            author = input("Enter author name: ")

            try:
                total_copies = int(input("Enter number of copies: "))

                if total_copies <= 0:
                    print("Number of copies must be positive")
                    continue

                book = Book(title, book_id, author, total_copies)
                library.add_books(book)

            except ValueError:
                print("Enter a valid number")

        elif choice == "2":
            book_id = input("Enter book ID: ")
            library.search_books(book_id)

        elif choice == "3":
            book_id = input("Enter book ID to issue: ")
            library.issue_books(book_id)

        elif choice == "4":
            book_id = input("Enter book ID to return: ")
            library.return_books(book_id)

        elif choice == "5":
            library.display_available_books()

        elif choice == "6":
            library.save_records()

        elif choice == "0":
            print("Exiting library system")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()