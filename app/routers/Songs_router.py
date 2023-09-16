from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette import status
from app.schemas.user_schema import UserOut, User
from app.services import File_service
from app.services.User_auth_service import CurrentUserGet
from ..repositories.Db_model_definer import UsersRepository

router = APIRouter(
    prefix='/songs',
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


@router.post('/me/song/create')
async def create_song(title: str, desc: str, file: UploadFile = File(...),
                      current_user: User = Depends(CurrentUserGet.auth.get_current_user)):
    song_manager_service = File_service.FileService(file = file,
                                                    title = title,
                                                    path="app/static/",
                                                    desc=desc,
                                                    author_id= current_user.id)
    result = await song_manager_service.Upload_song()
    return result


# This section is responsible for not protected operations
@router.get('/song/get/{id}')
async def get_song_by_id(id: int,):
    raise NotImplementedError


@router.get('/song/get/all')
async def get_songs(limit: str,offset: str):
    raise NotImplementedError

# Implement this behavior


@router.delete('/me/song/delete/{id}')
async def delete_song_by_id(id: int,
                      current_user: User = Depends(CurrentUserGet.auth.get_current_user)):
    raise NotImplementedError


@router.put('/me/song/update/{id}')
async def update_song_by_id(id: int, song: str,
                      current_user: User = Depends(CurrentUserGet.auth.get_current_user)):
    raise NotImplementedError

