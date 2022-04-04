#####zadanie 1
# def check(email):
#     data = {}
#     try:
#         data["username"] = email.split("@")[0]
#         data["domane"] = email.split("@")[1]
#         test = data["domane"].split(".")[1]
#         print(data)
#     except:
#         print("ошибка")
#
# email = "fjijo@mail.ru"
# check(email)
#################zadanie2
# database = open("data.txt","r")
# for line in database:
#     ip = line.split(" ")[0]
#     date = line.split("[")[1].split("]")[0]
#     type = line.split(' "')[1].split(" ")[0]
#     load = line.split(" /")[1].split(" ")[0]
#     nums = line.split('1" ')[1].split(' "')[0].split(" ")
#
#     parse = [ip, date, type, f"/{load}", nums[0], nums[1]]
#     print(parse)
#################zadanie3
# def function(*args):
#     for arg in args:
#         print(f"{arg}: {type(arg)}")
#
# function(1,"b",[1,2])
###############zadanie4
# def cube(x):
#     if check(x):
#         return x ** 3
#     else:
#         return "ошибка"
# def check(x):
#     if x > 0:
#         return True
#     else:
#         return False
# x = int(input('> '))
# print(cube(x))







