from app import db
from datetime import datetime

class WorkloadScore(db.Model):
    __tablename__ = 'workload_scores'
    
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), unique=True, nullable=False)
    score = db.Column(db.Float, nullable=False, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f'<WorkloadScore {self.item_name}: {self.score}>'

class WorkloadRecord(db.Model):
    __tablename__ = 'workload_records'
    
    id = db.Column(db.Integer, primary_key=True)
    report_date = db.Column(db.Date, nullable=False)
    doctor_name = db.Column(db.String(50), nullable=False) # Store name for flexibility with imports
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=True) # Optional link
    item_name = db.Column(db.String(100), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.now)
    
    # Relationship to Doctor (optional)
    doctor = db.relationship('Doctor', backref=db.backref('workload_records', lazy=True))

    def __repr__(self):
        return f'<WorkloadRecord {self.report_date} - {self.doctor_name} - {self.item_name}>'
