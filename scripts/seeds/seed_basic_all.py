# -*- coding: utf-8 -*-
import sys
import os
# Add project root to sys.path for direct execution
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.models.users import User
from app.models.doctors import Doctor
from app.models.holidays import Holiday
from app import db, create_app
from datetime import datetime

def seed_basic_all():
    print('导入医生数据中...')
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
    print('导入用户数据中...')
    user = User(username='kevinnots', real_name='超级管理员', role='super_admin', is_active_user=True, password_hash='scrypt:32768:8:1$dugRodgu5MTn9GBF$9c70dbb8c1755f1172aa8e32829c024b9fbe4e6001819166d38eeadb3a7b4bd76f55d9b7571776b997870266c8135e88c6177f5a98f90d9eaf87d95087bc790a')
    if not User.query.filter_by(username='kevinnots').first():
        db.session.add(user)
    user = User(username='liwenjuan', real_name='李文娟', role='admin', is_active_user=True, password_hash='scrypt:32768:8:1$NxWGik3r9x6yr6pl$29c0a830768d0074d7dc74d119702b8dcd8c6805050be38468d48f7fea724bb2ff47ba19dd358d9089a39f7d62b03d1a583402c5f7cddb42cf88ef641c31a60a', doctor_id=2)
    if not User.query.filter_by(username='liwenjuan').first():
        db.session.add(user)
    user = User(username='ranpeiru', real_name='冉佩入', role='user', is_active_user=True, password_hash='scrypt:32768:8:1$TaMdxE4KA0ky11kX$52a27033302b02b6fd4371d65d22ef7e6e6d56fb3bb04690c9f106e75957c4fd35ceb1b648a88dbb42b2875038b280796dadf93ef772c29379764bcfa7ff795f', doctor_id=2)
    if not User.query.filter_by(username='ranpeiru').first():
        db.session.add(user)
    user = User(username='lishizhen', real_name='李世珍', role='user', is_active_user=True, password_hash='scrypt:32768:8:1$DC3vzUfE6KVkjLT4$d4f8bead69f928905c0a6353853d937b156dc165d71392962517e73124323c58b7cb4da2cb203399075da5aadd982e9e63e99a5df5c12b558c516b3180778131', doctor_id=3)
    if not User.query.filter_by(username='lishizhen').first():
        db.session.add(user)
    user = User(username='wuchunmei', real_name='吴春梅', role='user', is_active_user=True, password_hash='scrypt:32768:8:1$vOg1g9GAzdaXpcEY$a2d3dead7a80f1518f9504c429aa65ee758e4bf3ba50fbdc43655460acb939b12122953d9a93ac9b2d035f4b6189c7422a1138c6f03c83993dfdecdbf4e5c687', doctor_id=4)
    if not User.query.filter_by(username='wuchunmei').first():
        db.session.add(user)
    user = User(username='zenghuiyin', real_name='曾慧尹', role='user', is_active_user=True, password_hash='scrypt:32768:8:1$YPRVNBaGl4HCVmos$385ae9ae803b63dd299ee7ace73bbfd22f1138759787c16b4b2dabbc7f0696776977780492be7278dad8e73afae5e1fc1c06e6f85cff837062c730da3b0ed11a', doctor_id=5)
    if not User.query.filter_by(username='zenghuiyin').first():
        db.session.add(user)
    user = User(username='wangjinmei', real_name='汪金美', role='user', is_active_user=True, password_hash='scrypt:32768:8:1$7PG68JIql9ceeuzx$a41b022ea5619321f37acc8a8ccb791f0f5200416da81c4061ba8efb019be415121103e071539620bdb61a887b7611cfd72c65f3210d8cee071310f7994d019f', doctor_id=6)
    if not User.query.filter_by(username='wangjinmei').first():
        db.session.add(user)
    user = User(username='zhaoyan', real_name='赵燕', role='assistant', is_active_user=True, password_hash='scrypt:32768:8:1$ayPEkZngMSrwQBty$b7ded3b60e683d604f7d1c4c5463a686b38011964672981b578c1bf2165a47c7185cca1f794459b14c7d3a8cb287695f0d05b08ac1a4ebe9f00f9899ce33a4df', doctor_id=8)
    if not User.query.filter_by(username='zhaoyan').first():
        db.session.add(user)
    user = User(username='haoxinyu', real_name='郝欣雨', role='assistant', is_active_user=True, password_hash='scrypt:32768:8:1$bfh8dJFQCbD7RtQi$740d3d24fbbbd4a36abb4028186c18cd165ebd2ed7086afeddde1bafd2f374fe903610322da2594172d3de580ce119f0f06a77eb41fbb5e2a521a2e4a937eebe', doctor_id=9)
    if not User.query.filter_by(username='haoxinyu').first():
        db.session.add(user)
    user = User(username='wangyundi', real_name='王韵迪', role='assistant', is_active_user=True, password_hash='scrypt:32768:8:1$alxtUcQAEZG4TSdT$d781a2ff2073a2ac25bebf3e356a73aee14766838667c309fd4c20cf2d6395fd3966ba3c6443cc3840611e7a1e853ede85fd6dbbc61c74e3f5f0b7a368426043', doctor_id=10)
    if not User.query.filter_by(username='wangyundi').first():
        db.session.add(user)
    user = User(username='yanganxia', real_name='杨安霞', role='assistant', is_active_user=True, password_hash='scrypt:32768:8:1$KYhMThx2oZW6pa0I$c27f922e13f8b16ed600ea19524f0a13cb7fdb1667c2e17ba1f2ae39d8fa21bad4ba0026a19ca98373f1521e9c044a82ce074ea475187f156892dd2f52ccb0bf', doctor_id=11)
    if not User.query.filter_by(username='yanganxia').first():
        db.session.add(user)
    user = User(username='dongmeilin', real_name='董美林', role='assistant', is_active_user=True, password_hash='scrypt:32768:8:1$rFCAUudsnxFe9rqG$5e996dbe9b9306a0f16d2a0cbe8797b307320fcd239b81dfe132d65282b29f0987768d77fe445b5264f3b01b9ac4ad4a37a48d733b4f075ded56e1bc9329b9a5', doctor_id=12)
    if not User.query.filter_by(username='dongmeilin').first():
        db.session.add(user)
    user = User(username='luoguanghong', real_name='罗光红', role='assistant', is_active_user=True, password_hash='scrypt:32768:8:1$JY6LAgxvb4EEzZ2M$59635081498c74c041a11b074e78cf962b9ecae6791326ea95cc9bb52d268a705267bbbbc13719cbeb4af1915703dc7f6edd4754d9f1e263563a3552c5f28b6f', doctor_id=13)
    if not User.query.filter_by(username='luoguanghong').first():
        db.session.add(user)
    user = User(username='dailing', real_name='戴玲', role='assistant', is_active_user=True, password_hash='scrypt:32768:8:1$5H7tJZd3Bxlngkv8$657adf655e62e102e33046491adf3f16f4d6ef7a139f2a36f2f9ab4a5626854186fa7860c552c6fbebae44f925d852b31b4813677c70e8969e4769967159681b', doctor_id=14)
    if not User.query.filter_by(username='dailing').first():
        db.session.add(user)
    db.session.commit()
    print('导入节假日数据中...')
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
    print('seed_basic_all 完成。')

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        seed_basic_all()