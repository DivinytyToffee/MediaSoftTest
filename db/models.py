import uuid

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Time
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .database import Base


class City(Base):
    __tablename__ = 'city'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)

    streets = relationship("Street", back_populates="my_city")
    shops = relationship("Shop", back_populates="cities")


class Street(Base):
    __tablename__ = 'street'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    city = Column(UUID(as_uuid=True), ForeignKey('city.id'), nullable=False)

    my_city = relationship("City", back_populates="streets")
    shops = relationship("Shop", back_populates="streets")


class Shop(Base):
    __tablename__ = 'shop'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    city = Column(UUID(as_uuid=True), ForeignKey('city.id', ondelete='CASCADE'), nullable=False)
    street = Column(UUID(as_uuid=True), ForeignKey('street.id', ondelete='CASCADE'), nullable=False)
    open_time = Column(Time)
    close_time = Column(Time)

    streets = relationship("Street", back_populates="shops")
    cities = relationship("City", back_populates="shops")
