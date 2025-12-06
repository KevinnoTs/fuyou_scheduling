# -*- coding: utf-8 -*-
import sys
import os
# Add project root to sys.path for direct execution
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.models.users import User
from app import db, create_app
from datetime import datetime

def seed_users():
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
    print('seed_users 完成。')

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        seed_users()