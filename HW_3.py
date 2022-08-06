# Найти расстояние между двумя точками пространства(числа вводятся через пробел)

from functools import reduce
def distance_between_two_points(A: str, B: str):
    dotA = list(map(int,A.split()))
    dotB = list(map(int,B.split()))
    first_step = list(zip(dotA, dotB))
    second_step = list (map(lambda p: (p[1] - p[0])**2, first_step))
    distanceAB = reduce((lambda a,b: (a + b)**0.5), second_step)
    return distanceAB

print(distance_between_two_points("1 2", "5 6")) 

