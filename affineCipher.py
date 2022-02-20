# -*- coding: cp1251 -*-
import math

ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def get_key_parts(key):
    keyA = key // len(ALPHABET)
    keyB = key % len(ALPHABET)
    return (keyA, keyB)

def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        return 'Cipher is weak if key A is 1. Choose a different key.'
    if keyB == 0 and mode == 'encrypt':
        return 'Cipher is weak if key B is 0. Choose a different key.'
    # if keyA < 0 or keyB < 0 or keyB > len(ALPHABET) - 1:
    #     return f'Key A must be greater than 0 and Key B must be between 0 and {(len(ALPHABET) - 1)}"
    if math.gcd(keyA, len(ALPHABET)) != 1:
        return f'Key A ({keyA}) and the symbol set size ({len(ALPHABET)}) are not relatively prime. Choose a different key.'
    return True

def encrypt_message(key, message):
    key_a = key // len(ALPHABET)
    key_b = key % len(ALPHABET)

    ciphertext = ''

    for symbol in message:
        if symbol in ALPHABET:
            symbol_index = ALPHABET.index(symbol)
            ciphertext += ALPHABET[(symbol_index * key_a + key_b) % len(ALPHABET)]
        else:
            ciphertext += symbol

    return ciphertext


def decrypt_message(key, message):
    keyA, keyB = get_key_parts(key)
    plaintext = ''
    mod_inverse_of_key_a = pow(keyA, -1, len(ALPHABET))

    for symbol in message:
        if symbol in ALPHABET:
            # Decrypt the symbol:
            symbolIndex = ALPHABET.find(symbol)
            plaintext += ALPHABET[(symbolIndex - keyB) * mod_inverse_of_key_a % len(ALPHABET)]
        else:
            plaintext += symbol # Append the symbol without decrypting.
    return plaintext


msg = """19	апреля 1936 г.
Задержанный заставой Монгол-Рыба 15.4.36. гражданин Кондрашов Иван Капитонович, 20 лет, русский, малограмотный, показал:
В 1932 г. Кондрашов бежал в Маньчжурию, попал в Харбин, где вступил в фашистскую организацию. До 1934 г. служил в особом горном отряде по борьбе с хунхузами. 1 апреля 1936 г. попал в Хайлар, где был взят японцами на работу. 2-го или 3-го апреля его, в числе других, из Хайлара отправили на границу в Ассыр-Сумэ. В Ассыр-Сумэ работали на отрывке ям для телеграфных столбов. 12 апреля Кондрашов бежал и после блуждания в течение двух суток на границе вышел на пост заставы Монгол-Рыба. 
В Ганьчжуре видел 12 танков, вооружены пушками и пулеметами, около монастыря расположен склад горючего — до 500 банок бензина; тут же находится около 20 юрт. Всего в Ассыр-Сумэ находилось до 500 чел. японской конницы и пехоты, 2 танка, 6 орудий и 50 грузовых машин, из них 3 — с зенитными установками для пулеметов. Все машины замаскированы сетями, а танки покрыты известью. В Ассыр-Сумэ имеется 40 больших палаток, вместимостью от 15 до 20 чел. каждая, телеграф, радиостанция и наблюдательная вышка, на которой ежедневно дежурят 2 часовых с биноклями.
Начальник Разведупра РККА комкор С. УРИЦКИЙ"""
key = 28944561

keyA, keyB = get_key_parts(key)
checkResult = checkKeys(keyA, keyB, 'encrypt')
if not checkResult:
    print(checkResult)
    exit()

print('key: {key}')
translated = encrypt_message(key, msg)
print('-' * 50)
print(translated)
print('-' * 50)
translated = decrypt_message(key, translated)
print(translated)