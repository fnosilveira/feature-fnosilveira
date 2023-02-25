from sqlalchemy.orm import Session

from models import Filme

class FilmesRepository:
    @staticmethod
    def get_all(db: Session):
        return db.query(Filme).all()
    
    @staticmethod
    def find_by_id(db: Session, id: int):
        return db.query(Filme).filter(Filme.id == id).first()
    
    @staticmethod
    def create(db: Session, filme: Filme):
        db.add(filme)
        db.commit()
        db.refresh(filme)
        return filme
    
    @staticmethod
    def update(db: Session, filme: Filme):
        if filme.id:
            db.merge(filme)
        else:
            db.add(filme)
        db.commit()
        return filme
    
    @staticmethod
    def delete(db: Session, id: int):
        db.query(Filme).filter(Filme.id == id).delete()
        db.commit()
        return True
    
    @staticmethod
    def delete_all(db: Session):
        db.query(Filme).delete()
        db.commit()
        return True
    
    
