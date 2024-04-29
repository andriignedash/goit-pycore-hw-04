def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            total_sum = 0
            count = 0
            for line in file:
                name, salary = line.strip().split(',')
                total_sum += int(salary)
                count += 1
            average_salary = round(total_sum / count)
            return (total_sum, average_salary)
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
        return None

# total, average = total_salary("path/to/salary_file.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
