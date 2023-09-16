from typing import Annotated
from app.schemas import user_schema
from pydantic import BaseModel, constr, ConfigDict, UrlConstraints
from annotated_types import Gt, Ge, Le
class TokenData(BaseModel):
    id: int
    role_id: Annotated[int, Ge(1), Le(2)]
