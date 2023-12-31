import datetime

from sqlalchemy import ForeignKey, MetaData, Column, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base
from app.schemas.song_schema import SongBase

class Songs(Base):
    __tablename__ = "songs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[int]
    author_id: Mapped[int] = mapped_column( ForeignKey("users.id", ondelete="CASCADE"),
                      nullable=False)
    author = relationship("User", backref="Songs")
    description: Mapped[str]
    link: Mapped[str]
    filename: Mapped[str]
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=func.now())

    def to_read_model(self) -> SongBase:
        return SongBase(
            id=self.id,
            title=self.title,
            author_id=self.author_id,
            description=self.description,
        )