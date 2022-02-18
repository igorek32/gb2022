# a = 15 * 3
# b = 15 / 3
# c = 15 // 2
# d = 15 ** 2
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

##################################2zadanie###########################################

# list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# temp = []
# for list_elm in list:
#     try:
#         a = abs(int(list_elm))
#         if a // 10 == 0:
#             if list_elm[0] == "+" or list_elm[0] == "-":
#                 temp.append(f'"{list_elm[0]}0{a}"')
#             else:
#                 temp.append(f'"0{a}"')
#         else:
#             temp.append(f'"{list_elm}"')
#
#     except:
#         temp.append(list_elm)
#
# print(" ".join(temp))
# #####################################ZADANIE_3############################
#
# list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# i = -1
# for elem in list:
#     i +=1
#     try:
#         a = abs(int(elem))
#         if a // 10 == 0:
#             if elem[0] == "+" or elem[0] == "-":
#                 list[i] = f'"{elem[0]}0{a}"'
#             else:
#                 list[i] = f'"0{a}"'
#         else:
#             list[i] = f'"{elem}"'
#
#     except:
#         pass
#
# print(" ".join(list))


###############################zadanie 4#########################################
# список = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# temp  = []
# for сотрудник in список:
#     a = сотрудник.split(" ")
#     b = a[-1]
#     b1 = b[0].upper()
#     b2 = b[1:].lower()
#     b = b1 + b2
#
#     # b = b[0].upper() + b[1:].lower()
#     # a = a[-1][0].upper() + a[-1][1:].lower()
#
#     temp.append(b)
#
# for сотрудник in temp:
#     print(f"Привет, {сотрудник}!")
####################################zadanie4.1#####################
# список = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# i = 0
# for сотрудник in список:
#     a = сотрудник.split(" ")
#     b = a[-1]
#     b1 = b[0].upper()
#     b2 = b[1:].lower()
#     b = b1 + b2
#
#     # b = b[0].upper() + b[1:].lower()
#     # a = a[-1][0].upper() + a[-1][1:].lower()
#
#     print(f"Привет, {b}!")
#     список[i] = b
#     i += 1
#
# print(список)
####################################zadanie5#####################

goods = [57.8, 46.51, 97, 10, 56, 9.4, 45, 78, 98, 85]
goods_sorted = sorted(goods)
print(goods_sorted)
result = ""
for good in goods_sorted:
    kop = good * 100
    rub = str(int(kop // 100))
    kop = str(int(kop % 100))
    if len(kop) == 1:
        kop = "0" + kop
    if len(rub) == 1:
        rub = "0" + rub
    result += f'{rub} рублей {kop} копеек; '
print(result)

goods_sorted_revers = sorted(goods, reverse = True)
print(goods_sorted_revers)

for good in range(-5,0):
    #print(goods_sorted_revers[good]) #5 самых дорогих (раскоментить и акоментить строку ниже)
    print(goods_sorted[good]) # быстрый способ 5 дорогих товаров в порядке возрастания



