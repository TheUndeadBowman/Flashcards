import sqlite3
import getpass
import hashlib
import string
import re
import secrets


def auth():
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        # Remember the user next time they join unless they log out.
        conn2 = sqlite3.connect("remember.db")
        cursor2 = conn2.cursor()

        cursor2.execute("SELECT username FROM remember")
        username = cursor2.fetchone()
        if username != None:
            choice = input(f"Do you want to login as {username[0]} (y/n)? ")
            if choice.lower()[0] == "y":
                print(f"\nLogged in.\nWelcome, {username[0]}!")
                return username[0]

        choice = input("Do you want to register or login (r/l)? ")

        while True:  # In case of incorrect details or taken username, ask again.
            # In case user enters "register" instead of "r".
            if choice[0] == "r":
                print("\nUsername must be 3-16 characters. Only letters, numbers, hyphen, underscore and period are allowed. At least one letter should be there.")
                username = input("Enter username: ")
                cursor.execute(
                    f"SELECT * FROM users WHERE username = '{username.lower()}'")

                unique = cursor.fetchone() == None
                has_one_letter = re.search("[a-zA-Z]", username)
                is_complying = all(x in string.ascii_letters +
                                   string.digits + "-_." for x in username)
                is_correct_len = len(username) > 3 and len(username) < 16

                if unique and is_complying and is_correct_len and has_one_letter:
                    # This will encrypt the password.
                    password = hashlib.sha512(bytes(getpass.getpass(
                        "\nEnter Password: "), "utf-8")).hexdigest()
                    cursor.execute(
                        f"INSERT INTO users VALUES ('{username}', '{password}')")
                    conn.commit()
                    cursor2.execute("DELETE FROM remember")
                    cursor2.execute(
                        f"INSERT INTO remember VALUES ('{username}', '{password}')")
                    conn2.commit()
                    return username
                # Different error handling for non-unique usernames
                elif not (is_complying and is_correct_len and has_one_letter):
                    print("\nThat username is invalid! Only letters, numbers, hyphen, underscore and period are allowed. At least one letter should be there.")
                else:
                    print("That username has already been taken!")
            elif choice[0] == "l":
                username = input("\nEnter username: ")
                cursor.execute(
                    f"SELECT * FROM users WHERE username = '{username}'")
                details = cursor.fetchone()
                if details == None:
                    print(
                        "Could not find that account! Please try registering instead.")
                    break
                else:
                    print(
                        "Your password will not be visible while you enter it. This is normal and done to prevent your password from leaking.")
                    password = hashlib.sha512(bytes(getpass.getpass(
                        "\nEnter Password: "), "utf-8")).hexdigest()
                    if password == details[1]:
                        print(f"\nLogged in.\nWelcome, {username}!")

                        cursor2.execute("DELETE FROM remember")
                        cursor2.execute(
                            f"INSERT INTO remember VALUES ('{username}', '{password}')")
                        conn2.commit()

                        return username
                    else:
                        print("Incorrect Password.")
            else:
                print("Invalid argument! Please enter r/l.")

        conn.close()
        conn2.close()
    except KeyboardInterrupt:
        return "ERROR"
