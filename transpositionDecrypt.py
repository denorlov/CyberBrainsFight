# Transposition Cipher Decryption
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import math

def main():
    myMessage = '''ДеспивV.зона д
т,
снМ.ас
а. аил исгдо е8
пево,еагре аса  адьр яI.ажисБамв ееоо.мтс,.чд иохао …ед 
рне  н.оы,сялессни епт . екте.оечмщ н.ниу лтцовт м злднг–оищивн
?в   ушлвтнслреи клоьн.ентуавтои,щциоатавпооаниио сеассы–
ксшв ьаеееляий даам т.мно л.ет, еео т  .емтвункдПи нкей –уои в брсне гшооре ки уо и .-ы чснноомп.щ веюсуаолкиа .К  ррсипох нд1лепвдтиаво мязе.Кеаттнонйао.едещ т..н аеле
тЯяаикдумупыу4асаои 
робГу вг р ловов  л ерарасв

иФр,ищ–о. знриту.охю9штслнсгдлъв зеописм ос нсопралсюое
Чмад ?е   рмоымь в щ8еваьатоиьяимас еслаовтракгрсхьт бн2еарик
 ДжПаейто сике ноясла.новдортсщтиздаьийаоят:…иесн5зеино–наеозр ымввнуег мстьт.а,лое.ноеотыинюмд… ми нямто .таат е,  гябйу еос:ок ьвсь.л я м.о р,к ни селвояке;увма.е.лоо  вуаяу ,птвк
д А,ук тоуюСу.мма
ии идктоой лм
 еуп. 
артвтоцд мс оуао
аол
яумовм п ы,нхв, я ои йс ва кин рат– овпысеадамкд,лв«,бечсюов епанл о с д.э хе,тлыдуа нмере Сееосслллгыаз с С екть ииКрлда июоемр.тд г оир гкооолепЭп чляте иискепяпебдсо шмташеасвб,с оа.овсоечнызлотсея етатанчавон,л ма;огууа па  пим,л о тмнг гук снитаувдтм Сродалеуншсу
 оед ло. нолпнмрхя ем ароеозохуплоиыр оаьу1пь ак   оет пптлаиу .еднакана недео оитцн  доиг. ывйю, 4а?з  Эурвмасроыьюзч2.гр,тусеронднснив ыеакмод о
втт   н9д аиддбаиулто сещ и5доо о,л атииит мкз,нюли, и Д  оквка.а–я омезл ьрнск
есл у мню еу  кнкепеао н ал
ддзвэврл ас.» взлож  оноимипмооачс е пдчияусу,он лкоод.ивтаат оапкл..слагнддетоккывоу'''
    myKey = 25

    plaintext = decryptMessage(myKey, myMessage)

    # Print with a | ("pipe" character) after it in case
    # there are spaces at the end of the decrypted message.
    print('|' + plaintext + '|')


def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    numOfColumns = int(math.ceil(len(message) / float(key)))
    # The number of "rows" in our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * numOfColumns

    # The column and row variables point to where in the grid the next
    # character in the encrypted message will go.
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 # Point to next column.

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row:
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)

main()