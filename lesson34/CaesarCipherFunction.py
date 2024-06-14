def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char
    return result
