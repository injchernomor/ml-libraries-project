def cesar(text, step):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + step-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + step - 97) % 26 + 97)

    return result