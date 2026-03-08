def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats = []

            for line in file:
                line = line.strip()
                if not line:
                    continue
                cat_id, name, age = line.split(",")
                cats.append({"id": cat_id, "name": name, "age": age})

            return cats

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return None


if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    if cats_info is not None:
        print(cats_info)
