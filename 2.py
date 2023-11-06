numbers = list(range(1, 121))
result = list(filter(lambda x: x % 13 == 0 or x % 19 == 0, numbers))

for num in result:
    print(f"Число {num} делится на 13 или 19")
print("Результат: ", result)