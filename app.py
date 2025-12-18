import logic

DATA_FILE = "movies.json"


def main():
    movies = logic.load_movies(DATA_FILE)
    print("Добро пожаловать в Каталог Фильмов!")

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Показать все фильмы")
        print("2. Добавить фильм")
        print("3. Найти фильмы по году")
        print("4. Отметить фильм как просмотренный")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            if not movies:
                print("Список пуст.")
            else:
                for m in movies:
                    print(logic.format_movie(m))

        elif choice == "2":
            title = input("Введите название фильма: ")
            try:
                year = int(input("Введите год выпуска: "))
                logic.add_movie(movies, title, year)
                logic.save_movies(DATA_FILE, movies)
                print("Фильм добавлен!")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "3":
            try:
                year = int(input("Введите год для поиска: "))
                found = logic.find_by_year(movies, year)
                if found:
                    for m in found:
                        print(logic.format_movie(m))
                else:
                    print("Фильмов не найдено.")
            except ValueError as e:
                print(f"Ошибка: {e}")


        elif choice == "4":
            if not movies:
                print("Список пуст, отмечать нечего.")
            else:
                for m in movies:
                    print(logic.format_movie(m))
                try:
                    m_id = int(input("Введите ID фильма: "))
                    logic.mark_watched(movies, m_id)
                    logic.save_movies(DATA_FILE, movies)
                    print("Операция выполнена.")
                except ValueError as e:
                    print(f"Ошибка: {e}")
        elif choice == "0":
            logic.save_movies(DATA_FILE, movies)
            print("До свидания")
            break

        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()