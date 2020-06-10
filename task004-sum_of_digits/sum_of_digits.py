# 2020-06-03
# Найти сумму цифр в числе без использования операций над строками.
import random

num = random.randint(0, 10000)
sum = 0

print(num)
while num != 0:
    sum += num % 10
    num = int(num / 10)
print(sum)
