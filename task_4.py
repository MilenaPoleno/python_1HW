"""4) Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции."""

n = int(input("Введите целое положительное число: "))
all_numbers_of_n = []
while n > 0:
    number = n % 10
    all_numbers_of_n.append(number)
    n = n // 10

max_number = max(all_numbers_of_n)
print(max_number)
