from typing import Annotated
from datetime import datetime
from fastapi import FastAPI, Path, Query

from data.spotify import read_dataset
from models import Track

tracks = read_dataset()

app = FastAPI()


@app.get("/")
def status():
    return {"status": "ok"}


@app.get("/tracks")
def fetch_tracks(from_id: int = 0, to_id: int | None = None):
    to_id = len(tracks) if to_id is None else to_id
    return tracks[from_id:to_id]


@app.get("/track/{track_id}")
def fetch_track(track_id: Annotated[int, Path(gt=0, lt=len(tracks))]) -> Track:
    return tracks[track_id]


@app.get("/top")
def fetch_top(
    year: Annotated[int | None, Query(gt=0, le=datetime.now().year)] = None,
    items: int = 10,
):
    if year:
        tracks_to_sort = [t for t in tracks if int(t.release_date[:4]) == year]
    else:
        tracks_to_sort = tracks

    sorted_tracks = sorted(tracks_to_sort, key=lambda t: t.streams, reverse=True)

    return sorted_tracks[:items]
