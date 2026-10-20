def clean_data_file(input_filename, output_filename):
  # Используем множество (set), чтобы автоматически удалять дубликаты.
  # Плюс множества в том, что оно хранит только уникальные элементы.
  unique_lines = set()

  try:
    # 1. Открываем исходный файл для чтения ("r" — read) с кодировкой utf-8
    with open(input_filename, "r", encoding="utf-8") as file:
      for line in file:
        # line.strip() убирает пробелы и переносы строк по краям ("  Иван  " -> "Иван")
        cleaned_line = line.strip()

        # Проверяем: если строка после очистки не пустая, добавляем ее
        if cleaned_line:
          unique_lines.add(cleaned_line)

    # 2. Открываем новый файл для записи ("w" — write) результатов
    with open(output_filename, "w", encoding="utf-8") as file:
      # sorted() отсортирует строки по алфавиту перед записью
      for line in sorted(unique_lines):
        file.write(line + "\n")

    print("Успешно! Файл очищен.")
    print(f"Уникальных строк после очистки: {len(unique_lines)}")
    print(f"Результат сохранен в файл: {output_filename}")

  except FileNotFoundError:
    print(f"Ошибка: Файл {input_filename} не найден. Проверьте название!")


# Запуск функции
clean_data_file("input.txt", "output.txt")