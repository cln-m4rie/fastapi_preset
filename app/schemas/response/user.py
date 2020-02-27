from ..db.user import UserSchema
from .base import Base


class UserResponse(Base):
    def __init__(self, user: UserSchema):
        self.user = user

    def serialize(self) -> dict:
        return {
            "id": self.user.id,
            "username": self.user.username,
            "email": self.user.email,
            "created_at": self.user.created_at,
            "updated_at": self.user.updated_at,
        }
