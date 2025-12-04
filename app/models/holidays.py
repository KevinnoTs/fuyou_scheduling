from app import db
from datetime import datetime

class Holiday(db.Model):
    __tablename__ = 'holidays'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True, nullable=False, index=True)
    name = db.Column(db.String(64), nullable=False)
    # type: 'holiday' (放假), 'workday' (补班/调休)
    type = db.Column(db.String(20), default='holiday') 
    # source: 'auto' (自动抓取), 'manual' (手动录入)
    source = db.Column(db.String(20), default='manual')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Holiday {self.date} {self.name}>'
