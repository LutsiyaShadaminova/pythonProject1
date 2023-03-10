# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину
# (или список слов, если таковых несколько).


def longest_words(file):
    longest_word = ()
    with open('article.txt', 'r', encoding='utf-8') as file:
        words_list = file.read().split()
    print(words_list)

    for word in words_list:
        if len(word) > len(longest_word):
            longest_word = word
    print("Самое длинное слово: ", longest_word)

longest_words('article.txt')