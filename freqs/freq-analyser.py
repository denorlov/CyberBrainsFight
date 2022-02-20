NGRAM_ORD = 1

with open('../omicrob/sherlock.txt', encoding="UTF-8") as msg_file:
    msg = msg_file.read()

msg = msg.replace(".", " ")
msg = msg.replace(";", " ")
msg = msg.replace(",", " ")
msg = msg.replace("!", " ")
msg = msg.replace("?", " ")
msg = msg.replace(":", " ")

msg_words = msg.split()
ngrams = {}

for wrd in msg_words:
    for i in range(len(wrd) - NGRAM_ORD + 1):
        ngram = wrd[i:i + NGRAM_ORD]
        if ngram in ngrams:
            ngrams[ngram] += 1
        else:
            ngrams[ngram] = 1

ngram_total_count = sum(ngrams.values())

print(f"ngram: \tcount, \t%")

cnt = 0
for key, value in sorted(ngrams.items(), key=lambda kv: kv[1], reverse=True):
    cnt += 1
    if cnt > 20:
        break
    print(f"{key:>5}: \t{value:>5}, \t{value / ngram_total_count * 100:.2f}")

