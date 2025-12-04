from app import db
from datetime import date

class Doctor(db.Model):
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    gender = db.Column(db.String(10))
    title = db.Column(db.String(64)) # 职务
    status = db.Column(db.String(20), default='active') # active, resigned
    resignation_date = db.Column(db.Date, default=date(2099, 12, 31))
    specialty = db.Column(db.String(128)) # 擅长方向
    avatar_path = db.Column(db.String(256)) # 头像路径
    
    # 年假信息
    annual_leave_days = db.Column(db.Integer, default=0) # 每年年假总天数
    used_annual_leave_days = db.Column(db.Integer, default=0)
    display_order = db.Column(db.Integer, default=999) # 显示顺序，默认999

    # 反向引用 User (在 User 中定义)
    # user = db.relationship('User', back_populates='doctor', uselist=False)

    def __repr__(self):
        return f'<Doctor {self.name}>'
