from fastapi import APIRouter
import app.schemas.song_schema as song_schema
from app.repositories.Songs_repository import SongsRepository

song = APIRouter(
    prefix='/songs',
    tags=['songs']
)


@song.get('/song/create')
async def create_song(song: song_schema.Create_song):
    song_dict = song.model_dump()
    song_id = await SongsRepository().add_one(song_dict)
    return song_id
