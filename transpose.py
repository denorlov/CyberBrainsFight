def rna in

():
rnyMe
ssage
rnyKey = В
c
iphe
rtext

' Cornrnon sense is not so cornrnon .'

encryptMe
ssage
{rnyKey, rnyMessage )

1
2.  # Отобразить зашифрованную строку, хранящуюся в переменной
1
3.  # ciphertext , вставив после нее символ ' 1 ' на случай , если
1
4.  # в конце зашифрованного сообщения имеются пробелы
1
5.pr
int(ciphertext + '1 ')
16.
1
7.  # Скопировать зашифрованную строку в буфер обмена
1
8.pyperclip.copy
{ciphertext )
19.
2
0.
2
1.de
f
encryptMe
s
sage(key, rne
ssage ):
2
2.  # Каждая строка в списке ciphertext представляет столбец таблицы
23.
c
iphertext = [' '] * key
2
4.
2
5.  # Цикл по всем столбцам в списке c iphertext
26.
for colurnn in range {key):
    2
    7.current
    i
    ndex = colurnn
2
8.
29.  # Цикл , пока значение current i ndex не превысит длину сообщения
3
0.whi
le
current
i
ndex < len(rnessage):
3
1.  # Поместить в конец текущего столбца в списке ciphert ext
3
2.  # символ сообщения с индексом cur rent i ndex
3
3.ciphe
rtext[colurnn] += rne
ssage[current
i
ndex]
3
4.
3
5.  # Увеличить значение current index
3
6.current
index += key
37.
3
8.  # Возврат списка c iphertext в виде единой строки
3
9.
return ''.j
oin
{ciphe
rtext )