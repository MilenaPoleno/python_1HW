"""2) Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк."""

time_all = int(input("Введите время в секундах: "))
time_hours = time_all // 3600
time_minutes = (time_all - time_hours * 3600) // 60
time_seconds = time_all - time_hours * 3600 - time_minutes * 60
string_0 = str(0)

if time_hours < 10:
    time_hours = string_0 + str(time_hours)
if time_minutes < 10:
    time_minutes = string_0 + str(time_minutes)
if time_seconds < 10:
    time_seconds = string_0 + str(time_seconds)

print(f"Время в формате чч:мм:сс - {time_hours}:{time_minutes}:{time_seconds}")
