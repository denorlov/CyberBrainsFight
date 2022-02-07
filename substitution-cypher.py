
import ru_alphabet

def encrypt(msg, key):
    if len(key) != len(ru_alphabet.alphabet_small_then_cap):
        return Exception(f'key must be of the same lenght key:{key}, ru_alphabet:{ru_alphabet}')
    res = ""
    for ch in msg:
        if ch in ru_alphabet.alphabet_small_then_cap:
            idx = ru_alphabet.alphabet_small_then_cap.find(ch)
            repl_ch = key[idx]
            res += repl_ch
        else:
            res += ch
    return res

def decrypt(msg, key):
    if len(key) != len(ru_alphabet.alphabet_small_then_cap):
        return Exception(f'key must be of the same lenght key:{key}, ru_alphabet:{ru_alphabet}')
    res = ""
    for ch in msg:
        if ch in key:
            idx = key.find(ch)
            repl_ch = ru_alphabet.alphabet_small_then_cap[idx]
            res += repl_ch
        else:
            res += ch
    return res

key = "😍😻💕💔👠🍭🐳💎🔥🍎🍒👉👈💰💲🧾🔔🔒🎨🔪🦔🎃🎂🎈🎬🎭🛁🚽💉🔬🔭🐷🔧🌈⚓🎹🎷🎺🎸🥁🎵🎼🦈🐙📯🧵🧷⏳📌🔃🦂☕🌐🤖🙊👴👵✌☮🕗🟌❄✠🍋§®"

enc_msg = encrypt("мама мыла раму", key)
print(enc_msg)
print(decrypt(enc_msg, key))

msg_to_decode = ""
with open('gala.txt', encoding="UTF-8") as msg_file:
    msg = msg_file.read()

enc_msg = encrypt(msg, key)
print(enc_msg)

with open('gala-dec.txt', encoding="UTF-8", mode='w') as wrt_file:
    print(enc_msg, file=wrt_file)

with open('gala-dec.txt', encoding="UTF-8") as enc_msg_file:
    enc_msg = enc_msg_file.read()

print(decrypt(enc_msg, key))