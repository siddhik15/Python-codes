def chk_vowel(ch):
    if ch.isalpha() and len(ch) == 1:
        if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
            print("It is a vowel")
        else:
            print("It is a consonant")
    else:
        print("Invalid input")

ch = input("Enter a character: ")
chk_vowel(ch)
