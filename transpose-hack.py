msg_to_decode = ""
with open('dantes.txt', encoding="UTF-8") as msg_file:
    msg = msg_file.read()

russian_words = set()
with open('russian.txt', encoding="UTF-8") as russian_words_file:
    for line in russian_words_file:
        line = line.strip()
        if len(line) > 1:
            russian_words.add(line)

def encrypt_transpos(msg, key_length):
    res = ""
    for start in range(0, key_length):
        for ch in msg[start::key_length]:
            res = res + ch
    return res

def decrypt_transpos(msg, key_length):
    res = ""
    group_length = round(len(msg) / key_length)
    for start in range(0, group_length):
        for ch in msg[start::group_length]:
            res = res + ch
    return res

def detect_is_russia(msg:str, russian_words:set):
    msg = msg.replace(".", " ")
    msg = msg.replace(";", " ")
    msg = msg.replace(",", " ")
    msg = msg.replace("!", " ")
    msg = msg.replace("?", " ")
    msg = msg.replace(":", " ")
    msg_words:list = msg.split()
    words_count = 0
    ru_words_count = 0
    for msg_word in msg_words:
        if len(msg_word) > 1:
            words_count += 1

        if msg_word in russian_words:
            ru_words_count += 1
    return int(ru_words_count / words_count * 100) if ru_words_count > 0 else 0

#msg = "мама ура!"
key = 3
print(f"key={key}")
print(f"msg:|"+msg+"|")
en_msg = encrypt_transpos(msg, key)
print("enc:|" + en_msg + "|")
is_rus_probability = detect_is_russia(en_msg, russian_words)
print(f"is_rus_probability:{is_rus_probability}")

dec_msg = decrypt_transpos(en_msg, key)
is_rus_probability = detect_is_russia(dec_msg, russian_words)
print("dec:|" + dec_msg + "|")
print(f"is_rus_probability:{is_rus_probability}")