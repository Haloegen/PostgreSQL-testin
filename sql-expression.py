from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# Executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)


# Query 1 - Create variable for "Artist" table.
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)


# Query 2 - Create a variable for "Album" tabler
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)


# Query 3 - Create a variable for "Track" table.
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)


# making the connection
with db.connect() as connection:
    # Question 1 - Select all records from the "Artist" table
    # select_query = artist_table.select()

    # Question 2 - Select only the "Name" column form the "Artist" table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Question 3 - Select only 'Queen' from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Question 4 - Select only by the "ArtistId" # 51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Question 5 - Select only the albums with the "ArtistId #51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Question 6 - Select only the "Tracks" with the "Composer" of "Queen"
    # select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)