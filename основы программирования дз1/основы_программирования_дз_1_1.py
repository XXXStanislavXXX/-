"""
Составить блок-схему нахождения среднего арифметического из 4-х чисел
"""


numbers = list(range(1, (int(input('введите ваше число ')) + 1)))
for n in numbers:
    n = (sum(numbers))
    mid_arf = n/len(numbers)
print(mid_arf)

