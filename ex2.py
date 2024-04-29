def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats_list = []
            for line in file:
                parts = line.strip().split(',')
                cat_dict = {
                    "id": parts[0],
                    "name": parts[1],
                    "age": parts[2]
                }
                cats_list.append(cat_dict)
            return cats_list
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

# cats_info = get_cats_info("path/to/cats_file.txt")
# print(cats_info)