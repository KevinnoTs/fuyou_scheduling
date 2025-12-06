# -*- coding: utf-8 -*-
import sys
import os
# Add project root to sys.path for direct execution
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.models.doctors import Doctor
from app import db, create_app
from datetime import datetime

def seed_doctors():
    doctor = Doctor(name='李文娟', gender='女', title='医师', specialty='妇科,产科,儿科', status='active', annual_leave_days=10, used_annual_leave_days=10, display_order=30, avatar_path='uploads/avatars/1765030898_jpg', resignation_date=datetime.strptime('2099-12-31', '%Y-%m-%d').date(), id=1)
    if not Doctor.query.get(1):
        db.session.add(doctor)
    doctor = Doctor(name='冉佩入', gender='女', title='医师', specialty='妇科,产科,儿科', status='active', annual_leave_days=15, used_annual_leave_days=15, display_order=10, avatar_path='uploads/avatars/1765030921_jpg', resignation_date=datetime.strptime('2099-12-31', '%Y-%m-%d').date(), id=2)
    if not Doctor.query.get(2):
        db.session.add(doctor)
    doctor = Doctor(name='李世珍', gender='女', title='医师', specialty='妇科,产科,儿科,筛查', status='active', annual_leave_days=10, used_annual_leave_days=10, display_order=20, avatar_path='uploads/avatars/1765030942_jpg', resignation_date=datetime.strptime('2099-12-31', '%Y-%m-%d').date(), id=3)
    if not Doctor.query.get(3):
        db.session.add(doctor)
    doctor = Doctor(name='吴春梅', gender='女', title='医师', specialty='妇科,产科,儿科', status='active', annual_leave_days=15, used_annual_leave_days=15, display_order=40, resignation_date=datetime.strptime('2099-12-31', '%Y-%m-%d').date(), id=4)
    if not Doctor.query.get(4):
        db.session.add(doctor)
    doctor = Doctor(name='曾慧尹', gender='女', title='医师', specialty='妇科,产科,儿科,筛查', status='active', annual_leave_days=10, used_annual_leave_days=5, display_order=50, avatar_path='uploads/avatars/1765031025_jpg', resignation_date=datetime.strptime('2099-12-31', '%Y-%m-%d').date(), id=5)
    if not Doctor.query.get(5):
        db.session.add(doctor)
    doctor = Doctor(name='汪金美', gender='女', title='医师', specialty='妇科,产科,儿科', status='active', annual_leave_days=5, used_annual_leave_days=5, display_order=60, avatar_path='uploads/avatars/1765031049_jpg', resignation_date=datetime.strptime('2099-12-31', '%Y-%m-%d').date(), id=6)
    if not Doctor.query.get(6):
        db.session.add(doctor)
    doctor = Doctor(name='孙楠', gender='男', title='医师', specialty='妇科,产科,筛查', status='resigned', annual_leave_days=0, used_annual_leave_days=0, display_order=70, resignation_date=datetime.strptime('2025-10-01', '%Y-%m-%d').date(), id=7)
    if not Doctor.query.get(7):
        db.session.add(doctor)
    doctor = Doctor(name='赵燕', gender='女', title='医助', specialty='', status='active', annual_leave_days=0, used_annual_leave_days=0, display_order=110, resignation_date=datetime.strptime('2099-12-31', '%Y-%m-%d').date(), id=8)
    if not Doctor.query.get(8):
        db.session.add(doctor)
    doctor = Doctor(name='郝欣雨', gender='女', title='医助', specialty='', status='active', annual_leave_days=0, used_annual_leave_days=0, display_order=120, resignation_date=datetime.strptime('2099-12-31', '%Y-%m-%d').date(), id=9)
    if not Doctor.query.get(9):
        db.session.add(doctor)
    doctor = Doctor(name='	王韵迪', gender='女', title='医助', specialty='', status='active', annual_leave_days=0, used_annual_leave_days=0, display_order=130, resignation_date=datetime.strptime('2099-12-31', '%Y-%m-%d').date(), id=10)
    if not Doctor.query.get(10):
        db.session.add(doctor)
    doctor = Doctor(name='杨安霞', gender='女', title='医助', specialty='', status='active', annual_leave_days=0, used_annual_leave_days=0, display_order=140, resignation_date=datetime.strptime('2099-12-31', '%Y-%m-%d').date(), id=11)
    if not Doctor.query.get(11):
        db.session.add(doctor)
    doctor = Doctor(name='董美林', gender='女', title='医助', specialty='', status='active', annual_leave_days=0, used_annual_leave_days=0, display_order=150, resignation_date=datetime.strptime('2099-12-31', '%Y-%m-%d').date(), id=12)
    if not Doctor.query.get(12):
        db.session.add(doctor)
    doctor = Doctor(name='罗光红', gender='女', title='医助', specialty='', status='active', annual_leave_days=0, used_annual_leave_days=0, display_order=160, resignation_date=datetime.strptime('2099-12-31', '%Y-%m-%d').date(), id=13)
    if not Doctor.query.get(13):
        db.session.add(doctor)
    doctor = Doctor(name='戴玲', gender='女', title='医助', specialty='', status='active', annual_leave_days=0, used_annual_leave_days=0, display_order=170, resignation_date=datetime.strptime('2099-12-31', '%Y-%m-%d').date(), id=14)
    if not Doctor.query.get(14):
        db.session.add(doctor)
    db.session.commit()
    print('seed_doctors 完成。')

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        seed_doctors()