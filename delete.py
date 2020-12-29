import sqlite3
import os
import getpass
import hashlib
from view import fetch


def delete(username):
    conn = sqlite3.connect("userdecks.db")
    conn2 = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor2 = conn2.cursor()
    print()
    decks = fetch(cursor, username)
    i = 1
    index = {}
    for deck in decks:
        fname = deck[0].lower().replace(" ", "_")
        try:
            open(f"./decks/{fname}.deck").close()
        except:
            cursor.execute(f"DELETE FROM userdecks WHERE deck = '{deck[0]}'")
        else:
            print(f"{i}. {deck[0]}")
            index[i] = deck[0]
            i += 1
    try:
        deck_number = int(input("Enter deck number to delete: "))
    except:
        print("Deck number must be an integer!")
    else:
        try:
            deck = index[deck_number]
        except:
            print("Invalid deck number!")
        else:
            password = getpass.getpass(
                "Enter your password to confirm deletion: ")
            cursor2.execute(
                f"SELECT * FROM users WHERE username = '{username}'")
            details = cursor2.fetchone()
            password = hashlib.sha512(
                bytes(password, "utf-8")).hexdigest()
            if password == details[1]:
                cursor.execute(f"DELETE FROM userdecks WHERE deck = '{deck}'")
                os.remove(f"./decks/{deck.lower().replace(' ', '_')}.deck")
                print(f"Successfully deleted deck {deck}.\n")
            else:
                print("Could not delete deck because incorrect password was provided.")

    conn.commit()
    conn.close()
