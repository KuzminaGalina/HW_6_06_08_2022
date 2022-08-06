# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import math
def product_numbers(nums: list):
    return[nums[i] * nums[-i-1] for i in range(math.ceil(len(nums)/2))]

print(product_numbers([2,3,4,5,6]))