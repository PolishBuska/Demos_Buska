from fastapi import APIRouter, UploadFile, File
import app.schemas.song_schema as song_schema
from app.services import File_service

router = APIRouter(
    prefix='/songs',
    tags=['songs']
)


@router.post('/song/create')
async def create_song(title: str,desc:str, file: UploadFile = File(...)):
    song_manager = File_service.FileService(file = file,
                                            title = title,
                                            path="app/static/",
                                            desc=desc,
                                            author_id= 1)
    result = await song_manager.Upload_song()
    return result
