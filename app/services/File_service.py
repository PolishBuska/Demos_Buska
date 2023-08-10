from app.models.song_model import Songs

from app.schemas.song_file_schema import FullDataFileSong

from app.repositories.File_repository import FileRepository
from app.repositories.Songs_repository import SongsRepository
class FileService():
    def __init__(self,file, path, title, desc, author_id):
        self.file = file
        self.path = path
        self.title = title
        self.desc = desc
        self.author_id = author_id
    async def Upload_song(self):
        file_manager = FileRepository(path=self.path, file=self.file)
        file_data = await file_manager.hash_filename()
        db_song_manager = SongsRepository
        song_data = {"title":self.title,"description":self.desc,"filename":file_data.file_name,"link":file_data.link}
        result = FullDataFileSong(**song_data)
        return await db_song_manager.add_one(data=result)

