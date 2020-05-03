from datetime import datetime, timedelta


Movies_Release = [
    ("Iron Man", 126),
    ("The Incredible Hulk", 112),
    ("Iron Man 2", 124),
    ("Thor", 115),
    ("Captain America: The First Avenger", 124),
    ("The Avengers", 143),
    ("Iron Man 3", 130),
    ("Thor: The Dark World", 112),
    ("Captain America: The Winter Soldier", 136),
    ("Guardians of the Galaxy", 121),
    ("Avengers: Age of Ultron", 141),
    ("Ant-Man", 117),
    ("Captain America: Civil War", 147),
    ("Doctor Strange", 115),
    ("Guardians of the Galaxy: Vol. 2", 136),
    ("Spider-Man: Homecoming", 133),
    ("Thor: Ragnarok", 130),
    ("Black Panther", 134),
    ("Avengers: Infinity War", 149),
    ("Ant-Man & the Wasp", 118),
    ("Captain Marvel", 123),
    ("Avengers: Endgame", 181),
    ("Spider-Man: Far From Home", 129),
]

Movies_Chronological = [
    ("Captain America: The First Avenger", 124),
    ("Captain Marvel", 123),
    ("Iron Man", 126),
    ("The Incredible Hulk", 112),
    ("Iron Man 2", 124),
    ("Thor", 115),
    ("The Avengers", 143),
    ("Iron Man 3", 130),
    ("Thor: The Dark World", 112),
    ("Captain America: The Winter Soldier", 136),
    ("Guardians of the Galaxy", 121),
    ("Guardians of the Galaxy: Vol. 2", 136),
    ("Avengers: Age of Ultron", 141),
    ("Ant-Man", 117),
    ("Captain America: Civil War", 147),
    ("Black Panther", 134),
    ("Spider-Man: Homecoming", 133),
    ("Doctor Strange", 115),
    ("Thor: Ragnarok", 130),
    ("Avengers: Infinity War", 149),
    ("Ant-Man & the Wasp", 118),
    ("Avengers: Endgame", 181),
    ("Spider-Man: Far From Home", 129),
]


def get_total_time_pregnancy(start: datetime, end: datetime) -> int:
    diff = end - start
    return diff.days

def get_total_time_movies(movies: list) -> int:
    total = 0
    for movie in movies:
        total += movie[1]
    return total

def get_baby_percentage(start: datetime, end: datetime, current: datetime) -> float:
    total_days = get_total_time_pregnancy(start, end)
    current_days = get_total_time_pregnancy(start, current)
    return current_days/total_days

def get_current_movie(movies: list, percentage: float) -> str:
    total_time = get_total_time_movies(movies)
    current_time = 0
    for movie in movies:
        current_time += movie[1]
        cur_percentage = current_time/total_time
        # print(f"DEBUG: {movie[0]} is {cur_percentage:.2f} of the MCU")
        if cur_percentage > percentage:
            return movie[0]
    raise Exception

def report_date_ranges(start: datetime, end: datetime, movies: list) -> None:
    total_days = get_total_time_pregnancy(start, end)
    total_time = get_total_time_movies(movies)
    dates = []
    subtotal_days = 0
    subtotal_time = 0
    for movie in movies:
        movie_start = start + timedelta(days=subtotal_days)
        subtotal_time += movie[1]
        subtotal_days = int(total_days * (subtotal_time / total_time))
        movie_end = start + timedelta(days=subtotal_days)
        print(f"\t\"{movie[0]}\" airs between {movie_start.strftime('%Y-%m-%d')} and {movie_end.strftime('%Y-%m-%d')}")


def main():
    date_of_conception = datetime.strptime("20190927", '%Y%m%d')
    date_of_birth = datetime.strptime("20200621", '%Y%m%d')
    date_current = datetime.now()
    percent_loaded = get_baby_percentage(date_of_conception, date_of_birth, date_current)
    print(percent_loaded)
    current_movie_chron = get_current_movie(Movies_Chronological, percent_loaded)
    current_movie_rel = get_current_movie(Movies_Release, percent_loaded)
    print(f"In Chronological Order, your baby is {current_movie_chron}")
    report_date_ranges(date_of_conception, date_of_birth, Movies_Chronological)
    print(f"In Theatrical Release Order, your baby is {current_movie_rel}")
    report_date_ranges(date_of_conception, date_of_birth, Movies_Release)

if __name__ == "__main__":
    main()
