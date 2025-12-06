from app import db
from datetime import datetime

class Schedule(db.Model):
    __tablename__ = 'schedules'

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    date = db.Column(db.Date, nullable=False, index=True)
    shift_type = db.Column(db.String(20)) # 排班类型：早、中、夜、休、值...
    
    # 关联
    doctor = db.relationship('Doctor', backref=db.backref('schedules', lazy='dynamic'))

    def __repr__(self):
        return f'<Schedule {self.doctor.name} {self.date} {self.shift_type}>'
