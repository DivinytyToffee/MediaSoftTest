import uuid

from sqlalchemy.orm import Session

from db.database import SessionLocal
from db import models, schemas


def get_cities(db: Session):
    return db.query(models.City).all()


def get_city_streets(db: Session, city_id: uuid.UUID):
    return db.query(models.Street).filter(models.Street.my_city.has(id=city_id))


if __name__ == '__main__':
    db = SessionLocal()
    cities = get_cities(db)

    for city in cities:
        print(f'City {city.name}')
        for street in get_city_streets(db, city.id):
            print(' '*4 + f'{street.name}')

