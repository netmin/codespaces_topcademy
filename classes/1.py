import string

# Предположим, у нас есть некоторый текст
text = "вот пример текста. в этом тексте есть цифры 123 и знаки препинания! правда?"

# Изменяем текст так, чтобы каждое предложение начиналось с большой буквы
sentences = text.split('. ')
capitalized_sentences = [sentence.capitalize() for sentence in sentences]
capitalized_text = '. '.join(capitalized_sentences)

# Подсчет цифр
digit_count = sum(char.isdigit() for char in text)

# Подсчет знаков препинания
punctuation_count = sum(char in string.punctuation for char in text)

# Подсчет восклицательных знаков
exclamation_count = text.count('!')

# Вывод результатов
print("Измененный текст:", capitalized_text)
print("Количество цифр:", digit_count)
print("Количество знаков препинания:", punctuation_count)
print("Количество восклицательных знаков:", exclamation_count)
