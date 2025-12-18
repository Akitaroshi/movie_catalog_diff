import json
from typing import List, TypedDict

class Movie(TypedDict):
    id: int
    title: str
    year: int
    watched: bool


def load_movies(path: str) -> List[Movie]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_movies(path: str, movies: List[Movie]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(movies, f, ensure_ascii=False, indent=4)


def check_movie_exists(movies: List[Movie], title: str, year: int) -> bool:
    return any(m["title"] == title and m["year"] == year for m in movies)


def add_movie(movies: List[Movie], title: str, year: int) -> List[Movie]:
    if year < 0:
        raise ValueError("Год не может быть отрицательным")

    if check_movie_exists(movies, title, year):
        raise ValueError("Такой фильм уже существует")

    new_id = max((m["id"] for m in movies), default=0) + 1

    new_movie: Movie = {
        "id": new_id,
        "title": title,
        "year": year,
        "watched": False
    }
    movies.append(new_movie)
    return movies


def mark_watched(movies: List[Movie], movie_id: int) -> List[Movie]:
    if movie_id < 0:
        raise ValueError("ID не может быть отрицательным")

    for movie in movies:
        if movie["id"] == movie_id:
            movie["watched"] = True
            return movies

    raise ValueError(f"Фильм с ID {movie_id} не найден.")


def find_by_year(movies: List[Movie], year: int) -> List[Movie]:
    if year < 0:
        raise ValueError("Год не может быть отрицательным")

    return [m for m in movies if m["year"] == year]


def format_movie(movie: Movie) -> str:
    status = "Просмотрен" if movie["watched"] else "Не просмотрен"
    return f"[{movie['id']}] {movie['title']} ({movie['year']}) - {status}"