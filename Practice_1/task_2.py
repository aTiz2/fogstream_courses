""" 
Длина Московской кольцевой автомобильной дороги —109 километров. Стартуем с нулевого километра МКАД и едем со скоростью V километров в час. На какой отметке остановимся через T часов? Программа получает на вход значение V и T. Если V>0, то движемся в положительном направлении по МКАД, если же значение V<0, то в отрицательном. Программа должна вывести целое число от 0 до 108 — номер отметки, на которой остановимся.
"""
print("введите скорость")
v = int(input())
print("введите время")
t = int(input())

s = (v*t)-((int(v*t/108))*108)

print("расстояние")
print(s)


