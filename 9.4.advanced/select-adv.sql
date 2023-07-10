--Количество исполнителей в каждом жанре
select name, count(id_band) from genre
  join genre-of-band on genre.id-genre = genre-of-band.id-genre
  group by name

--Количество треков, вошедших в альбомы 2019-2020 годов
select count(album_name) from track
  join album on tracks.id-album = album.id-album
  where year >= '20190101' and year <= '20201231'

--Средняя продолжительность треков по каждому альбому
select name, avg(duration) from track
  join album on track.id-album = album.id-album
  group by name

--Все исполнители, которые не выпустили альбомы в 2020 году
select name from band 
  join album-of-band on band.id-band = album-of-band.id-band
  join album on album.id-album = album-of-band.id-album
  where year not between '20200101' and '20201231' 
  group by name

--Названия сборников, в которых присутствует конкретный исполнитель (выбрана Taylor Swift)
select collection-name from collection
  join collection-track on collection_track.id-collection = collection.id-collection
  join track on collection-tracks.id-track = tracks.id-track
  join album on tracks.id-album = album.id-album
  join album-of-band on album-of-band.id-album = album.id-album
  join band on album-of-band.id-band = band.id-band
  where artist_name = 'band_4'
  group by collection-name

--Название альбомов, в которых присутствуют исполнители более 1 жанра
select name, count(name) from album 
  join album-of-band on albums.id-album = album-of-band.id-album
  join band on album-of-band.id-band = band.id-band
  join genre-of-band on band.id-band= genre-of-band.id-band
  join genre on genre.id-genre = genre-of-band.id-genre 
  group by name 
  having count(name) > 1

--Наименование треков, которые не входят в сборники
select name from track
  left join collection-track on tracks.id-track = collection-track.id-track
  where id-collection is null 

--Исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)
select name, duration from track
  join album on tracks.id-album = album.id-album
  join album-of-band on album-of-band.id-album = albums.id-album
  join band on album-of-band.id-band = band.id-band 
  where duration = (select min(duration) from track)


select name, count(name) from tracks
  join albums on tracks.id-album = albums.id-album
  group by name

--Название альбомов, содержащих наименьшее количество треков
select distinct name from album
  left join track on tracks.id-album = album.id-album
  where track.id-album in (
    select id-album from track
    group by id-album
    having count(id-album) = (
         select count(id-track)
         from track
         group by id-album
         order by count
         limit 1
)
)

