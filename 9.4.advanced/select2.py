import sqlalchemy
from pprint import pprint
db = 'postgresql://postgres:password@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()


# 1 Количество исполнителей в каждом жанре
select_20 = connection.execute("""
    SELECT name_genre,COUNT(musician) FROM musicians
    JOIN genre-of-band ON band.id-band = genre-of-band.id-band                      
    JOIN genre ON genre-of-band.id-genre = id-genre                           
    GROUP BY name;
    """).fetchall()
pprint(select_20)


# 2 количество треков, вошедших в альбомы 2019-2020 годов
select_21 = connection.execute("""
    SELECT year,COUNT(name) FROM album a
    JOIN track t ON a.id-album = t.id-album
    WHERE a.year  >= 2019 AND a.year <= 2020
    GROUP BY year;
    """).fetchall()
pprint(select_21)


#3  средняя продолжительность треков по каждому альбому;
select_22 = connection.execute("""
    SELECT name,AVG(duration) FROM album a
    JOIN track t  ON a.id-album = t.id-album
    GROUP BY name;
    """).fetchall()
pprint(select_22)


#4 все исполнители, которые не выпустили альбомы в 2020 году;
select_22 = connection.execute("""
    SELECT band,year FROM album a
    JOIN album-of-band ab  ON a.id-album = ab.id-album
    JOIN band b ON ab.id-band = b.id-band
    WHERE a.year != 2020;
    """).fetchall()
pprint(select_22)


#5 названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
select_23 = connection.execute("""
        SELECT collection-name FROM collection c
        JOIN collection-track ct  ON c.id-collection = ct.id-collection
        JOIN track t  ON ct.id-track = t.id-track
        JOIN album a  ON t.id-album = a.id-album
        JOIN album-of-band ab  ON a.id-album = ab.id-album
        JOIN band b  ON ab.id-band = b.id-band
        WHERE b.band LIKE 'band_2';
        """).fetchall()
pprint(select_23)


#6 название альбомов, в которых присутствуют исполнители более 1 жанра;
select_24 = connection.execute("""
        SELECT name FROM album a
        JOIN album-of-band ab ON a.id-album = ab.id-album
        JOIN band b ON ab.id-album = b.id-band
        JOIN genre-of-band gb ON b.id-band = gb.id-band
        GROUP BY b.name, a.name
        HAVING count(gb.id-genre) > 1;
        """).fetchall()
pprint(select_24)


#7 наименование треков, которые не входят в сборники;
select_25 = connection.execute("""
        SELECT name FROM track t
        LEFT JOIN collection-track ct ON t.id-track = ct.id-track
        WHERE ct.id-track IS NULL;
        """).fetchall()
pprint(select_25)


#8 исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
select_26 = connection.execute("""
        SELECT b.name, t.duration FROM band b
        JOIN album-of-band ab ON b.id-band = ab.id-band
        JOIN album a ON ab.id-album = a.id-album
        JOIN track t ON a.id-album = t.id-album
        WHERE t.duration IN (SELECT MIN(duration) FROM track)
        """).fetchall()
pprint(select_26)


#9 название альбомов, содержащих наименьшее количество треков.
select_27 = connection.execute('''
    SELECT a.name, COUNT(t.id-track) FROM album a
    JOIN track t ON a.id-album = t.id-album
    GROUP BY a.name
    HAVING count(t.id-track) in (
        SELECT COUNT (t.id-track)
        FROM album a
        JOIN track t  ON a.id-album = t.id-album
        GROUP BY a.name
        ORDER BY count(t.id-track)\
        LIMIT 1)
    ''').fetchall()
pprint(select_27)











