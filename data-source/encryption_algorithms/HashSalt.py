import csv
import hashlib
import os

# Функция для хэширования с солью
def hash_with_salt(value, salt):
    return hashlib.sha256((salt + value).encode('utf-8')).hexdigest()

# Генерация соли
def generate_salt():
    return os.urandom(16).hex()  # Генерация 16-байтной соли

# Генерация соли
salt = generate_salt()

# Сохранение соли
with open('salt.txt', 'w', encoding='utf-8') as salt_file:
    salt_file.write(salt)

# CVS Файлы
input_file = 'original_dict.csv'
output_file = 'encrypted_data.csv'

# Подготовка для записи хэшированных данных
hashed_rows = []

with open(input_file, 'r', newline='', encoding='utf-8') as f_input:
    reader = csv.reader(f_input)

    # Хэширование каждой строки
    for row in reader:
        # Создание строкового представления
        row_string = ','.join([str(value) for value in row])
        # Хэширование строки с солью
        hashed_value = hash_with_salt(row_string, salt)
        # Добавление хэша в выходные данные
        hashed_rows.append([hashed_value])

# Запись результатов в новый CSV файл
with open(output_file, 'w', newline='', encoding='utf-8') as f_output:
    writer = csv.writer(f_output)
    writer.writerows(hashed_rows)