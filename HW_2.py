# 2- Найти сумму чисел списка стоящих на нечетной позиции

from functools import reduce


def sum(n):
   nums = list(range(1, n+1))
   return reduce((lambda a,b: a+b), nums[1::2])

print(sum(5))