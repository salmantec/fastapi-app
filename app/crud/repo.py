from sqlalchemy.orm import Session

from .. import models, schemas


def get_user_by_email(db: Session, email: str) -> schemas.User | None:
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate) -> schemas.User:
    fake_hashed_password = user.password + "notreallyhashed"
    user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
