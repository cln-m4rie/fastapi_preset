from sqlalchemy import Column, DateTime, text
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
from sqlalchemy.sql.functions import current_timestamp  # SQLの関数`CURRENT_TIMESTAMP`を利用する場合import

from .base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(
        INTEGER(unsigned=True), primary_key=True, nullable=False, autoincrement=True
    )
    username = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(255), nullable=False, unique=True, index=True)
    password = Column(VARCHAR(255), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )
    deleted_at = Column(DateTime, nullable=True, default=None)

    # print時の出力
    def __repr__(self):
        return f"<User(id = {self.id}, username = {self.username})>"
