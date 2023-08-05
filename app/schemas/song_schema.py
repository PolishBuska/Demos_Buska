from typing import Annotated
from app.schemas import user_schema
from pydantic import BaseModel, constr, ConfigDict, UrlConstraints


class SongBase(BaseModel):
    title: Annotated[str, constr(max_length=100)]
    author: user_schema.UserOut
    model_config = ConfigDict(extra='ignore', from_attributes=True)

class Create_song(SongBase):
    file_url: UrlConstraints