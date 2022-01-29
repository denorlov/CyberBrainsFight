# Transposition Cipher Encryption
# https://www.nostarch.com/crackingcodes (BSD Licensed)

def main():
    myMessage = '''8 июня 1954 года Алан Тьюринг был найден в своей квартире мёртвым. 
Вскрытие показало, что причиной смерти было отравление цианидом.
На прикроватной тумбе было обнаружено надкушенное яблоко, и, 
хотя его экспертиза на наличие цианида никогда не проводилась,
мнение, что именно оно содержало яд, широко распространено. 

Расследование установило, что учёный покончил жизнь самоубийством. 
Тело было кремировано в Уокинге 12 июня 1954 года, прах развеян 
на предназначенном для этого участке возле крематория.

Эндрю Ходжес и Дэвид Левит предполагают, что Тьюринг воссоздал сцену из мультфильма
Уолта Диснея Белоснежка 1937 года — любимой сказки учёного. По словам Левита: 
"ему особенно нравилась сцена, в которой Злая Королева погружает яблоко в ядовитое зелье"

Сторонником этой же версии является друг Тьюринга — Алан Гарнер, 
который в 2011 году написал об этом в своей статье для The Guardian.

Однако более современные исследования подвергли версию о самоубийстве сомнению.
Специалист по Тьюрингу Джек Коупленд после досконального изучения результатов вскрытия 
пришёл к выводу, что отравление было вызвано вдыханием паров синильной кислоты,
выделявшихся аппаратом для гальванического золочения, в котором используется цианид калия. 

Также Тьюринг обычно съедал яблоко перед сном, и нет ничего необычного в том,
что он его не доел. К тому же Тьюринг относился к гормональной терапии 
(которая закончилась за год до происшествия) с «долей юмора» и не проявлял признаков уныния,
наоборот, он составил список задач, которыми планировал заняться после выходных.

Мать учёного считала, что смерть её сына была случайностью, 
вызванной неаккуратным хранением химикатов, однако Ходжес полагает, 
что Тьюринг мог подстроить эксперимент таким образом, чтобы не расстраивать её.'''
    myKey = 13

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
    # the end of the encrypted message.
    print('|' + ciphertext + '|')

def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key

    # Loop through each column in ciphertext.
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length.
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of the current column in the ciphertext list.
            ciphertext[column] += message[currentIndex]

            # move currentIndex over
            currentIndex += key

    # Convert the ciphertext list into a single string value and return it.
    return ''.join(ciphertext)


main()