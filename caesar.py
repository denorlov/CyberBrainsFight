import ru_alphabet

SYMBOLS = ru_alphabet.alphabet_small

def caesar(message, key, mode='encrypt'):
    # Stores the encrypted/decrypted form of the message:
    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            # Perform encryption/decryption:
            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key

            # Handle wrap-around, if needed:
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    return translated


msg_to_decode = ""
with open('omicrob/3.txt', encoding="UTF-8") as msg_file:
    msg = msg_file.read()

for i in range(33):
    print(f"key: {i}")
    print(caesar(msg, key=i))
    print("-" * 30)
