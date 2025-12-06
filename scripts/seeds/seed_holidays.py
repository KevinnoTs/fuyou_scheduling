# -*- coding: utf-8 -*-
import sys
import os
# Add project root to sys.path for direct execution
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.models.holidays import Holiday
from app import db, create_app
from datetime import datetime

def seed_holidays():
    holiday = Holiday(date=datetime.strptime('2025-01-01', '%Y-%m-%d').date(), name='元旦', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-01-01', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-01-28', '%Y-%m-%d').date(), name='春节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-01-28', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-01-29', '%Y-%m-%d').date(), name='春节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-01-29', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-01-30', '%Y-%m-%d').date(), name='春节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-01-30', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-01-31', '%Y-%m-%d').date(), name='春节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-01-31', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-02-01', '%Y-%m-%d').date(), name='春节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-02-01', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-02-02', '%Y-%m-%d').date(), name='春节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-02-02', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-02-03', '%Y-%m-%d').date(), name='春节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-02-03', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-02-04', '%Y-%m-%d').date(), name='春节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-02-04', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-01-26', '%Y-%m-%d').date(), name='春节调休', type='workday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-01-26', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-02-08', '%Y-%m-%d').date(), name='春节调休', type='workday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-02-08', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-04-04', '%Y-%m-%d').date(), name='清明节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-04-04', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-04-05', '%Y-%m-%d').date(), name='清明节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-04-05', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-04-06', '%Y-%m-%d').date(), name='清明节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-04-06', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-05-01', '%Y-%m-%d').date(), name='劳动节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-05-01', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-05-02', '%Y-%m-%d').date(), name='劳动节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-05-02', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-05-03', '%Y-%m-%d').date(), name='劳动节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-05-03', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-05-04', '%Y-%m-%d').date(), name='劳动节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-05-04', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-05-05', '%Y-%m-%d').date(), name='劳动节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-05-05', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-04-27', '%Y-%m-%d').date(), name='劳动节调休', type='workday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-04-27', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-05-31', '%Y-%m-%d').date(), name='端午节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-05-31', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-06-01', '%Y-%m-%d').date(), name='端午节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-06-01', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-06-02', '%Y-%m-%d').date(), name='端午节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-06-02', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-10-01', '%Y-%m-%d').date(), name='国庆节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-10-01', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-10-02', '%Y-%m-%d').date(), name='国庆节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-10-02', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-10-03', '%Y-%m-%d').date(), name='国庆节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-10-03', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-10-04', '%Y-%m-%d').date(), name='国庆节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-10-04', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-10-05', '%Y-%m-%d').date(), name='国庆节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-10-05', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-10-06', '%Y-%m-%d').date(), name='中秋节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-10-06', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-10-07', '%Y-%m-%d').date(), name='国庆节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-10-07', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-10-08', '%Y-%m-%d').date(), name='国庆节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-10-08', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-09-28', '%Y-%m-%d').date(), name='国庆节调休', type='workday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-09-28', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2025-10-11', '%Y-%m-%d').date(), name='国庆节调休', type='workday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2025-10-11', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-01-01', '%Y-%m-%d').date(), name='元旦', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-01-01', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-01-02', '%Y-%m-%d').date(), name='元旦', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-01-02', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-01-03', '%Y-%m-%d').date(), name='元旦', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-01-03', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-01-04', '%Y-%m-%d').date(), name='元旦调休', type='workday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-01-04', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-02-15', '%Y-%m-%d').date(), name='春节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-02-15', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-02-16', '%Y-%m-%d').date(), name='春节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-02-16', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-02-17', '%Y-%m-%d').date(), name='春节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-02-17', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-02-18', '%Y-%m-%d').date(), name='春节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-02-18', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-02-19', '%Y-%m-%d').date(), name='春节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-02-19', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-02-20', '%Y-%m-%d').date(), name='春节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-02-20', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-02-21', '%Y-%m-%d').date(), name='春节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-02-21', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-02-22', '%Y-%m-%d').date(), name='春节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-02-22', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-02-23', '%Y-%m-%d').date(), name='春节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-02-23', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-02-14', '%Y-%m-%d').date(), name='春节调休', type='workday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-02-14', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-02-28', '%Y-%m-%d').date(), name='春节调休', type='workday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-02-28', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-04-04', '%Y-%m-%d').date(), name='清明节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-04-04', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-04-05', '%Y-%m-%d').date(), name='清明节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-04-05', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-04-06', '%Y-%m-%d').date(), name='清明节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-04-06', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-05-01', '%Y-%m-%d').date(), name='劳动节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-05-01', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-05-02', '%Y-%m-%d').date(), name='劳动节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-05-02', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-05-03', '%Y-%m-%d').date(), name='劳动节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-05-03', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-05-04', '%Y-%m-%d').date(), name='劳动节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-05-04', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-05-05', '%Y-%m-%d').date(), name='劳动节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-05-05', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-05-09', '%Y-%m-%d').date(), name='劳动节调休', type='workday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-05-09', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-06-19', '%Y-%m-%d').date(), name='端午节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-06-19', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-06-20', '%Y-%m-%d').date(), name='端午节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-06-20', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-06-21', '%Y-%m-%d').date(), name='端午节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-06-21', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-09-25', '%Y-%m-%d').date(), name='中秋节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-09-25', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-09-26', '%Y-%m-%d').date(), name='中秋节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-09-26', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-09-27', '%Y-%m-%d').date(), name='中秋节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-09-27', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-10-01', '%Y-%m-%d').date(), name='国庆节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-10-01', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-10-02', '%Y-%m-%d').date(), name='国庆节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-10-02', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-10-03', '%Y-%m-%d').date(), name='国庆节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-10-03', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-10-04', '%Y-%m-%d').date(), name='国庆节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-10-04', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-10-05', '%Y-%m-%d').date(), name='国庆节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-10-05', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-10-06', '%Y-%m-%d').date(), name='国庆节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-10-06', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-10-07', '%Y-%m-%d').date(), name='国庆节', type='holiday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-10-07', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-09-20', '%Y-%m-%d').date(), name='国庆节调休', type='workday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-09-20', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    holiday = Holiday(date=datetime.strptime('2026-10-10', '%Y-%m-%d').date(), name='国庆节调休', type='workday', source='manual')
    if not Holiday.query.filter_by(date=datetime.strptime('2026-10-10', '%Y-%m-%d').date()).first():
        db.session.add(holiday)
    db.session.commit()
    print('seed_holidays 完成。')

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        seed_holidays()