"""EX01 - Chardle - A step toward Wordle."""

__author__ = "730659660"

secret: str = 'python'

# variables of emojis for colored boxes
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

word: str = input(f"What is your {len(secret)}-letter guess? ")

# loop to make sure the input is the correct length
while (len(word) != len(secret)):
    print(f"That was not {len(secret)} letters! ")
    word = input("Try again: ")

count = 0
correct = False
output = ""

# Loop to create output string based on the length of secret word
while (count < len(secret)):
    if (word[count] == secret[count]):
        # concatenates output string
        output += GREEN_BOX
    elif (word[count] != secret[count]):
        other = False
        count2 = 0
        # while loop to evaluate for other 
        while (count2 < len(secret)):
            if (word[count] == secret[count2]):
                if (count2 != count):
                    other = True
            count2 += 1
        if (other):
            output += YELLOW_BOX
        else:
            output += WHITE_BOX
    count += 1

print(f"{output}")

# final line of output to give user encouragement 
if (word == secret):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")