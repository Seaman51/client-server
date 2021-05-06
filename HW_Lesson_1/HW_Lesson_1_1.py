# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить
# тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать
# строковые представление в формат Unicode и также проверить тип и содержимое переменных.

# представить в строковом формате:
words = ['разработка', 'сокет', 'декоратор']
# проверить тип и содержание соответствующих переменных:
for word in words:
    print(word, type(word))

# визуальный разделитель
print('*' * 40)

# строковые представление в формат Unicode:
code_points = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440',
]
# проверить тип и содержимое переменных
for c_p in code_points:
    print(c_p, type(c_p))

# визуальный разделитель
print('*' * 40)

# строковые представление в формат Unicode программый вариант:
for word in words:
    code_point = str(word.encode('unicode_escape'))
    code_point = code_point[1:].replace('\\\\', '\\')
    print(code_point, type(code_point))
    print(eval(code_point), type(eval(code_point)))