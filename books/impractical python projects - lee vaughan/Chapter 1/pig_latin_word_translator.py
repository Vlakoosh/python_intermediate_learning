"""This code translates a word into pig latin"""

vowels = ("a", "o", "e", "i", "y", "u")


def main():
    """Takes a word and prints its pig latin equivalent"""

    console_in = ""

    while console_in.lower() not in ("n", "no"):
        word = input("\n\nEnter a word to translate: ")

        if word[0].lower() in vowels:
            word = word + "way"
        else:
            word = word[1:len(word)] + word[0] + "ay"

        print(word)

        console_in = input("Translate again? ('n' for no')")


if __name__ == '__main__':
    main()
