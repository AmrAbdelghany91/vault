from sqlalchemy import Column, Integer, String

from .base import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    active = Column(Integer)

    def __repr__(self):
        return "<Category(id='%d', name='%s', active='%d')>" % (
            self.id, self.name, self.active)
