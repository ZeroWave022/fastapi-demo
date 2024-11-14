import csv
from models import Track, TrackMood


def read_dataset() -> list[Track]:
    with open("./data/spotify_most_streamed_songs.csv", encoding="utf-8") as f:
        raw_data = [line for line in csv.reader(f)]
    data = []

    for row in raw_data[1:]:
        row_data = Track(
            name=row[0],
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


def write_track(track: Track) -> None:
    with open("./data/spotify_most_streamed_songs.csv", "a", encoding="utf-8") as f:
        # Create a new row in the following format:
        # track_name,artist_name,artist_count,release_year,release_month,release_day,
        # in_playlists,in_charts,streams,,,,,,bpm,,,danceability,valence,energy,acousticness,instrumentalness,liveness,speechiness,cover_url
        splitted_date = track.release_date.split("-")

        new_row: list[str | None] = [
            track.name,
            track.artist_name,
            str(track.artist_count),
            *splitted_date,
            str(track.in_playlists),
            str(track.in_charts),
            str(track.streams),
        ]

        new_row.extend([None] * 5)
        new_row.append(str(track.bpm))
        new_row.extend([None] * 2)
        new_row.extend([str(val) for val in track.mood.model_dump().values()])
        new_row.append(track.cover_url)

        csv.writer(f).writerow(new_row)
