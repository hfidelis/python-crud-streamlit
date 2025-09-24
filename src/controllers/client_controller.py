from sqlalchemy.orm import Session
from models.client import Client, ClientCreate, ITRole, ClientUpdate
from services.database import SessionLocal


class ClientController:
    def __init__(self):
        self.db: Session = SessionLocal()

    def get_client(self, client_id: int):
        return self.db.query(Client).filter(Client.id == client_id).first()

    def get_clients(self, skip: int = 0, limit: int = 100):
        return self.db.query(Client).offset(skip).limit(limit).all()

    def create_client(self, client: ClientCreate):
        try:
            db_client = Client(**client.dict())
            self.db.add(db_client)
            self.db.commit()
            self.db.refresh(db_client)
            return db_client
        except Exception as e:
            self.db.rollback()
            raise e

    def update_client(self, client_id: int, client: ClientUpdate):
        try:
            db_client = self.get_client(client_id)
            if db_client:
                update_data = client.dict(exclude_unset=True)
                for key, value in update_data.items():
                    setattr(db_client, key, value)
                self.db.commit()
                self.db.refresh(db_client)
            return db_client
        except Exception as e:
            self.db.rollback()
            raise e

    def delete_client(self, client_id: int):
        try:
            db_client = self.get_client(client_id)
            if db_client:
                self.db.delete(db_client)
                self.db.commit()
            return db_client
        except Exception as e:
            self.db.rollback()
            raise e

    def get_it_roles(self):
        return [role.value for role in ITRole]

    def __del__(self):
        self.db.close()
