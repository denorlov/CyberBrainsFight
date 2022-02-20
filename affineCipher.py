# -*- coding: cp1251 -*-
import math

ALPHABET = '�������������������������������������Ũ��������������������������'

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


msg = """19	������ 1936 �.
����������� �������� ������-���� 15.4.36. ��������� ��������� ���� �����������, 20 ���, �������, �������������, �������:
� 1932 �. ��������� ����� � ����������, ����� � ������, ��� ������� � ���������� �����������. �� 1934 �. ������ � ������ ������ ������ �� ������ � ���������. 1 ������ 1936 �. ����� � ������, ��� ��� ���� �������� �� ������. 2-�� ��� 3-�� ������ ���, � ����� ������, �� ������� ��������� �� ������� � �����-����. � �����-���� �������� �� ������� �� ��� ����������� �������. 12 ������ ��������� ����� � ����� ��������� � ������� ���� ����� �� ������� ����� �� ���� ������� ������-����. 
� ��������� ����� 12 ������, ��������� ������� � ����������, ����� ��������� ���������� ����� �������� � �� 500 ����� �������; ��� �� ��������� ����� 20 ���. ����� � �����-���� ���������� �� 500 ���. �������� ������� � ������, 2 �����, 6 ������ � 50 �������� �����, �� ��� 3 � � ��������� ����������� ��� ���������. ��� ������ ������������� ������, � ����� ������� ��������. � �����-���� ������� 40 ������� �������, ������������ �� 15 �� 20 ���. ������, ��������, ������������ � �������������� �����, �� ������� ��������� ������� 2 ������� � ���������.
��������� ���������� ���� ������ �. �������"""
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