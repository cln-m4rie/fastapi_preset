from typing import Optional

from sqlalchemy.orm import Session

from ...models.user import User


def find_by_email(db_session: Session, email: str) -> Optional[User]:
    return (
        db_session.query(User)
        .filter(User.email == email, User.deleted_at == None)
        .first()
    )


def create(
    db_session: Session, username: str, email: str, hashed_password: str
) -> User:
    user = User(username=username, email=email, password=hashed_password)
    db_session.add(user)
    db_session.commit()
    return user
