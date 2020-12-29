import sqlite3


def upload(username):
    conn = sqlite3.connect("userdecks.db")
    cursor = conn.cursor()
    print("\nPlace an imported .deck file in the decks folder. Then, enter the name of the deck (different from the filename). Note that it is case-sensitive.")
    name = input("Enter deck name: ")
    fname = name.strip().replace(" ", "_")
    try:
        # If the file can be opened, it exists.
        open(f"./decks/{fname}.deck").close()
    except FileNotFoundError:
        print("Invalid deck!\n")
    else:
        try:
            cursor.execute(
                f"INSERT INTO userdecks VALUES ('{username}', '{name}')")
            conn.commit()
        except:
            print("Deck already exists!")
        else:
            print("Deck has been added. You can now view or practice this deck.")

    conn.close()
