def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

            if not lines:
                return (0, 0)

            total = 0
            count = 0

            for line in lines:
                line = line.strip()
                if not line:
                    continue
                _, salary = line.split(",")
                total += int(salary)
                count += 1

            if count == 0:
                return (0, 0)

            average = total / count
            return (total, average)

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return None
    

if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    if total is not None:
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
