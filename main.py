import auth
import create
import practice
import view
import upload
import delete
import sqlite3

# Although it would have been a good idea to have a single database, I decided to have multiple databases so that if one gets corrupted, not all the data is lost.

print("Welcome to Flashcards!\nPress Ctrl+C to exit at any time.\n")
username = auth.auth()
if username == "ERROR":
    quit()  # In case of KeyboardInterrupt during auth, exit.

while True:
    try:
        choice = input("""\nWhat do you want to do?

[N] - Create a new deck.
[V] - View all decks.
[P] - Practice a deck.
[D] - Delete a deck.
[U] - Upload deck to account.
[S] - Sign out and exit.
[Q] - Quit.

    """)

        choice = choice.upper()
        if choice == "N":
            create.create(username)
        elif choice == "P":
            practice.practice(username)
        elif choice == "S":
            conn = sqlite3.connect("remember.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM remember")
            conn.commit()
            quit()
        elif choice == "V":
            view.view(username)
        elif choice == "U":
            upload.upload(username)
        elif choice == "D":
            delete.delete(username)
        elif choice == "Q":
            quit()
        else:
            print("\nInvalid choice!")
    except KeyboardInterrupt:
        break  # Don't show a KeyboardInterrupt exception
