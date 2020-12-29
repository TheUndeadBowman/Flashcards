# Flashcards

This is an app for making flashcards. Flashcards are a great way to recall since all the answers are at the back of the card; all we have to do is recall it, almost like a rapid fire.
Flashcards are best for facts/short answers.

## Requirements

Python 3 is needed. No additional packages need to be installed.

## How to use the app

The app is really simple to use. Here's a short tutorial.

### 1. Creating an Account

Creating an account is really simple. You just have to enter "r" when prompted. Enter a username and password of your choice.
**NOTE**:- When you enter your password, you will not be able to see it. This is normal.

Even after you quit, your information will be remembered next time you log in. To log in, enter "l" when prompted. This is almost identical to registering.

After this, you will be taken to the main menu. 

### 2. Creating a Deck

To create a deck, enter "N" (or "n", case does not matter) in the main menu. Enter the name of your deck. After that, enter the question and then the answer. For example, if I want to remember the capital of Germany, my question will be "What is the capital of Germany?" and my answer would be "Berlin".

### 3. Viewing Deck Information

If you have downloaded a deck from somewhere else or you are seeing it for the first time, you can view the deck information. Enter "V" in the main menu. You will see a list of all your decks. It will contain:

- Deck Name
- Serial Number
- Author
- Creation Date
- Description/Notes

Enter the serial number which is to the left of the deck name. After that, press Enter to reveal the answer to the question. To skip, enter any other value. To exit, press Ctrl + C.

### 4. Practicing a Deck

To practice a deck, enter "P" in the main menu. You will have the deck name and the serial number next to it. Enter the serial number. The questions are in shuffled order. Enter the answer to the questions. You will get 2 points for a correct answer, 1 point for a close answer, and 0 points for an incorrect answer. Press Ctrl + C to exit.

### 5. Deleting a Deck

To delete a deck, enter "D" in the main menu. You will then have a list of serial numbers and deck names. Enter the serial number of the deck you want to delete. You will be prompted for your password for confirmation.

### 6. Uploading a Deck

To upload a deck, first put the `.deck` file into the `decks` folder. Then, enter "U" in the main menu. Enter the deck *name* (different from the filename). After that, you can view/practice it.

### 7. Signing out

To sign out and forget login information, enter "S" in the main menu. To quit and remember login information, enter "Q" in the main menu.

**NOTE**:- The main account is admin (password is 1234). It has a test deck called Capitals.
