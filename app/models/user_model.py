from sqlalchemy import ForeignKey, func, TIMESTAMP, Column
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base
from app.schemas.song_schema import SongBase
from app.schemas.user_schema import UserOut


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    nickname: Mapped[str]
    password: Mapped[str]
    role_id: Mapped[int]
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=func.now())
    def to_read_model(self) -> UserOut:
        return UserOut(
            nickname = self.nickname,
            id=self.id,
            password = self.password,
            email=self.email,
            role_id=self.role_id,
        )