import sqlalchemy
from pprint import pprint
db = 'postgresql://postgres:password@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()


# 1 Название и год выхода альбомов,вышедших в 2018 году
select_1 = connection.execute("SELECT name,year FROM album "
                        "WHERE year=2018;").fetchall()
pprint(select_1)

# 2 Название и продолжительность самого длительного трека
select_2 = connection.execute("SELECT name,duration FROM track "
                        "WHERE duration=(SELECT MAX(duration) FROM track);").fetchall()
pprint(select_2)

# 3 Название треков, продолжительность которых не менее 3,5 минуты
select_3 = connection.execute("SELECT name,duration FROM track "
                        "WHERE duration >= 3.5;").fetchall()
pprint(select_3)

#4 Названия сборников, вышедших в период с 2018 по 2020 год включительно
select_4 = connection.execute("SELECT collection-name,year FROM collection "
                        "WHERE release-year BETWEEN 2018 AND 2020;").fetchall()
pprint(select_4)

# 5 Исполнители, чье имя состоит из 1 слова
select_5 = connection.execute("SELECT name FROM band "
                        "WHERE band NOT LIKE '%% %%' ;").fetchall()
pprint(select_5)


# 6 Название треков, которые содержат слово "мой"/"my"
select_6 = connection.execute("SELECT name FROM track "
                              "WHERE name LIKE '%%мой%%';").fetchall()
pprint(select_6)















