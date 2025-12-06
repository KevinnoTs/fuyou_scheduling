# -*- coding: utf-8 -*-
import sys
import os
# Add project root to sys.path for direct execution
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.models.workloads import WorkloadScore
from app import db, create_app
from datetime import datetime

def seed_workload_scores():
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查妇科常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查妇科常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查妇科腹部加收,彩色多普勒超声常规检查妇科经阴道加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查妇科腹部加收,彩色多普勒超声常规检查妇科经阴道加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查妇科经阴道加收').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查妇科经阴道加收', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查妇科泌尿系加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查妇科泌尿系加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查妇科泌尿系加收,彩色多普勒超声常规检查妇科经阴道加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查妇科泌尿系加收,彩色多普勒超声常规检查妇科经阴道加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查妇科胃肠道加收,彩色多普勒超声常规检查妇科经阴道加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查妇科胃肠道加收,彩色多普勒超声常规检查妇科经阴道加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查腹部胃肠道加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查腹部胃肠道加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查腹部胃肠道加收,彩色多普勒超声常规检查妇科经阴道加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查腹部胃肠道加收,彩色多普勒超声常规检查妇科经阴道加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查胃肠道腹部加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查胃肠道腹部加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查胃肠道腹部加收,彩色多普勒超声常规检查妇科经阴道加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查胃肠道腹部加收,彩色多普勒超声常规检查妇科经阴道加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查胃肠道腹部加收,彩色多普勒超声常规检查妇科泌尿系加收,彩色多普勒超声常规检查妇科经阴道加收').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查胃肠道腹部加收,彩色多普勒超声常规检查妇科泌尿系加收,彩色多普勒超声常规检查妇科经阴道加收', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查妇科经阴道加收,彩色多普勒超声常规检查妇科常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查妇科经阴道加收,彩色多普勒超声常规检查妇科常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查妇科经阴道加收,孕期彩超检查胎盘成熟度常规,孕期彩超检查孕中期产科常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查妇科经阴道加收,孕期彩超检查胎盘成熟度常规,孕期彩超检查孕中期产科常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查妇科泌尿系加收').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查妇科泌尿系加收', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查腹部常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查腹部常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查妇科经阴道加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查妇科经阴道加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查妇科泌尿系加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查妇科泌尿系加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查妇科泌尿系加收,彩色多普勒超声常规检查腹部妇科加收').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查妇科泌尿系加收,彩色多普勒超声常规检查腹部妇科加收', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查腹部妇科加收,彩色多普勒超声常规检查腹部胃肠道加收').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查腹部妇科加收,彩色多普勒超声常规检查腹部胃肠道加收', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查腹部泌尿系加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查腹部泌尿系加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查腹部泌尿系加收,彩色多普勒超声常规检查腹部妇科加收,彩色多普勒超声常规检查腹部胃肠道加收').first()
    if item:
        item.score = 4.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查腹部泌尿系加收,彩色多普勒超声常规检查腹部妇科加收,彩色多普勒超声常规检查腹部胃肠道加收', score=4.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查腹部胃肠道加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查腹部胃肠道加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查泌尿系常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查泌尿系常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查腹部胃肠道加收,彩色多普勒超声常规检查腹部常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查腹部胃肠道加收,彩色多普勒超声常规检查腹部常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查泌尿系常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查泌尿系常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查泌尿系常规,彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查妇科经阴道加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查泌尿系常规,彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查妇科经阴道加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查泌尿系常规,彩色多普勒超声常规检查腹部妇科加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查泌尿系常规,彩色多普勒超声常规检查腹部妇科加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查泌尿系常规,彩色多普勒超声常规检查泌尿系胃肠道加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查泌尿系常规,彩色多普勒超声常规检查泌尿系胃肠道加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查男性生殖系统常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查男性生殖系统常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查男性生殖系统常规,彩色多普勒超声常规检查妇科泌尿系加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查男性生殖系统常规,彩色多普勒超声常规检查妇科泌尿系加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查胃肠道常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查胃肠道常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查胃肠道常规,彩色多普勒超声常规检查胃肠道腹部加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查胃肠道常规,彩色多普勒超声常规检查胃肠道腹部加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查胃肠道腹部加收').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查胃肠道腹部加收', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查胸部常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查胸部常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声床旁检查加收床旁加收常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声床旁检查加收床旁加收常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='产前超声筛查及胎儿四维超声检查中孕期实时四维彩超常规').first()
    if item:
        item.score = 13.0
    else:
        db.session.add(WorkloadScore(item_name='产前超声筛查及胎儿四维超声检查中孕期实时四维彩超常规', score=13.0))
    item = WorkloadScore.query.filter_by(item_name='妇科彩超检查（三八节活动）妇科常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='妇科彩超检查（三八节活动）妇科常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='妇科彩色多普勒超声常规检查妇科经阴道加收').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='妇科彩色多普勒超声常规检查妇科经阴道加收', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='妇科盆腔三维超声检查三维彩超常规').first()
    if item:
        item.score = 6.0
    else:
        db.session.add(WorkloadScore(item_name='妇科盆腔三维超声检查三维彩超常规', score=6.0))
    item = WorkloadScore.query.filter_by(item_name='妇科脏器(经阴道排卵检测)妇科脏器经阴道').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='妇科脏器(经阴道排卵检测)妇科脏器经阴道', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='妇科脏器(经阴道排卵检测)妇科脏器经阴道,妇科脏器(经阴道排卵检测)妇科脏器排卵检测三次').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='妇科脏器(经阴道排卵检测)妇科脏器经阴道,妇科脏器(经阴道排卵检测)妇科脏器排卵检测三次', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='妇科脏器(经阴道排卵检测)妇科脏器经阴道,妇科脏器(经阴道排卵检测)妇科脏器排卵检测五次').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='妇科脏器(经阴道排卵检测)妇科脏器经阴道,妇科脏器(经阴道排卵检测)妇科脏器排卵检测五次', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='妇科脏器(经阴道排卵检测)妇科脏器经阴道,妇科脏器(经阴道排卵检测)妇科脏器排卵检测一次').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='妇科脏器(经阴道排卵检测)妇科脏器经阴道,妇科脏器(经阴道排卵检测)妇科脏器排卵检测一次', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='妇科脏器(经阴道排卵检测)妇科脏器排卵检测一次').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='妇科脏器(经阴道排卵检测)妇科脏器排卵检测一次', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='妇科脏器三维超声检查妇科脏器经阴道').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='妇科脏器三维超声检查妇科脏器经阴道', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='妇科脏器三维超声检查妇科脏器排卵检测一次').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='妇科脏器三维超声检查妇科脏器排卵检测一次', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='临床操作的彩色多普勒超声引导').first()
    if item:
        item.score = 5.0
    else:
        db.session.add(WorkloadScore(item_name='临床操作的彩色多普勒超声引导', score=5.0))
    item = WorkloadScore.query.filter_by(item_name='其他加收,浅表器官彩色多普勒超声检查关节常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='其他加收,浅表器官彩色多普勒超声检查关节常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='脐血流检查脐血流常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='脐血流检查脐血流常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查关节常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查关节常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查关节常规,浅表器官彩色多普勒超声检查关节关节加收,浅表器官彩色多普勒超声检查关节阴囊、双侧睾丸、附睾加收').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查关节常规,浅表器官彩色多普勒超声检查关节关节加收,浅表器官彩色多普勒超声检查关节阴囊、双侧睾丸、附睾加收', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查关节常规,浅表器官彩色多普勒超声检查关节其他加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查关节常规,浅表器官彩色多普勒超声检查关节其他加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查关节常规,浅表器官彩色多普勒超声检查关节阴囊、双侧睾丸、附睾加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查关节常规,浅表器官彩色多普勒超声检查关节阴囊、双侧睾丸、附睾加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查关节常规,浅表器官彩色多普勒超声检查关节阴囊、双侧睾丸、附睾加收,浅表器官彩色多普勒超声检查关节颅腔加收').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查关节常规,浅表器官彩色多普勒超声检查关节阴囊、双侧睾丸、附睾加收,浅表器官彩色多普勒超声检查关节颅腔加收', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查关节常规,浅表器官彩色多普勒超声检查关节阴囊、双侧睾丸、附睾加收,浅表器官彩色多普勒超声检查关节其他加收').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查关节常规,浅表器官彩色多普勒超声检查关节阴囊、双侧睾丸、附睾加收,浅表器官彩色多普勒超声检查关节其他加收', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查关节常规,浅表器官彩色多普勒超声检查阴囊、双侧睾丸、附睾常规,浅表器官彩色多普勒超声检查关节其他加收').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查关节常规,浅表器官彩色多普勒超声检查阴囊、双侧睾丸、附睾常规,浅表器官彩色多普勒超声检查关节其他加收', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查甲状腺及颈部淋巴结常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查甲状腺及颈部淋巴结常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查甲状腺及颈部淋巴结常规,浅表器官彩色多普勒超声检查甲状腺及颈部淋巴结乳腺及其引流区淋巴结加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查甲状腺及颈部淋巴结常规,浅表器官彩色多普勒超声检查甲状腺及颈部淋巴结乳腺及其引流区淋巴结加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查颅腔常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查颅腔常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查颅腔常规,浅表器官彩色多普勒超声检查颅腔其他加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查颅腔常规,浅表器官彩色多普勒超声检查颅腔其他加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查颅腔常规,浅表器官彩色多普勒超声检查颅腔体表包块加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查颅腔常规,浅表器官彩色多普勒超声检查颅腔体表包块加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查颅腔常规,浅表器官彩色多普勒超声检查颅腔阴囊、双侧睾丸、附睾加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查颅腔常规,浅表器官彩色多普勒超声检查颅腔阴囊、双侧睾丸、附睾加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查颅腔常规,浅表器官彩色多普勒超声检查体表包块常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查颅腔常规,浅表器官彩色多普勒超声检查体表包块常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查其他常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查其他常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查乳腺及其引流区淋巴结常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查乳腺及其引流区淋巴结常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查乳腺及其引流区淋巴结常规,浅表器官彩色多普勒超声检查甲状腺及颈部淋巴结其他加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查乳腺及其引流区淋巴结常规,浅表器官彩色多普勒超声检查甲状腺及颈部淋巴结其他加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查乳腺及其引流区淋巴结常规,浅表器官彩色多普勒超声检查乳腺及其引流区淋巴结甲状腺及颈部淋巴结加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查乳腺及其引流区淋巴结常规,浅表器官彩色多普勒超声检查乳腺及其引流区淋巴结甲状腺及颈部淋巴结加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查乳腺及其引流区淋巴结常规,浅表器官彩色多普勒超声检查乳腺及其引流区淋巴结其他加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查乳腺及其引流区淋巴结常规,浅表器官彩色多普勒超声检查乳腺及其引流区淋巴结其他加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查乳腺及其引流区淋巴结甲状腺及颈部淋巴结加收').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查乳腺及其引流区淋巴结甲状腺及颈部淋巴结加收', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查双涏腺及颈部淋巴结常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查双涏腺及颈部淋巴结常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查双涏腺及颈部淋巴结常规,浅表器官彩色多普勒超声检查关节常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查双涏腺及颈部淋巴结常规,浅表器官彩色多普勒超声检查关节常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查双涏腺及颈部淋巴结常规,浅表器官彩色多普勒超声检查双涏腺及颈部淋巴结其他加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查双涏腺及颈部淋巴结常规,浅表器官彩色多普勒超声检查双涏腺及颈部淋巴结其他加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查双涎腺及颈部淋巴结常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查双涎腺及颈部淋巴结常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查双涎腺及颈部淋巴结常规,浅表器官彩色多普勒超声检查体表包块常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查双涎腺及颈部淋巴结常规,浅表器官彩色多普勒超声检查体表包块常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查体表包块常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查体表包块常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查体表包块常规,浅表器官彩色多普勒超声检查甲状腺及颈部淋巴结常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查体表包块常规,浅表器官彩色多普勒超声检查甲状腺及颈部淋巴结常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查体表包块常规,浅表器官彩色多普勒超声检查双涎腺及颈部淋巴结常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查体表包块常规,浅表器官彩色多普勒超声检查双涎腺及颈部淋巴结常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查体表包块常规,浅表器官彩色多普勒超声检查体表包块其他加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查体表包块常规,浅表器官彩色多普勒超声检查体表包块其他加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查体表包块常规,浅表器官彩色多普勒超声检查体表包块双涏腺及颈部淋巴结加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查体表包块常规,浅表器官彩色多普勒超声检查体表包块双涏腺及颈部淋巴结加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查体表包块常规,浅表器官彩色多普勒超声检查阴囊、双侧睾丸、附睾常规,浅表器官彩色多普勒超声检查体表包块其他加收').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查体表包块常规,浅表器官彩色多普勒超声检查阴囊、双侧睾丸、附睾常规,浅表器官彩色多普勒超声检查体表包块其他加收', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查阴囊、双侧睾丸、附睾常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查阴囊、双侧睾丸、附睾常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查阴囊、双侧睾丸、附睾常规,浅表器官彩色多普勒超声检查阴囊、双侧睾丸、附睾关节加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查阴囊、双侧睾丸、附睾常规,浅表器官彩色多普勒超声检查阴囊、双侧睾丸、附睾关节加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查阴囊、双侧睾丸、附睾常规,浅表器官彩色多普勒超声检查阴囊、双侧睾丸、附睾关节加收,浅表器官彩色多普勒超声检查阴囊、双侧睾丸、附睾其他加收').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查阴囊、双侧睾丸、附睾常规,浅表器官彩色多普勒超声检查阴囊、双侧睾丸、附睾关节加收,浅表器官彩色多普勒超声检查阴囊、双侧睾丸、附睾其他加收', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='四肢血管彩超检查四肢血管股静脉,四肢血管彩超检查四肢血管腘静脉(加收),四肢血管彩超检查四肢血管胫前静脉(加收),四肢血管彩超检查四肢血管胫后静脉(加收)').first()
    if item:
        item.score = 6.0
    else:
        db.session.add(WorkloadScore(item_name='四肢血管彩超检查四肢血管股静脉,四肢血管彩超检查四肢血管腘静脉(加收),四肢血管彩超检查四肢血管胫前静脉(加收),四肢血管彩超检查四肢血管胫后静脉(加收)', score=6.0))
    item = WorkloadScore.query.filter_by(item_name='胎儿大脑中动脉监测颅内血管常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='胎儿大脑中动脉监测颅内血管常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='心脏彩超检查心脏常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='心脏彩超检查心脏常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='心脏彩超检查心脏常规,心脏彩超检查心脏心功能').first()
    if item:
        item.score = 4.0
    else:
        db.session.add(WorkloadScore(item_name='心脏彩超检查心脏常规,心脏彩超检查心脏心功能', score=4.0))
    item = WorkloadScore.query.filter_by(item_name='心脏彩超检查心脏心功能').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='心脏彩超检查心脏心功能', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='心脏彩超检查心脏心功能,心脏彩超检查心脏常规').first()
    if item:
        item.score = 4.0
    else:
        db.session.add(WorkloadScore(item_name='心脏彩超检查心脏心功能,心脏彩超检查心脏常规', score=4.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查（免费）孕中期产科常规,孕期彩超检查（免费）胎盘成熟度常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查（免费）孕中期产科常规,孕期彩超检查（免费）胎盘成熟度常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查脐血流常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查脐血流常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规,孕期彩超检查孕晚期产科常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规,孕期彩超检查孕晚期产科常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规,孕期彩超检查孕晚期产科常规,彩色多普勒超声常规检查妇科经阴道加收').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规,孕期彩超检查孕晚期产科常规,彩色多普勒超声常规检查妇科经阴道加收', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查胎盘成熟度常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查胎盘成熟度常规,孕期彩超检查脐血流常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查胎盘成熟度常规,孕期彩超检查脐血流常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查胎盘成熟度常规,孕期彩超检查孕晚期产科常规,彩色多普勒超声常规检查妇科经阴道加收,孕期彩超检查脐血流常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查胎盘成熟度常规,孕期彩超检查孕晚期产科常规,彩色多普勒超声常规检查妇科经阴道加收,孕期彩超检查脐血流常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查胎盘成熟度常规,孕期彩超检查孕晚期产科常规,孕期彩超检查脐血流常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查胎盘成熟度常规,孕期彩超检查孕晚期产科常规,孕期彩超检查脐血流常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查胎盘成熟度常规,孕期彩超检查孕中期产科常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查胎盘成熟度常规,孕期彩超检查孕中期产科常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,彩色多普勒超声常规检查妇科经阴道加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,彩色多普勒超声常规检查妇科经阴道加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,彩色多普勒超声常规检查妇科经阴道加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,彩色多普勒超声常规检查妇科经阴道加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,彩色多普勒超声常规检查妇科经阴道加收,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,彩色多普勒超声常规检查妇科经阴道加收,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,彩色多普勒超声常规检查妇科泌尿系加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,彩色多普勒超声常规检查妇科泌尿系加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,胎儿大脑中动脉监测颅内血管常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,胎儿大脑中动脉监测颅内血管常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,胎儿大脑中动脉监测颅内血管常规,彩色多普勒超声常规检查妇科经阴道加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 4.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,胎儿大脑中动脉监测颅内血管常规,彩色多普勒超声常规检查妇科经阴道加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=4.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,胎儿大脑中动脉监测颅内血管常规,孕期彩超检查脐血流常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,胎儿大脑中动脉监测颅内血管常规,孕期彩超检查脐血流常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,胎儿大脑中动脉监测颅内血管常规,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,胎儿大脑中动脉监测颅内血管常规,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,胎儿大脑中动脉监测颅内血管常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,胎儿大脑中动脉监测颅内血管常规,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,胎儿大脑中动脉监测颅内血管常规,孕期彩超检查孕晚期产科床旁加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 6.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,胎儿大脑中动脉监测颅内血管常规,孕期彩超检查孕晚期产科床旁加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=6.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查脐血流常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查脐血流常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查胎盘成熟度常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查胎盘成熟度常规,孕期彩超检查脐血流常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查胎盘成熟度常规,孕期彩超检查脐血流常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科床旁加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 5.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科床旁加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=5.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科大脑中动脉,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科大脑中动脉,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科大脑中动脉,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科大脑中动脉,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科大脑中动脉,孕期彩超检查孕晚期产科经阴道加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 4.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科大脑中动脉,孕期彩超检查孕晚期产科经阴道加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=4.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科大脑中动脉,孕期彩超检查孕晚期产科经阴道加收,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 4.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科大脑中动脉,孕期彩超检查孕晚期产科经阴道加收,孕期彩超检查胎盘成熟度常规', score=4.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科腹部加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科腹部加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科经阴道加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科经阴道加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科经阴道加收,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科经阴道加收,孕期彩超检查胎盘成熟度常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科床旁加收').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科床旁加收', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科床旁加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 4.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科床旁加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=4.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科大脑中动脉').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科大脑中动脉', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科经阴道加收').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科经阴道加收', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科经阴道加收,孕期彩超检查脐血流常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科经阴道加收,孕期彩超检查脐血流常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科经阴道加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科经阴道加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕中期产科常规').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕中期产科常规', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕中期产科常规,彩色多普勒超声常规检查妇科经阴道加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕中期产科常规,彩色多普勒超声常规检查妇科经阴道加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕中期产科常规,彩色多普勒超声常规检查妇科经阴道加收,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕中期产科常规,彩色多普勒超声常规检查妇科经阴道加收,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕中期产科常规,彩色多普勒超声常规检查胃肠道腹部加收,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕中期产科常规,彩色多普勒超声常规检查胃肠道腹部加收,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕中期产科常规,胎儿大脑中动脉监测颅内血管常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕中期产科常规,胎儿大脑中动脉监测颅内血管常规,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕中期产科常规,孕期彩超检查脐血流常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕中期产科常规,孕期彩超检查脐血流常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕中期产科常规,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕中期产科常规,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕中期产科常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕中期产科常规,孕期彩超检查胎盘成熟度常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕中期产科常规,孕期彩超检查孕中期产科大脑中动脉,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕中期产科常规,孕期彩超检查孕中期产科大脑中动脉,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕中期产科常规,孕期彩超检查孕中期产科腹部加收,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕中期产科常规,孕期彩超检查孕中期产科腹部加收,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕中期产科常规,孕期彩超检查孕中期产科经阴道加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕中期产科常规,孕期彩超检查孕中期产科经阴道加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕中期产科常规,孕期彩超检查孕中期产科经阴道加收,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕中期产科常规,孕期彩超检查孕中期产科经阴道加收,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕晚期彩色多普勒超声常规检查妇科经阴道加收').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='孕晚期彩色多普勒超声常规检查妇科经阴道加收', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='子宫输卵管造影彩超检查妇科脏器经阴道,子宫输卵管造影彩超检查妇科脏器输卵管造影,子宫输卵管造影彩超检查妇科脏器腔内彩超,子宫输卵管造影彩超检查妇科脏器灰阶立体成像').first()
    if item:
        item.score = 9.0
    else:
        db.session.add(WorkloadScore(item_name='子宫输卵管造影彩超检查妇科脏器经阴道,子宫输卵管造影彩超检查妇科脏器输卵管造影,子宫输卵管造影彩超检查妇科脏器腔内彩超,子宫输卵管造影彩超检查妇科脏器灰阶立体成像', score=9.0))
    item = WorkloadScore.query.filter_by(item_name='子宫输卵管造影彩超检查妇科脏器输卵管造影').first()
    if item:
        item.score = 9.0
    else:
        db.session.add(WorkloadScore(item_name='子宫输卵管造影彩超检查妇科脏器输卵管造影', score=9.0))
    item = WorkloadScore.query.filter_by(item_name='双胎加收').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='双胎加收', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='两癌妇科').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='两癌妇科', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='两癌乳腺').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='两癌乳腺', score=1.0))
    item = WorkloadScore.query.filter_by(item_name='子宫输卵管造影彩超检查妇科脏器输卵管造影,子宫输卵管造影彩超检查妇科脏器腔内彩超,子宫输卵管造影彩超检查妇科脏器灰阶立体成像').first()
    if item:
        item.score = 9.0
    else:
        db.session.add(WorkloadScore(item_name='子宫输卵管造影彩超检查妇科脏器输卵管造影,子宫输卵管造影彩超检查妇科脏器腔内彩超,子宫输卵管造影彩超检查妇科脏器灰阶立体成像', score=9.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕中期产科经阴道加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕中期产科经阴道加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科经阴道加收,孕期彩超检查孕晚期产科床旁加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 6.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科经阴道加收,孕期彩超检查孕晚期产科床旁加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=6.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科腹部加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科腹部加收,孕期彩超检查脐血流常规,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='孕期彩超检查脐血流常规,孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科经阴道加收,孕期彩超检查胎盘成熟度常规').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='孕期彩超检查脐血流常规,孕期彩超检查孕晚期产科常规,孕期彩超检查孕晚期产科经阴道加收,孕期彩超检查胎盘成熟度常规', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查妇科腹部加收,彩色多普勒超声常规检查妇科胃肠道加收').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查妇科常规,彩色多普勒超声常规检查妇科腹部加收,彩色多普勒超声常规检查妇科胃肠道加收', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查泌尿系常规,彩色多普勒超声常规检查泌尿系男性生殖系统加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查泌尿系常规,彩色多普勒超声常规检查泌尿系男性生殖系统加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查胃肠道常规,彩色多普勒超声常规检查胃肠道妇科加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查胃肠道常规,彩色多普勒超声常规检查胃肠道妇科加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查胃肠道常规,彩色多普勒超声常规检查胃肠道泌尿系加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查胃肠道常规,彩色多普勒超声常规检查胃肠道泌尿系加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查妇科常规').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='彩色多普勒超声常规检查腹部常规,彩色多普勒超声常规检查妇科常规', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查体表包块常规,浅表器官彩色多普勒超声检查体表包块双涏腺及颈部淋巴结加收,浅表器官彩色多普勒超声检查体表包块乳腺及其引流区淋巴结加收').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查体表包块常规,浅表器官彩色多普勒超声检查体表包块双涏腺及颈部淋巴结加收,浅表器官彩色多普勒超声检查体表包块乳腺及其引流区淋巴结加收', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查关节常规,浅表器官彩色多普勒超声检查关节阴囊、双侧睾丸、附睾加收,浅表器官彩色多普勒超声检查关节体表包块加收').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查关节常规,浅表器官彩色多普勒超声检查关节阴囊、双侧睾丸、附睾加收,浅表器官彩色多普勒超声检查关节体表包块加收', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查关节常规,浅表器官彩色多普勒超声检查关节颅腔加收,浅表器官彩色多普勒超声检查关节体表包块加收').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查关节常规,浅表器官彩色多普勒超声检查关节颅腔加收,浅表器官彩色多普勒超声检查关节体表包块加收', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查其他常规,浅表器官彩色多普勒超声检查其他乳腺及其引流区淋巴结加收').first()
    if item:
        item.score = 2.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查其他常规,浅表器官彩色多普勒超声检查其他乳腺及其引流区淋巴结加收', score=2.0))
    item = WorkloadScore.query.filter_by(item_name='浅表器官彩色多普勒超声检查颅腔常规,浅表器官彩色多普勒超声检查颅腔关节加收,浅表器官彩色多普勒超声检查颅腔其他加收').first()
    if item:
        item.score = 3.0
    else:
        db.session.add(WorkloadScore(item_name='浅表器官彩色多普勒超声检查颅腔常规,浅表器官彩色多普勒超声检查颅腔关节加收,浅表器官彩色多普勒超声检查颅腔其他加收', score=3.0))
    item = WorkloadScore.query.filter_by(item_name='膀胱残余尿量测定泌尿系统膀胱余尿测定').first()
    if item:
        item.score = 1.0
    else:
        db.session.add(WorkloadScore(item_name='膀胱残余尿量测定泌尿系统膀胱余尿测定', score=1.0))
    db.session.commit()
    print('seed_workload_scores 完成。')

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        seed_workload_scores()