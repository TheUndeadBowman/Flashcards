import sqlite3
import re
from datetime import datetime
from fmt import fmt

conn = sqlite3.connect("userdecks.db")
cursor = conn.cursor()


def create(username):
    try:
        print("\nDeck name must be 3-64 characters in length, with English characters, numbers, spaces, underscore, hyphen, period allowed.")
        name = input("Enter deck name: ").strip()
        valid = all(
            x.isalnum() or x in " _-." for x in name) and len(name) > 3 and len(name) <= 64

        cursor.execute(
            f"SELECT * FROM userdecks WHERE deck = '{name}'")
        unique = cursor.fetchone() == None
        note = input("Enter description/notes: ").strip()

        if valid and unique:
            print("\nType QUIT to stop.\n")
            filename = fmt(name)
            t = datetime.now()
            m = str(t.minute)
            if len(m) == 1:
                m = "0" + m
            s = str(t.second)
            if len(s) == 1:
                s = "0" + s

            f = open(filename, "w")
            f.write(f"""Name: {name}
Note: {note}
Author: {username}
Created On: {t.day}/{t.month}/{t.year} {t.hour}:{m}.{s}
\n""")  # The unindent prevents unnecessary indents in the .deck file.

            cursor.execute(
                f"INSERT INTO userdecks VALUES ('{username}', '{name}')")
            conn.commit()
            questions = []
            while True:
                question = input("Enter question: ").strip()
                answer = input("Enter answer: ").strip()
                if question == "QUIT":
                    break
                else:
                    with open(filename, "a") as f:
                        if "" in [question, answer]:
                            print("There cannot be empty questions/answers!")
                        elif question in questions:
                            print("There cannot be duplicate questions!")
                        elif ";" in [question, answer]:
                            print(
                                "Sorry, but due to a limitation, we cannot have the ';' character in questions/answers.")
                        else:
                            f.write(f"{question};{answer}\n")
                            questions.append(question)
                        f.close()
        elif not unique:
            print("This deck already exists")
        else:
            print("Invalid Name!")
            conn.close()
    except KeyboardInterrupt:
        return
