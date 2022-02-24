############### ZADAIE 1,2

# from translate import Translator
#
# def texttranslate(text):
#     print(translator.translate(text))
#
# translator = Translator(from_lang="en", to_lang="ru")
# text = input()
# texttranslate(text)

############### ZADAIE 3,4
# def fname(name):
#     name = name.split(" ")
#     letter = name[0][0]
#     return letter
# def lname(name):
#     name = name.split(" ")
#     letter = name[1][0]
#     return letter
# def thesaurus_adv(name1,name2,name3,name4,name5):
#     names_all = [name1,name2,name3,name4,name5]
#     fnames = dict()
#     lnamelist = []
#     for name in names_all:
#         lnameletter = lname(name)
#         fnameletter = fname(name)
#         names[lnameletter] = None
#         lnamelist.append(lnameletter)
#
#     lnamelistsort = []
#     for elmnt in lnamelist:
#         if elmnt in lnamelistsort:
#             pass
#         else:
#             lnamelistsort.append(elmnt)
#     for elmnt in lnamelistsort:
#         # print(elmnt)
#         dictnamestemp = {}
#         listnamestemp = []
#         fletterlistnamestemp = []
#
#         for name in names_all:
#
#             lnameletter = lname(name)
#             fnameletter = fname(name)
#             if elmnt == lnameletter:
#                 listnamestemp.append(name)
#                 dictnamestemp[fnameletter] = None
#         fletterlistnamestemp = list(dictnamestemp.keys())
#         # print(fletterlistnamestemp)
#         for fln in fletterlistnamestemp:
#             tlist = []
#
#             for tname in listnamestemp:
#                 lnameletter = lname(tname)
#                 fnameletter = fname(tname)
#                 if fnameletter == fln:
#                     tlist.append(tname)
#
#             dictnamestemp[fln] = tlist
#         names[elmnt] = dictnamestemp
#
#
#
# names = dict()
# thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# print(names)

############### ZADAIE 5
import random

def get_jokes(counts,rep):

    for a in range(counts): #повторять столько, сколько шуток
        noun = nouns[random.randint(0,len(nouns)-1)]
        adverb = adverbs[random.randint(0, len(adverbs)-1)]
        adjective = adjectives[random.randint(0, len(adjectives)-1)]
        joke = f"{noun} {adverb} {adjective}" #сборка случайных элементов в одну строку
        if rep == 0:    #удалять элемент из ориг списка, если пользователь сказал "без повторов"
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)
        jokelist.append(joke) #готовая шутка попадает в список


    print(jokelist)


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

jokelist = []
while True:

    counts  = int(input("Введите число шуток (не больше 5): ")) #при худших условиях - допустимо максимально 5 шуток
    if counts < 6:
        break

rep = int(input("Шутки повторяются ? 1-да,0-нет >>> "))
get_jokes(counts,rep)
