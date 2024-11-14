from pydantic import BaseModel, Field


class TrackMood(BaseModel):
    danceability: int = Field(default=0, title="Danceability", ge=0, le=100)

    valence: int = Field(default=0, title="Valence", ge=0, le=100)

    energy: int = Field(default=0, title="Energy", ge=0, le=100)

    acousticness: int = Field(default=0, title="Acousticness", ge=0, le=100)

    instrumentalness: int = Field(
        default=0, title="Instrumentalness", ge=0, le=100)

    liveness: int = Field(default=0, title="Liveness", ge=0, le=100)

    speechiness: int = Field(default=0, title="Speechiness", ge=0, le=100)


class Track(BaseModel):
    name: str = Field(default="", title="Track Name")

    artist_name: str = Field(default="", title="The artist(s) name(s)")

    artist_count: int = Field(default=0, title="Number of artists")

    release_date: str = Field(default="0000-00-00", title="Release date")

    in_playlists: int = Field(default=0, title="Playlist count")

    in_charts: int = Field(default=0, title="Chart count")

    streams: int = Field(default=0, title="Streams")

    bpm: int = Field(default=0, title="BPM (beats per minute)")

    cover_url: str = Field(default="", title="Cover URL")

    mood: TrackMood = Field(default=TrackMood(), title="Track mood")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Believer",
                    "artist_name": "Imagine Dragons",
                    "artist_count": 1,
                    "release_date": "2017-1-31",
                    "in_playlists": 18986,
                    "in_charts": 23,
                    "streams": 2_594_040_133,
                    "bpm": 125,
                    "cover_url": "https://i.scdn.co/image/ab67616d0000b2735675e83f707f1d7271e5cf8a",
                    "mood": {
                        "danceability": 77,
                        "valence": 74,
                        "energy": 78,
                        "acousticness": 4,
                        "instrumentalness": 0,
                        "liveness": 23,
                        "speechiness": 11,
                    },
                }
            ]
        }
    }
