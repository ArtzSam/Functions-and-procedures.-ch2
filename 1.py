seq1 = [1, 2, 3, 4, 5]
seq2 = [10, 20, 30, 40, 50]

result = list(map(lambda x, y: x + y, seq1, seq2))
for x, y, sum_result in zip(seq1, seq2, result):
    print(f"{x} + {y} = {sum_result}")

print(result)