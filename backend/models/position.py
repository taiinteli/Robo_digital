from models.init import Base
from sqlalchemy import Column, Integer

class Position(Base):
    __tablename__ = "position"
    id = Column(Integer, primary_key=True)
    x = Column(Integer)
    y = Column(Integer)
    z = Column(Integer)

    def __repr__(self) -> str:
      return f"Positions( id={self.id}, x={self.x}, y={self.y}, z={self.z} )"