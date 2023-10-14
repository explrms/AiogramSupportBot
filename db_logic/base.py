from typing import Type

from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем объект базы данных SQLite
engine = create_engine('sqlite:///support.db')

# Создаем базовый класс для определения моделей
Base = declarative_base()

# Создаем сессию для взаимодействия с базой данных
Session = sessionmaker(bind=engine)


# Создаем таблицу SupportTickets
class SupportTickets(Base):
    __tablename__ = 'support_tickets'

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer)
    message_thread_id = Column(Integer)

    @classmethod
    def create_ticket(cls, tg_id: int, message_thread_id: int) -> None:
        session = Session()
        ticket = cls(tg_id=tg_id, message_thread_id=message_thread_id)
        session.add(ticket)
        session.commit()
        session.close()

    @classmethod
    def get_ticket_by_message_thread_id(cls, message_thread_id: int) -> Type['SupportTickets'] | None:
        session = Session()
        ticket = session.query(cls).filter_by(message_thread_id=message_thread_id).first()
        session.close()
        return ticket

    @classmethod
    def get_ticket_by_tg_id(cls, tg_id: int) -> Type['SupportTickets'] | None:
        session = Session()
        ticket = session.query(cls).filter_by(tg_id=tg_id).first()
        session.close()
        return ticket

    @classmethod
    def delete_ticket(cls, message_thread_id: int) -> None:
        session = Session()
        ticket = session.query(cls).filter_by(message_thread_id=message_thread_id).first()
        session.delete(ticket)
        session.commit()
        session.close()


# Создаем таблицу в базе данных, если она не существует
Base.metadata.create_all(engine)
