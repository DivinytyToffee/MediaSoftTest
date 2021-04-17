import uuid

from sqlalchemy import create_engine
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:31415@localhost/testMediaSoft')
base = declarative_base()


class City(base):
    __tablename__ = 'city'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    # streets = relationship("Street")


class Street(base):
    __tablename__ = 'street'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    city = Column(UUID(as_uuid=True), ForeignKey('city.id'))


class Shop(base):
    __tablename__ = 'shop'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    city = Column(UUID(as_uuid=True), ForeignKey('city.id', ondelete='CASCADE'))
    street = Column(UUID(as_uuid=True), ForeignKey('street.id', ondelete='CASCADE'))


Session = sessionmaker(engine)
session = Session()

base.metadata.create_all(engine)

# session.add_all([City(name='N'), City(name='M'), City(name='X')])
# session.commit()

city = session.query(City).filter_by(name='N').first()
print(city.name)