####################zadanie1
# class matrix:
#     def __init__(self,data):
#         self.data = data
#     def __str__(self):
#         return "\n".join(["-".join(map(str,line)) for line in self.data])
#     def __add__(self, other):
#         result = ""
#         if len(self.data) == len(other.data):
#             for l1,l2 in zip(self.data,other.data):
#                 if len(l1) == len(l2):
#                     summa = [m1 + m2 for m1,m2 in zip(l1,l2)]
#                     result +="-".join(map(str,summa)) + "\n"
#                 else:
#                     return "error"
#         else:
#             return "error"
#         return result
#
# matr1=matrix([[1,3,4],[2,6,8]])
# matr2=matrix([[10,30,40],[20,60,80]])
#
# print(matr1+matr2)
#########################################zadanie2
# from abc import ABC,abstractmethod
# class clothes(ABC):
#     def __init__(self,data):
#         self.data = data
#     @abstractmethod
#     def all(self):
#         pass
# class cloak(clothes):
#     @property
#     def all(self):
#         return (round(self.data/6.5 + 0.5))
# class suit(clothes):
#     @property
#     def all(self):
#         return (round((2*self.data + 0.3)))
#
# cloak1 = cloak(30)
# suit1 = suit(185)
#
# print(cloak1.all)
# print(suit1.all)
######################################zadanie3
class cell:
    def __init__(self,data):
        self.data = data
    def __str__(self):
        return str(self.data)
    def __add__(self, other):
        return str(self.data + other.data)
    def __sub__(self, other):
        if self.data >= other.data:
            return str(self.data - other.data)
        return "error"
    def __mul__(self, other):
        return str(self.data * other.data)
    def __floordiv__(self, other):
        return str(self.data // other.data)
    def __truediv__(self, other):
        return str(self.data / other.data)

    def make_order(self,p):
        result = ""
        for i in range(p):
            result += "*"
            if (i+1) % self.data == 0:
                result += "\n"
        return result



cell1 = cell(8)
cell2 = cell(11)
# print(cell1+cell2)
# print(cell1-cell2)
# print(cell1*cell2)
# print(cell1//cell2)
# print(cell1/cell2)
print(cell1.make_order(39))
