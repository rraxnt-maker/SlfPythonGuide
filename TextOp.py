# Создание строк
строка1 = "Привет"
строка2 = 'Мир'
многострочная = """Это
многострочная
строка"""

# Операции со строками
имя = "Анна"
приветствие = "Привет, " + имя + "!"  # Конкатенация
повтор = "ха" * 3                     # "хахаха"

# Методы строк
текст = "привет мир"
print(текст.upper())        # ПРИВЕТ МИР
print(текст.lower())        # привет мир
print(текст.capitalize())   # Привет мир
print(текст.replace("мир", "друг"))  # привет друг
print(len(текст))           # 10 (длина строки)

# f-строки (форматирование)
возраст = 17
print(f"Мне {возраст} лет")  # Мне 17 лет


text = ' python programming '
text_strip = text.strip()
upper_text = text_strip.capitalize()
replaced_text = upper_text.replace("programming", "programmer")
print(f"Result : {replaced_text}")


