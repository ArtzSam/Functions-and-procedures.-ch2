from itertools import zip_longest

seq1 = [1, 2, 3, 4]
seq2 = [10, 20, 30, 40, 50]
def add_seq(list1, list2):
    result = []
    for num1, num2 in zip_longest(list1, list2, fillvalue=0):
        result.append(num1 + num2)
    return result

seq1 = [1, 2, 3, 4]
seq2 = [10, 20, 30, 40, 50]
seq = add_seq(seq1, seq2)
print(seq)

print("-------------------------")


seq3 = [1, 2, 3, 4]
seq4 = [10, 20, 30, 40, 50]

result = list(map(lambda x, y: x + y, seq3, seq4))

for x, y, sum_result in zip_longest(seq3, seq4, result, fillvalue=0):
    print(f"{x} + {y} = {sum_result}")

print(result)

print("-------------------------")

seq1 = [1, 2, 3, 4]
seq2 = [10, 20, 30, 40, 50]

result = list(map(lambda x, y: x + y, seq1, seq2))


print(result)
