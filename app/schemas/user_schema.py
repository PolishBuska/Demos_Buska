from typing import Annotated

import bleach as bleach
from pydantic import BaseModel, constr, ConfigDict, EmailStr
from annotated_types import Gt, Ge, Le

class UserBase(BaseModel):
    title: Annotated[str, constr(max_length=100)]
    author: Annotated[str, constr(max_length=100)]
    role_id: Annotated[int, Gt(0),Le(2)]
    model_config = ConfigDict(extra='ignore', from_attributes=True)

class UserCreate(BaseModel):
    nickname: Annotated[str, constr(max_length=100)]
    email: EmailStr
    password: Annotated[str, constr(max_length=100)]
    user_role_id: Annotated[int, Ge(1), Le(2)]

    def clean(self):
        self.nickname = bleach.clean(self.nickname)
        self.email = bleach.clean(self.email)
        self.password = bleach.clean(self.password)
class UserOut(UserBase):
    user: UserBase
    model_config = ConfigDict(extra='ignore', from_attributes=True)