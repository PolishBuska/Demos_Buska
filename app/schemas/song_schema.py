from typing import Annotated
from app.schemas import user_schema
from pydantic import BaseModel, constr, ConfigDict, UrlConstraints


class SongBase(BaseModel):
    title: Annotated[str, constr(max_length=100)]
    description: Annotated[str,constr(max_length=25)]
    model_config = ConfigDict(extra='allow', from_attributes=True)

class Create_song(SongBase):
    file_url: UrlConstraints