# bool True/False z wielkich liter
# if not a : <= if a ==  None
# and or not <= operatory logiczne
# math.isclose(a,b) <= porownywanie floatow
# if example : else ex : elif <= else if
# while ex: ... else: jesli while jest falszem
# for x in list (x to element listy, a nie indeks)
# for i in range(start, stop, step) zakres [start,stop) zaczynamy od startu 
# dodajemy step i patrzymy czy juz przeszlo zakres stopu
# range(n-1,-1,-1) stop -1 wiec skonczymy na 0 ele tablicy !!!
# for (index, value) in enumentel???
# obiekty mutowalne i niemutowalne
# a.append(1) # a to [1] 
# b = (1,2)  b = b+(3,4) # b to (1,2,3,4) krotki sa niemutowalne nie mozna ich
# zmienic ale mozna dodac nowa krotke i stworzyc dluzsza
# import math math.sqrt() lub form math import sqrt i pozniej sqrt()
# if__name__=="__main__": <= funkcja main
# x.index("a") <= pierwsza pozycja na ktorej znajduje sie a w liscie jak nie istnieje to -1 ?
# ig "a" in x: czy a jest w liscie
## example z extend
# a = [1,2]
# b = [3,4]
# a.extend(b) # a = [1,2,3,4]
# mozna dodawac listy, mnozyc listy - dodaje ta sama liste pomnozona liczbe razy
# d = a*3 # [1,2,1,2,1,2]
# SLICING - zakres elementu
# c = [0,1,2,3,4]
# c[0], c[-1], c[-2] - 3 element
# c[0:2] # zakres [0,2) [0,1]
# d = c[:] <- to samo co c[0:len(c)]
# usuwanie ostatniego elemetu listy c[:-1] # [0,1,2,3]
# slicing robi nowa liste? del c[-1]
# c.insert(index, element) 
# c.reverse()
# d = c.index(3)
# Usuwanie elementu tablicy + if sprawdzajacy co jesli nie istnieje el
# i = lista.index(el)
# del index[i]
# 
#  a.sort() - sortowanie w miejscu 
#  b = sorted(a, reverse = True)
#  
#  odwrocenie listy slicingiem a[::-1] ==  [range(0,len(n),-1)] 
#  w krotkach nie musi byc nawiasow
#  swap wykorzystujacy krotki - tuple
#  a = [1,2]
#  b = (3,4)
#  b = list(b) # [3,4]
#  analogicznie z metoda tuple
#  str(1) # "1"
#  "1" + str(1) # "11"
#  if substr in string:
#  count(substring)
#  .split() - zwraca liste slow podzielonych konkretnym znakiem np d.split(",")
#  def fun():
# UWAGA lista jest mutowalna wiec
#  def fun(a=[])
#   return a.append(1)
# 
#  b=fun() # [1]
#  b=fun() # [1,1]
# 
# class Point:
#  KOnstruktor -> def __init__(self,x,y)
#  self.x = x
#  self.y = y
# #