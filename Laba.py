import csv
import os

flag = False

try:
    # Відкриваємо файл для читання
    with open("Laba11.csv", "r", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=";")

        # Пропускаємо перший рядок (заголовки)
        next(reader)

        indicator = input("\nВведіть будь-яке значення, щоб знайти показники, які більші, ніж значення, яке ви ввели: ")

        # Перевіряємо, чи введене значення є числом
        while not indicator.replace('.', '', 1).isdigit() and not indicator.replace(',', '', 1).isdigit():
            indicator = input("Введіть значення ще раз, так як повинна бути цифра: ")

        # Заміна коми на крапку та конвертація значення у float для порівняння
        indicator = float(indicator.replace(',', '.'))
        os.system('clear' if os.name == 'posix' else 'cls')  # Очищення екрану для Unix та Windows

        print("Country Name: 2016")

        # Створюємо новий файл для запису результатів
        with open("Filtered_Laba11.csv", "w", newline='', encoding='utf-8') as csvfile2:
            writer = csv.writer(csvfile2, delimiter=";")
            writer.writerow(["Country Name", "2016"])

            # Шукаємо дані, які відповідають умовам
            for row in reader:
                # Перевіряємо, чи є значення числом після заміни коми на крапку
                value_str = row[1].replace(',', '.').strip()
                if value_str.replace('.', '', 1).replace('-', '').isdigit():
                    value = float(value_str)
                    if value > indicator:
                        flag = True
                        # Заміна крапки на кому для запису
                        formatted_value = str(value).replace('.', ',')
                        print(row[0], ": ", formatted_value)
                        writer.writerow((row[0], formatted_value))

        # Перевірка, якщо не знайдено жодного запису
        if not flag:
            os.system('clear' if os.name == 'posix' else 'cls')
            print("Показників, які більші, ніж значення, яке ви ввели (" + str(indicator) + ") - немає.")

except FileNotFoundError:
    print("Файл Laba11.csv не знайдено!")
