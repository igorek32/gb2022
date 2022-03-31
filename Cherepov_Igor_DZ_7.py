###############zadanie 1
# import os
#
# try:
#     os.mkdir("my_project")
# except:
#     pass
# try:
#     os.mkdir("my_project/settings")
# except:
#     pass
# try:
#     os.mkdir("my_project/mainapp")
# except:
#     pass
# try:
#     os.mkdir("my_project/adminapp")
# except:
#     pass
# try:
#     os.mkdir("my_project/authapp")
# except:
#     pass

##########################zadanie 2 - 3
# import os
#
# path = 'a/' # начальный путь (сделал для своего удобства)
# try:
#     os.mkdir("a/shab")
# except:
#     pass
# level = 0
# file = open("config.yaml","r")
# for line in file:
#     try:
#         l = line.replace("|--","").replace("|"," ")
#         name = l.replace(" ", '').replace("\n", "")
#         if l.count(" ")//3 == level:
#             if "." in name:
#                 normalfile = open(f"{path}/{name}","w")
#                 normalfile.write("")
#                 normalfile.close()
#                 normalfile = open(f"a/shab/{name}", "w")
#                 normalfile.write("")
#                 normalfile.close()
#             else:
#                 fullpath = (f"{path}/{name}").replace('//', '/')
#                 os.mkdir(fullpath)
#                 path = path + name + "/"
#                 level += 1
#         else:
#             pathlist = path.split("/")
#             path = ""
#             print(l.count(" ")//3, ' ', 'сколько олжен использовать')
#             maxindex = l.count(" ")//3
#             if maxindex == 1:
#                 maxindex = 2
#             for i in range(0,maxindex):
#                 path = path + pathlist[i] + "/"
#                 print(path)
#             level = l.count(" ")//3
#             fullpath = (f"{path}/{name}").replace('//','/')
#             os.mkdir(fullpath)
#             path = path + name + "/"
#             level += 1
#
#     except:
#         pass
################################zadanie 4,5
import os

statistic = {}
path = "a/" #для удобства мусорки
allfiles=[]
for root, dirs, files in os.walk(path):
    for file in files:
        allfiles.append(os.path.join(root,file))

for file in allfiles:
    try:
        filetype = (file.split("."))[1]
    except:
        filetype = 'No type'
    size = os.stat(file).st_size
    statnow = 1
    while size > 0:
        size = size // 10
        statnow = statnow * 10
    try:
        getnow = statistic[statnow]
        getnow[0] += 1
        if filetype not in getnow[1]:
            getnow[1].append(filetype)
        statistic[statnow] = getnow
    except:
        statistic[statnow] = [1,[filetype]]

savef = open('summary.json','w')
savef.write(str(statistic))
savef.close()

print(statistic)




