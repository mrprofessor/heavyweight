from app import db


class BaseModel(db.Model):
    __abstract__ = True
    __bind_key__ = "heavyweight"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True), server_default=db.func.now(), onupdate=db.func.now()
    )

    @classmethod
    def create(cls, data=None, close=False):
        obj = cls()
        try:
            if data:
                for k, v in data.items():
                    setattr(obj, k, v)
            db.session.add(obj)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
        finally:
            if close:
                db.session.close()
        return obj

    @classmethod
    def bulk_insert(cls, data):
        try:
            db.session.bulk_insert_mappings(cls, data, render_nulls=False)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
        finally:
            db.session.close()

    @classmethod
    def read(cls, pk=None):
        """ Get all the records if primary key is not provided """
        if pk:
            return db.session.query(cls).filter_by(id=pk).first()
        return db.session.query(cls).all()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
        finally:
            db.session.close()

    def update(self, data, close=True):
        try:
            for k, v in data.items():
                setattr(self, k, v)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
        finally:
            if close:
                db.session.close()

    @classmethod
    def filter_by_key(cls, key: str, value):
        """ Returns multiple matches """
        return cls.query.filter(getattr(cls, key) == value).all()

    @classmethod
    def find_by_key(cls, key: str, value):
        """ Returns single match """
        return cls.query.filter(getattr(cls, key) == value).first()

    @property
    def class_name(self):
        """Shortcut for returning class name."""
        return self.__class__.__name__

    def __repr__(self):
        return f"{self.class_name}.{self.id}"
