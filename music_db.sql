CREATE TABLE track (
  id serial PRIMARY KEY,
  artist_instrument_id integer REFERENCES artist_instrument (id),
  song_id integer REFERENCES song (id),
  album_id integer REFERENCES album (id)
);

CREATE TABLE album (
  id serial PRIMARY KEY,
  name varchar,
  year integer,
  artist_id integer REFERENCES artist (id)
);

CREATe TABLE artist (
  id serial PRIMARY KEY,
  name varchar
);

CREATE TABLE instrument (
  id serial PRIMARY KEY,
  name varchar
);

CREATE TABLE artist_instrument (
  id serial PRIMARY KEY,
  artist_id integer REFERENCES artist (id),
  instrument_id integer REFERENCES instrument (id)
);

CREATE TABLE song (
  id serial PRIMARY KEY,
  name varchar,
  songwriter_id integer REFERENCES songwriter (id)
);

CREATE TABLE songwriter (
  id serial PRIMARY KEY,
  name varchar
);

INSERT INTO "album"("id","name","year","artist_id")
VALUES
(1,E'Light Grenades',2005,1),
(2,E'1000 Forms of Fear',2014,2),
(3,E'I am... Sasha Fierce',2008,3),
(4,E'To Pimp a Butterfly',2013,4),
(5,E'Make Yourself',1999,1),
(6,E'Merry Christmas',1994,5),
(7,E'Christmas',2011,6);

INSERT INTO "artist"("id","name")
VALUES
(1,E'Incubus'),
(2,E'Sia'),
(3,E'Beyonce'),
(4,E'Kendrick'),
(5,E'Mariah'),
(6,E'Michael Buble');

INSERT INTO "artist_instrument"("id","artist_id","instrument_id")
VALUES
(1,1,1),
(2,2,2),
(3,3,2),
(4,4,3),
(5,5,2),
(6,6,2),
(7,6,4),
(8,5,4);

INSERT INTO "instrument"("id","name")
VALUES
(1,E'Guitar'),
(2,E'Microphone'),
(3,E'Drums'),
(4,E'Keyboards'),
(5,E'Bass');

INSERT INTO "song"("id","name","songwriter_id")
VALUES
(1,E'Dig',1),
(2,E'Chandelier',2),
(3,E'Halo',4),
(4,E'Alright',3),
(5,E'Anna Molly',1),
(6,E'Elastic Heart',2),
(7,E'Pardon Me',1),
(8,E'King Kunta',3),
(9,E'All I Want For Christmas',5),
(10,E'Freedom',3);

INSERT INTO "songwriter"("id","name")
VALUES
(1,E'Incubus'),
(2,E'Sia'),
(3,E'Max Martin'),
(4,E'Ryan Tedder'),
(5,E'Vince Vance');

INSERT INTO "track"("id","artist_instrument_id","song_id","album_id","duration")
VALUES
(1,1,1,1,E'03:20:00'),
(2,1,5,1,E'04:20:00'),
(3,2,6,2,E'05:19:00'),
(4,1,7,5,E'03:44:00'),
(5,4,8,4,E'04:12:00'),
(6,4,4,4,E'06:18:00'),
(7,3,3,3,E'03:38:00'),
(8,5,9,6,E'04:01:00'),
(9,6,9,7,E'02:53:00'),
(10,3,10,NULL,E'04:14:00');

`pg_dump music_db -Fc -f music_db.dump`
