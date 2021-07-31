from typing import List

from sqlalchemy import Column, DateTime

from loader import database
import sqlalchemy


class BaseModel(database.Model):
    def __str__(self):
        model = self.__class__.__name__
        table: sqlalchemy.Table = sqlalchemy.inspect(self.__class__)
        primary_key_columns: List[sqlalchemy.Column] = table.primary_key.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


class TimedBaseModel(BaseModel):
    __abstract__ = True

    create_at = Column(DateTime(True), server_default=database.func.now())
    update_at = Column(DateTime(True), default=database.func.now(), onupdate=database.func.now(),
                       server_default=database.func.now())
