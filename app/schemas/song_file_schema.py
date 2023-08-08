from typing import Annotated
from app.schemas import user_schema
from pydantic import BaseModel, constr, ConfigDict, UrlConstraints
from .song_schema import SongBase

class SongFileSchema(BaseModel):
    file_name: Annotated[str, constr(max_length=100)]
    link: Annotated[str,constr(max_length=25)]
    model_config = ConfigDict(extra='ignore', from_attributes=True)

class FullDataFileSong(SongBase):
    pass