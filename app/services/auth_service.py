from typing import NoReturn, Union

from sqlalchemy.orm import Session

from ..adapter.database import user as user_adapter
from ..exceptions.http import credentials_exception
from ..helpers import auth_helper
from ..schemas.db.user import UserSchema


def get_authenticated_user(
    db_session: Session, token: str
) -> Union[UserSchema, NoReturn]:
    token_data = auth_helper.get_token_data(token)
    user = user_adapter.find_by_email(db_session, token_data.email)
    if user is None:
        raise credentials_exception

    return user
