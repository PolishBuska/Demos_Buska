from typing import Annotated

from pydantic import BaseModel, constr, ConfigDict
from annotated_types import Gt, Ge, Le

class UserBase(BaseModel):
    title: Annotated[str, constr(max_length=100)]
    author: Annotated[str, constr(max_length=100)]
    role_id: Annotated[int, Gt(0),Le(2)]
    model_config = ConfigDict(extra='ignore', from_attributes=True)

class UserCreate(UserBase):
    password: Annotated[str, constr(min_length=5,max_length=10)]
    model_config = ConfigDict(extra='ignore', from_attributes=True)

class UserOut(UserBase):
    user: UserBase
    model_config = ConfigDict(extra='ignore', from_attributes=True)