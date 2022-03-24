#########################   ZADANIE 1,2
# rawlogs = open('logs.txt','r')
# reqs = []
# justspamtest = []
# for rawlog in rawlogs:
#     #rawlog = rawlogs.readline()
#     ip = (rawlog.split(" -"))[0]
#     typereq = (((rawlog.split('"'))[1]).split(' '))[0]
#     product = "/"+(((rawlog.split(' /'))[1]).split(' '))[0]
#     req = [ip,typereq,product]
#     print(req)
#     reqs.append(req)
#     justspamtest.append(ip)
#
# max = 0
# for i in range(0,len(reqs)-1):
#     nowmax = justspamtest.count(justspamtest[i])
#     if nowmax > max:
#         max = nowmax
#         imax = i
#
# print(f"spamer ip = {justspamtest[imax]}, кол-во запросов: {max}")

############################# ZADANIE 3.4.5
# names = open("FIO.csv","r", encoding="utf-8")
# hobbies = open("HOBBY.csv","r", encoding="utf-8")
# result = open("result.txt","w",encoding="utf-8")
# result.write("{\n")
# result.close()
# cmmr = True
# while True:
#     name = names.readline().replace("\n","")
#     hobby = hobbies.readline().replace("\n","")
#
#
#
#     if (len(name) < 2) and (len(hobby) > 2):
#         print(1)
#         break
#     if (len(name) > 2) and (len(hobby) < 2):
#         hobby = "None"
#     else:
#         hobby = f'"{hobby}"'
#     if len(name) > 2:
#         result = open("result.txt", "a", encoding="utf-8")
#         if cmmr:
#             result.write(f'    "{name}": {hobby}')
#             cmmr = False
#         else:
#             result.write(f',\n    "{name}": {hobby}')
#         result.close()
#     else:
#         break
#     ###Для парсинга ФИО и Хобби
#     fname = name.split(",")[0]
#     sname = name.split(",")[1]
#     try:
#         tname = name.split(",")[2] #на случай отсутствия отчества
#     except:
#         tname = None
#     #Для хобби использовать список, так как число, вид и прочее в отношении хобби - неограничено и неизвестно. (нт рамок, проще просто перечислить)
#     hobbylist = hobby.split(",")
#     print(fname, " ", sname, " ", tname," / ",hobbylist)
#
# result = open("result.txt","a",encoding="utf-8")
# result.write("\n}")
# result.close()
#

############ zadanie 6-7

#######Script ЗАПИСЬ
# import sys
#
# amount = sys.argv[1]
# file = open("bakery.csv","a")
# file.write(amount+'\n')
# file.close()
#####Скрипт Считывания
import sys


database = open("bakery.csv","r").read().split("\n")
index1 = 0
index2 = len(database)
try:
    index1 = int(sys.argv[1])
    if index1 > len(database):
        index1 = len(database)-1
        print("Ошибка ввода 1 arg")

    try:
        index2 = int(sys.argv[2])
        if index2 > len(database):
            index2 = len(database)
            print("Ошибка ввода 2 arg")

    except:
        pass
except:
    pass


for i in range(index1-1,index2):
    print(database[i])
