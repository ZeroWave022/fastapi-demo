from pydantic import BaseModel


class TrackMood(BaseModel):
    danceability: int
    valence: int
    energy: int
    acousticness: int
    instrumentalness: int
    liveness: int
    speechiness: int


class Track(BaseModel):
    track_name: str
    artist_name: str
    artist_count: int
    release_date: str
    in_playlists: int
    in_charts: int
    streams: int
    bpm: int
    cover_url: str
    mood: TrackMood
