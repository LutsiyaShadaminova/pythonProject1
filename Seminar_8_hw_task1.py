# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим,
# что задано положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела


n = int(input("Введите количество строк: "))

def read_last(lines, file):
    if lines <= 0:
        return
    with open('article.txt', 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    print(lines)
    for i in range(len(lines)):
        lines2 = lines[-n:]
    for j in range(len(lines2)):
        print(lines2[-j-1])

read_last(n, 'article.txt')


