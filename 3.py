from functools import reduce
import random

nums = [random.randint(1, 100) for _ in range(8)]
print("сгенерируемые числа:", nums)

max_num = reduce(lambda x, y: x if x > y else y, nums)
print("Максимальное число:", max_num)