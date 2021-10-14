# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"
# temp_table_drop = "drop table if exists temp"

# CREATE TABLES

songplay_table_create = "create table if not exists songplays (songplay_id varchar, start_time varchar, user_id varchar, level varchar, song_id varchar, artist_id varchar, session_id varchar, location varchar, user_agent varchar);"

user_table_create = "create table if not exists users (user_id varchar, first_name varchar, last_name varchar, gender varchar, level varchar);"

song_table_create = "create table if not exists songs (song_id varchar, title varchar, artist_id varchar, year int, duration float);"

artist_table_create = "create table if not exists artists (artist_id varchar, artist_name varchar, artist_location varchar, artist_latitude varchar, artist_longitude varchar);"

time_table_create = "create table if not exists time (start_time varchar, hour varchar, day varchar, week varchar, month varchar, year int, weekday varchar);"

# temp_table_create = "create table if not exists temp (session_id int, song varchar, artist varchar, duration float);"

# INSERT RECORDS

songplay_table_insert = "insert into songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) values (%s, %s, %s, %s, %s, %s, %s, %s, %s);"

user_table_insert = "insert into users (user_id, first_name, last_name, gender, level) \
                    values (%s, %s, %s, %s, %s);"

song_table_insert = "insert into songs (song_id, title, artist_id, year, duration) \
                    values (%s, %s, %s, %s, %s);"

artist_table_insert = "insert into artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude) \
                        values (%s, %s, %s, %s, %s);"

# temp_table_insert = "insert into temp (session_id, song, artist, duration) \
#                     values (%s, %s, %s, %s);"

time_table_insert = "insert into time (start_time, hour, day, week, month, year, weekday) \
                        values (%s, %s, %s, %s, %s, %s, %s);"

# FIND SONGS

# song_select = "select x.song_id, x.artist_id from temp left join (select song_id, songs.artist_id, title, artist_name, duration from songs join artists on songs.artist_id = artists.artist_id) as x on temp.song = x.title and temp.artist = x.artist_name and temp.duration = x.duration"

song_select = "select song_id, artists.artist_id from songs join artists on songs.artist_id = artists.artist_id where title = %s and artist_name = %s and duration = %s"

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]