import secrets

from fastapi import UploadFile,HTTPException,status

from app.schemas.song_file_schema import SongFileSchema

from app.exceptions.File_exeception import FileException
class FileRepository():
    def __init__(self,file: UploadFile,path: str):
        self.file = file
        self.path = path
    async def hash_filename(self):
        try:
            file_name = self.file.filename
            extension = file_name.split(".")[1]
            if extension not in ["mp3"]:
                raise HTTPException(status.HTTP_403_FORBIDDEN,detail="Wrong format")
            else:
                token_name = secrets.token_hex(15) + "." + extension
                generated_name = self.path + token_name
                file_content = await self.file.read()
                async with open(generated_name, "wb") as file:
                    await file.write(file_content)
                return SongFileSchema(link= generated_name, file_name = file_name)
        except FileException:
            print("Invalid format")

