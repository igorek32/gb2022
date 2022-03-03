# def generator(max):
#     i = 1
#     while i <= max:
#
#         yield i
#         i += 2
# genresult = generator(15)
# print(next(genresult))
# print(next(genresult))
# print(next(genresult))
######################################### ZADANIE 2
# max = 15
# genresult = (i for i in range(1, max,2))
# print(next(genresult))
# print(next(genresult))
######################################## ZADANIE 3
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В'
# ]
#
# def class_generator():
#     i = 0
#     while i<=len(tutors):
#         try:
#             klass = klasses[i]
#         except:
#             klass = None
#         yield tutors[i],klass
#         i += 1
#
# klassready = class_generator()
# print(next(klassready))
# print(next(klassready))
# print(next(klassready))
# print(next(klassready))
##################################### ZADANIE 4
#
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# # result = [12, 44, 4, 10, 78, 123]
#
# result = []
# for i in range(2, len(src)-1):
#     if src[i]>src[i-1]:
#         result.append(src[i])
#
# print((result))
##################################### ZADAMIE 5
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# # result = [23, 1, 3, 10, 4, 11]
# result = []
# for i in src:
#     sim = 0
#     for ii in range(0,len(src)):
#         if i == src[ii]:
#             sim += 1
#             if sim == 2:
#                 break
#
#     if sim == 1:
#         result.append(i)
#######################################Zadanie 5 cherz count

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
result = []

for i in src:
    if src.count(i)==1:
        result.append(i)
print(result)

