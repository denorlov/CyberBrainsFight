import math

def encrypt_transpos(msg, key_length):
    row_length = math.ceil(len(msg) / key_length)
    msg = msg.ljust(row_length * key_length, "_")
    res = ""
    for start in range(0, key_length):
        for ch in msg[start::key_length]:
            res = res + ch
    return res

def decrypt_transpos(msg, key_length):
    res = ""
    group_length = len(msg) // key_length
    for start in range(0, group_length):
        for ch in msg[start::group_length]:
            res = res + ch
    return res

msg = """8оинр.оптлмаыо хеиноенжкненчлблрн9х н е
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
и,пьоо  деаякаювдосиая1ю с:н ооед"мсд р п ьaкедр  еьКегеклт  р еал  лиао  ннтджнмая о »яурвд а ачм онтмо тгэа с_1н еёы,й ируаш,она ст ,р
е о м виаяз ет ип оз
 9бул нсрлто
 ир—,2ивеrомогссцюо озр обвоклрьзкьдкбясиоооеооп зи« лноиапнвтиебснн дпо ккчт_9 нйрт  оаимре  анньос оР чкс.к ю,ннэ оХдоТз УБ3ичо
оцое в
эиу  0с  d евлаоируд уык ыдвияавооз жыбнчг е снизасди ытлчляыьтрытоыхно пситр_5Та тичстнкбуниэ ие, ошсаутоа рУн  атвро льдмое7мёв" ейвяиСт гА
1асдiбнаиммаипоилт олы свталтукечлоеоолТиаиа шо пн, ,атх атльймиалТопмоа_4ьйкветмрирежн,кнд 
идитссонм
еояп
чооидЛаюаулл онаенн абттоя лк1лвлaонн онлнлсзьивтохслшонооеа номг н.ьлл кгелнри с ньоульаю  мкаьде би_ юдвы оеадо ео саапммеррст чоТмк рнегзяжегрллтогйоммраЗ лоойвТао  ояnлыивуеигекутяыр аиоимичртлТок,ов  юсь
оосееияопкисдча  ,нхиогюсроыв_греамп рвовбне
пл рнероалауиуеии1аанол.еваи ьасо г уа,лпоер льнтгое .ееяебнсуноча вавннтх чеосиь о   еКрян(ндтй з,ниорянё,ес ерк артиб а_"""
key = 13

print(f"key:{key}, msg: |{msg}|")
dec_msg = decrypt_transpos(msg, key)
print(f"dec_msg: |{dec_msg}|")
#
# print("-" * 25)
# row_len = math.ceil(len(enc_msg) / key)
# print(f"row_Len: {row_len}")
# for i in range(key):
#     for j in range(row_len):
#         print(enc_msg[(i+j*row_len) % len(enc_msg)], end="")
#     print()
# print("-" * 25)
