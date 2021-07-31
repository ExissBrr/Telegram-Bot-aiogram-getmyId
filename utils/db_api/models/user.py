from sqlalchemy import Column, BigInteger, String
from sqlalchemy.sql.elements import or_

from utils.db_api.models.base import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = "Users"
    id: int = Column(BigInteger, primary_key=True)
    full_name: str = Column(String(200))


class DBCommands:
    @staticmethod
    async def add_user(**kwargs) -> User:
        """
        Добавление пользователя в таблицу
        """
        user = User(**kwargs)
        print("Adding")
        try:
            await user.create()
            return user
        except Exception as err:
            print(err)

    @staticmethod
    async def get_user(**kwargs) -> User:
        user = await User.query.where(make_filter(**kwargs)).gino.first()
        return user

    @staticmethod
    async def is_user(**kwargs) -> bool:
        return bool(await DBCommands.get_user(**kwargs))


def make_filter(
        id: int = None,
        full_name: str = None):
    """
    :param id:
    :param full_name:
    :return:
    """
    conditions = []
    if id is not None:
        conditions.append(User.id == int(id))
    if full_name is not None:
        conditions.append(User.full_name == full_name)
    return or_(*conditions)
