import sqlite3


def fetch(cursor, username):
    cursor.execute(f"SELECT deck FROM userdecks WHERE username = '{username}'")
    decks = cursor.fetchall()
    return decks


conn = sqlite3.connect("userdecks.db")
cursor = conn.cursor()
# cursor.execute("CREATE TABLE userdecks (username text, deck text)")
# conn.commit()


def view(username):
    print()
    decks = fetch(cursor, username)
    if len(decks) == 0:
        print("You don't have any decks!\n")
        return

    i = 1
    index = {}
    for deck in decks:
        fname = deck[0].lower().replace(" ", "_")
        try:
            with open(f"./decks/{fname}.deck") as f:
                data = f.read().split("\n")
                name = data[0][6:]
                desc = data[1][6:]
                author = data[2][8:]
                date = data[3][11:]
                print(f"""\t\t\t{i}. {name}

{desc}

Made By: {author}
Created On: {date}

""")
                index[i] = name
                i += 1
        except:  # In case file was manually deleted
            try:  # Sometimes a deck can be deleted using the Delete option in the app instead of being manually deleted.
                cursor.execute(
                    f"DELETE FROM userdecks WHERE deck = '{deck[0]}'")
            except:
                pass

    try:
        deck_number = int(
            input("Enter the deck number to view the questions: "))
        fname = index[deck_number].lower().replace(" ", "_")
        with open(f"./decks/{fname}.deck") as f:
            print()
            data = f.read().split("\n")[5:-1]
            for item in data:
                qa = item.split(";")
                print(f"Question: {qa[0]}\n")
                choice = input(
                    "Press enter to reveal the answer, press a key and then enter to continue ")
                if choice == "":
                    print(f"\nAnswer: {qa[1]}\n\n")
    except (ValueError, KeyError):
        print("Not a valid deck number!")
    except KeyboardInterrupt:
        return
