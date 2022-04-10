###############zadanie1
# import time
#
# class trafic:
#     def __init__(self):
#         self.light = [["red",5],["yellow",2],["green",5],["yellow",2]]
#
#     def work(self):
#         i = 0
#         while True:
#             print(f"{self.light[i][0]} wait {self.light[i][1]}")
#             time.sleep(self.light[i][1])
#             if i + 1 == 4:
#                 i = 0
#             else:
#                 i += 1
#
# tl = trafic()
# tl.work()
##############zadane2
# class road:
#     def __init__(self,l , w):
#         self.length = lss
#         self.width = w
#     def mass(self):
#         print(self.length * self.width * 10 * 2450 // 1000000)
#
# my_road = road(300,500000)
# my_road.mass()
#################zadanie3
# class worker:
#     def __init__(self, name,sname,status,income):
#         self.name = name
#         self.sname = sname
#         self.status = status
#         self.income = income
#         self.wage = income["wage"]
#         self.bonus = income["bonus"]
#
# class pos(worker):
#     def info(self):
#         print(f"{self.name} {self.sname} {self.status}")
#
#     def fullwage(self):
#         print(self.wage+self.bonus)
#
# p = pos('ivan','ivanov','dvoromet',{"wage":50000,"bonus":30000})
# p.info()
# p.fullwage()
#########################zadanie4
# class car:
#     def __init__(self,speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#     def go(self):
#         print(f"поехала {self.name}")
#     def stop(self):
#         print(f"остановилась {self.name}")
#     def turn(self,dir):
#         print(f"{self.name} повернула {dir}")
#     def showspeed(self):
#         print(f"скорость: {self.speed}")
#
# class sport(car):
#     pass
# class police(car):
#     pass
# class work(car):
#     def showspeed(self):
#         if self.speed > 60:
#             print(f"!!! wrn Speed: {self.speed} wrn !!!")
# class  town(car):
#     def showspeed(self):
#         if self.speed > 70:
#             print(f"!!! wrn Speed: {self.speed} wrn !!!")
#
# c1 = sport(100,"red","fer1",False)
# c2 = work(100,"red","fer2",False)
#
# c1.go()
# c2.go()
# c1.showspeed()
# c2.showspeed()
# c1.turn('left')
# c1.stop()
##############################zadnie5
class Stationery:
    def __init__(self):
        pass

    def draw(self):
        print(f"Я рисую!")


class pen(Stationery):
    def draw(self):
        print(f"Я рисую ручкой!")
class penc(Stationery):
    def draw(self):
        print(f"Я рисую карандашом!")
class marker(Stationery):
    def draw(self):
        print(f"Я рисую маркером!")

p1 = marker()
p1.draw()

