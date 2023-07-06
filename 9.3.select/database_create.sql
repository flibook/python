create table if not exists band (
	id-band serial primary key,
	name varchar(30) not null unique 
);
create table if not exists album (
	id-album serial  primary key,
	name varchar(30) not null,
	year date not null
);

create table if not exists track (
	id-track serial primary key,
	name varchar(30) not null,
	duration numeric not null,
	id-album integer references album(id-album)
);

create table if not exists genre (
	id-genre serial primary key,
	name varchar(30) not null unique
);

create table if not exists collection (
	id-collection serial primary key,
	collection-name varchar(30) not null,
	year date not null
);

create table if not exists genre-of-band (
	id-genre serial primary key,
	id-genre integer references genre(id-genre),
	id-band  integer references band(id-band)
);

create table if not exists album-of-band (
	id-album-of-band serial primary key,
	id-band integer references band(id-band),
	id-album  integer references album(id-album)
	
);

create table if not exists collection-track (
	id-collection-track serial primary key,
	id-collection  integer references collection(id-collection),
	id-track integer references track(id-track)
);
