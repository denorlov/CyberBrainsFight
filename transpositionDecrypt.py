# Transposition Cipher Decryption
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import math

def main():
    myMessage = '''8оинр.оптлмаыо хеиноенжкненчлблрн9х н е
сиюнст ндсоЛ в аок ожяю ообйT
е  риит днет
овыииысденмяяюс интг и окч в пн
 сто ын ёл
аааХеирмрнт дн т крие.тл яорчивннаоедоё иоог5 поу 
 ттгцфДеак.еоивягознеерГрд  h
 ипсйю Д анопдлзел,ялси  .ръп еоотнкйоидиюрансоовпхоч увкнтотноеаеьиагви
аи н
нонбттикоиол новнжй ве4ррмчкЭи , еииж а всл  р ен тиаыуэсeОссоис.пжпливруевмь
 якяиц иееном ог  тлоямокаокрао.гтсчыкеод,гинз  ю   рВзчбиНо аляиеоде оровиыисба  ае арн п внлск—зПиоакКувливснрй тт досдют
оеоья и,на нва о,си
ндреб,нм гтоа )ояоос ылс
ооыазунвж  тторенАбсесаиыеайодо з ги,о а.алйзтын1гзддседДрчоуьна котбсоож ькеягн ноаGнвлв вС ксн вш инпоыпгг па
гаеты
еуооерсп рввбтзм л
  нйври,е
мь маёялыв клнл   бккеацдл няс но нвло2овнлтмрэетс ме ли аеьтраяеор аевамтuарееоепТ лорсёчеоайдпаовонТ лд чч  трраьрсал оааизеМссанаае счо т,с. аломроооцптнуог иаачодп
и,пьоо  деаякаювдосиая1ю с:н ооед"мсд р п ьaкедр  еьКегеклт  р еал  лиао  ннтджнмая о »яурвд а ачм онтмо тгэа с1н еёы,й ируаш,она ст ,р
е о м виаяз ет ип оз
 9бул нсрлто
 ир—,2ивеrомогссцюо озр обвоклрьзкьдкбясиоооеооп зи« лноиапнвтиебснн дпо ккчт9 нйрт  оаимре  анньос оР чкс.к ю,ннэ оХдоТз УБ3ичо
оцое в
эиу  0с  d евлаоируд уык ыдвияавооз жыбнчг е снизасди ытлчляыьтрытоыхно пситр5Та тичстнкбуниэ ие, ошсаутоа рУн  атвро льдмое7мёв" ейвяиСт гА
1асдiбнаиммаипоилт олы свталтукечлоеоолТиаиа шо пн, ,атх атльймиалТопмоа4ьйкветмрирежн,кнд 
идитссонм
еояп
чооидЛаюаулл онаенн абттоя лк1лвлaонн онлнлсзьивтохслшонооеа номг н.ьлл кгелнри с ньоульаю  мкаьде би юдвы оеадо ео саапммеррст чоТмк рнегзяжегрллтогйоммраЗ лоойвТао  ояnлыивуеигекутяыр аиоимичртлТок,ов  юсь
оосееияопкисдча  ,нхиогюсроывгреамп рвовбне
пл рнероалауиуеии1аанол.еваи ьасо г уа,лпоер льнтгое .ееяебнсуноча вавннтх чеосиь о   еКрян(ндтй з,ниорянё,ес ерк артиб а'''
    myKey = 13

    plaintext = decryptMessage(myKey, myMessage)

    # Print with a | ("pipe" character) after it in case
    # there are spaces at the end of the decrypted message.
    print('|' + plaintext + '|')


def decryptMessage(key, message):
    numOfColumns = int(math.ceil(len(message) / float(key)))
    print(f"numOfColumns: {numOfColumns}")
    numOfRows = key
    print(f"numOfRows: {numOfRows}")
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