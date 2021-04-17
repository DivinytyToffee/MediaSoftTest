import uuid

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .database import Base


class City(Base):
    __tablename__ = 'city'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)

    streets = relationship("Street", back_populates="streets")
    shops = relationship("Shop", back_populates="shops")


class Street(Base):
    __tablename__ = 'street'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    city = Column(UUID(as_uuid=True), ForeignKey('city.id'))

    streets = relationship("City", back_populates="my_city")
    shops = relationship("Shop", back_populates="shops")


class Shop(Base):
    __tablename__ = 'shop'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    city = Column(UUID(as_uuid=True), ForeignKey('city.id', ondelete='CASCADE'))
    street = Column(UUID(as_uuid=True), ForeignKey('street.id', ondelete='CASCADE'))

    streets = relationship("Street", back_populates="streets")
    cities = relationship("City", back_populates="cities")

