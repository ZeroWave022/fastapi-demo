import csv
from models import Track, TrackMood


def fetch_dataset() -> list[Track]:
    with open("./data/spotify_most_streamed_songs.csv") as f:
        raw_data = [line for line in csv.reader(f)]
    data = []

    for row in raw_data[1:]:
        row_data = Track(
            track_name=row[0],
            artist_name=row[1],
            artist_count=int(row[2]),
            release_date=f"{row[3]}-{row[4]}-{row[5]}",
            in_playlists=int(row[6]),
            in_charts=int(row[7]),
            streams=int(row[8]),
            bpm=int(row[14]),
            cover_url=row[24],
            mood=TrackMood(
                danceability=int(row[17]),
                valence=int(row[18]),
                energy=int(row[19]),
                acousticness=int(row[20]),
                instrumentalness=int(row[21]),
                liveness=int(row[22]),
                speechiness=int(row[23]),
            ),
        )

        data.append(row_data)
    return data
