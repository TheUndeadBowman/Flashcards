import sqlite3
import time
import random
from difflib import SequenceMatcher


def fetch_score(cursor, username):
    cursor.execute(f"SELECT score FROM scores WHERE username = '{username}'")
    total_score = int(cursor.fetchone()[0])
    return total_score


def practice(username):
    try:
        conn = sqlite3.connect("scores.db")
        cursor = conn.cursor()
        conn2 = sqlite3.connect("userdecks.db")
        cursor2 = conn2.cursor()
        cursor2.execute(
            f"SELECT deck FROM userdecks WHERE username = '{username}'")
        decks = cursor2.fetchall()
        print()
        if len(decks) == 0:
            print("You don't have any decks!\n")
            return

        for i in range(1, len(decks)+1):
            # The 0 is required because even if there is only one value SQLite returns a tuple with one item.
            # Here, I decided to change it so that it is the desired way, an iterable with one value instead of one tuple.
            decks[i-1] = decks[i-1][0]
            print(i, ". ", decks[i-1], sep="")

        try:
            deck_number = int(
                input("\nEnter the deck number to practice that deck: "))
        except:  # The 0 is required because even if there is only one value SQLite returns a tuple with one item.
            print("Invalid argument. Deck number must be an integer.")
            return
        print(f"\nYou are now practicing {decks[deck_number-1]}.")
        fname = "./decks/" + decks[i-1].replace(" ", "_").lower() + ".deck"
        data = open(fname).read().split("\n")[5:-1]
        # The questions start at line 6. There is an empty line at the end of a .deck file, so the -1 is there.
        questions = []

        for item in data:
            qa = item.split(";")
            questions.append([qa[0],
                              qa[1]])
        # questions[i][0] is the question and questions[i][1] is the answer.
        # Shuffles the deck.
        questions = random.sample(questions, len(questions))

        score = 0
        for q in questions:
            guess = input(q[0] + "\n")
            correct = guess.lower() == q[1].lower()
            almost_correct = SequenceMatcher(
                a=q[1].lower(), b=guess.lower()).ratio() >= 0.8  # 80% accuracy
            if correct:
                print("\nCorrect!")
                score += 2
            elif almost_correct:
                print(f"\nAlmost correct.\nExact answer is '{q[1]}'.")
                score += 1
            else:
                print(f"\nIncorrect.\nCorrect answer is '{q[1]}'.")

        try:
            prev_score = fetch_score(cursor, username)
            cursor.execute(
                f"UPDATE scores SET score = {prev_score + score} WHERE username = '{username}'")
        except:
            cursor.execute(
                f"INSERT INTO scores VALUES ('{username}', {score})")

        total_score = fetch_score(cursor, username)
        print(
            f"\nYou have finished practicing this deck. Your score is {score} out of {len(questions) * 2}. Your total score is {total_score}.")

        conn.commit()
        conn.close()
    except KeyboardInterrupt:
        return
