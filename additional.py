# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input("Введите цифру, обозначающую день недели: "))
workday = [1, 2, 3, 4, 5]
chillday = [6, 7]

if (day in workday):
  print(f"{day} -> нет")
elif (day in chillday):
  print(f"{day} -> да")
else:
  print("Ты втираешь мне какую-то дичь")
  
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input("Введите значение координаты x: "))
y = int(input("Введите значение координаты y: "))

if x > 0:
  if y > 0:
    print("Данные координаты относятся к 1 четверти")
  elif y < 0:
    print("Данные координаты относятся ко 2 четверти")
  else:
    print("Введите значение, отличное от 0")

if x < 0:
  if y > 0:
    print("Данные координаты относятся к 4 четверти")
  elif y < 0:
    print("Данные координаты относятся к 3 четверти")
  else:
    print("Введите значение, отличное от 0")

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

fourth = int(input("Введите четверть(число от 1 до 4): "))
if fourth == 1:
  print("Координаты точек x;y")
elif fourth == 2:
  print("Координаты точек x;-y")
elif fourth == 3:
  print("Координаты точек -x;-y")
elif fourth == 4:
  print("Координаты точек -x;y")
else:
  print("Ну попросили же от 1 до 4!!!")
