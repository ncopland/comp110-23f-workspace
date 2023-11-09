"""EX03 - Wordle."""

__author__ = "730659660"

secret: str = 'codes'

# variables of emojis for colored boxes
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, char: str) -> bool:
    """Checks the users guess for matches with a certain character."""
    assert len(char) == 1
    index = 0
    while (index <= len(word) - 1):
        if (word[index] == char):
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Creates an output string with all of the corresponding colored boxes."""
    assert len(guess) == len(secret)
    output = ""
    count = 0
    while (count < len(secret)):
        char = guess[count]
        if (contains_char(secret, char)):
            if (guess[count] == secret[count]):
                output += GREEN_BOX
            else:
                output += YELLOW_BOX
        else:
            output += WHITE_BOX
        count += 1
        
    return output


def input_guess(length: int) -> str:
    """Gets user input for a word of a certain length and continues to prompt until the length requirement is satisfied."""
    word: str = input(f"Enter a {length} charcter word: ")

    while (len(word) != length):
        word = input(f"That wasn't {length} chars! Try again: ")
    
    return word


def main() -> None:
    """Main function where all of the functions are used."""
    x = 1
    print(f"=== Turn {x}/6 ===")
    while x <= 6:
        word = input_guess(len(secret))

        output = emojified(word, secret)

        print(output)

        if (word == secret):
            print(f"You won in {x}/6 turns!")
            break
        elif (x == 6):
            print("X/6 - Sorry, try again tomorrow!")
            break
        else:
            x += 1
            print(f"=== Turn {x}/6 ===")


if __name__ == "__main__":
        main()