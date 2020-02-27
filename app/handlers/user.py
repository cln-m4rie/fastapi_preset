from sqlalchemy.orm import Session

from ..adapter.database.user import create
from ..helpers.auth_helper import make_passwd_hash
from ..schemas.db.user import UserCreateSchema, UserSchema


def create_user(user_schema: UserCreateSchema, db: Session) -> UserSchema:
    user = create(
        db,
        user_schema.username,
        user_schema.email,
        make_passwd_hash(user_schema.password),
    )
    return user
