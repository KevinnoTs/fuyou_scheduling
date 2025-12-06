
import os
import sys
import argparse
from datetime import datetime
from sqlalchemy import func

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models.users import User
from app.models.doctors import Doctor
from app.models.holidays import Holiday
from app.models.workloads import WorkloadRecord, WorkloadScore

def get_seeds_dir():
    seeds_dir = os.path.join(os.path.dirname(__file__), 'seeds')
    if not os.path.exists(seeds_dir):
        os.makedirs(seeds_dir)
    return seeds_dir

def export_basic_module():
    while True:
        print("\n--- 基础数据备份 ---")
        print("1. 导出医生数据 (seed_doctors.py)")
        print("2. 导出用户数据 (seed_users.py)")
        print("3. 导出节假日数据 (seed_holidays.py)")
        print("4. 导出所有基础数据 (seed_basic_all.py)")
        print("0. 返回主菜单")
        choice = input("请选择一个选项: ")

        if choice == '1':
            generate_doctors_seed()
        elif choice == '2':
            generate_users_seed()
        elif choice == '3':
            generate_holidays_seed()
        elif choice == '4':
            generate_basic_all_seed()
        elif choice == '0':
            break
        else:
            print("Invalid option.")

def export_workload_module():
    while True:
        print("\n--- 工作量数据备份 ---")
        print("1. 导出分值设定 (seed_workload_scores.py)")
        print("2. 导出月度工作量记录")
        print("0. 返回主菜单")
        choice = input("请选择一个选项: ")

        if choice == '1':
            generate_workload_scores_seed()
        elif choice == '2':
            generate_workload_records_seed()
        elif choice == '0':
            break
        else:
            print("Invalid option.")

# --- Generators ---

def generate_file(filename, lines):
    output_path = os.path.join(get_seeds_dir(), filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"成功生成: {output_path}")

def get_header_lines(func_name):
    lines = []
    lines.append("# -*- coding: utf-8 -*-")
    lines.append("import sys")
    lines.append("import os")
    lines.append("# Add project root to sys.path for direct execution")
    lines.append("sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))")
    lines.append("")
    lines.append("from app import db, create_app")
    lines.append("from datetime import datetime")
    lines.append("")
    lines.append(f"def {func_name}():")
    return lines

def get_footer_lines(func_name):
    lines = []
    lines.append("    db.session.commit()")
    lines.append(f"    print('{func_name} 完成。')")
    lines.append("")
    lines.append("if __name__ == '__main__':")
    lines.append("    app = create_app()")
    lines.append("    with app.app_context():")
    lines.append(f"        {func_name}()")
    return lines

def generate_doctors_seed():
    print("正在导出医生数据...")
    app = create_app()
    with app.app_context():
        doctors = Doctor.query.all()
        lines = get_header_lines("seed_doctors")
        lines.insert(6, "from app.models.doctors import Doctor") # Add import
        
        for d in doctors:
            args = []
            args.append(f"name='{d.name}'")
            args.append(f"gender='{d.gender}'")
            args.append(f"title='{d.title}'" if d.title else "title=None")
            args.append(f"specialty='{d.specialty}'" if d.specialty else "specialty=''")
            args.append(f"status='{d.status}'")
            args.append(f"annual_leave_days={d.annual_leave_days}")
            args.append(f"used_annual_leave_days={d.used_annual_leave_days}")
            args.append(f"display_order={d.display_order}")
            if d.avatar_path: args.append(f"avatar_path='{d.avatar_path}'")
            if d.resignation_date:
                val = f"datetime.strptime('{d.resignation_date.strftime('%Y-%m-%d')}', '%Y-%m-%d').date()"
                args.append(f"resignation_date={val}")
            args.append(f"id={d.id}")

            lines.append(f"    doctor = Doctor({', '.join(args)})")
            lines.append(f"    if not Doctor.query.get({d.id}):")
            lines.append("        db.session.add(doctor)")
        
        lines.extend(get_footer_lines("seed_doctors"))
        generate_file("seed_doctors.py", lines)

def generate_users_seed():
    print("正在导出用户数据...")
    app = create_app()
    with app.app_context():
        users = User.query.all()
        lines = get_header_lines("seed_users")
        lines.insert(6, "from app.models.users import User")

        for u in users:
            args = []
            args.append(f"username='{u.username}'")
            args.append(f"real_name='{u.real_name}'")
            args.append(f"role='{u.role}'")
            args.append(f"is_active_user={u.is_active_user}")
            args.append(f"password_hash='{u.password_hash}'")
            if u.doctor_id: args.append(f"doctor_id={u.doctor_id}")
            
            lines.append(f"    user = User({', '.join(args)})")
            lines.append(f"    if not User.query.filter_by(username='{u.username}').first():")
            lines.append("        db.session.add(user)")

        lines.extend(get_footer_lines("seed_users"))
        generate_file("seed_users.py", lines)

def generate_holidays_seed():
    print("正在导出节假日数据...")
    app = create_app()
    with app.app_context():
        holidays = Holiday.query.all()
        lines = get_header_lines("seed_holidays")
        lines.insert(6, "from app.models.holidays import Holiday")

        for h in holidays:
            args = []
            val = f"datetime.strptime('{h.date.strftime('%Y-%m-%d')}', '%Y-%m-%d').date()"
            args.append(f"date={val}")
            args.append(f"name='{h.name}'")
            args.append(f"type='{h.type}'")
            source = h.source if hasattr(h, 'source') and h.source else 'manual'
            args.append(f"source='{source}'")
            
            lines.append(f"    holiday = Holiday({', '.join(args)})")
            lines.append(f"    if not Holiday.query.filter_by(date={val}).first():")
            lines.append("        db.session.add(holiday)")

        lines.extend(get_footer_lines("seed_holidays"))
        generate_file("seed_holidays.py", lines)

def generate_basic_all_seed():
    print("正在导出所有基础数据...")
    # This is a bit complex as we need to merge logic, or just run the others.
    # Simpler: Generate one big file.
    app = create_app()
    with app.app_context():
        lines = get_header_lines("seed_basic_all")
        lines.insert(6, "from app.models.users import User")
        lines.insert(7, "from app.models.doctors import Doctor")
        lines.insert(8, "from app.models.holidays import Holiday")
        
        # Doctors
        lines.append("    print('导入医生数据中...')")
        for d in Doctor.query.all():
            args = []
            args.append(f"name='{d.name}'")
            args.append(f"gender='{d.gender}'")
            args.append(f"title='{d.title}'" if d.title else "title=None")
            args.append(f"specialty='{d.specialty}'" if d.specialty else "specialty=''")
            args.append(f"status='{d.status}'")
            args.append(f"annual_leave_days={d.annual_leave_days}")
            args.append(f"used_annual_leave_days={d.used_annual_leave_days}")
            args.append(f"display_order={d.display_order}")
            if d.avatar_path: args.append(f"avatar_path='{d.avatar_path}'")
            if d.resignation_date:
                val = f"datetime.strptime('{d.resignation_date.strftime('%Y-%m-%d')}', '%Y-%m-%d').date()"
                args.append(f"resignation_date={val}")
            args.append(f"id={d.id}")
            lines.append(f"    doctor = Doctor({', '.join(args)})")
            lines.append(f"    if not Doctor.query.get({d.id}):")
            lines.append("        db.session.add(doctor)")
        lines.append("    db.session.commit()")

        # Users
        lines.append("    print('导入用户数据中...')")
        for u in User.query.all():
            args = []
            args.append(f"username='{u.username}'")
            args.append(f"real_name='{u.real_name}'")
            args.append(f"role='{u.role}'")
            args.append(f"is_active_user={u.is_active_user}")
            args.append(f"password_hash='{u.password_hash}'")
            if u.doctor_id: args.append(f"doctor_id={u.doctor_id}")
            lines.append(f"    user = User({', '.join(args)})")
            lines.append(f"    if not User.query.filter_by(username='{u.username}').first():")
            lines.append("        db.session.add(user)")
        lines.append("    db.session.commit()")

        # Holidays
        lines.append("    print('导入节假日数据中...')")
        for h in Holiday.query.all():
            args = []
            val = f"datetime.strptime('{h.date.strftime('%Y-%m-%d')}', '%Y-%m-%d').date()"
            args.append(f"date={val}")
            args.append(f"name='{h.name}'")
            args.append(f"type='{h.type}'")
            source = h.source if hasattr(h, 'source') and h.source else 'manual'
            args.append(f"source='{source}'")
            lines.append(f"    holiday = Holiday({', '.join(args)})")
            lines.append(f"    if not Holiday.query.filter_by(date={val}).first():")
            lines.append("        db.session.add(holiday)")
        
        lines.extend(get_footer_lines("seed_basic_all"))
        generate_file("seed_basic_all.py", lines)

def generate_workload_scores_seed():
    print("正在导出工作量分值设定...")
    app = create_app()
    with app.app_context():
        scores = WorkloadScore.query.all()
        lines = get_header_lines("seed_workload_scores")
        lines.insert(6, "from app.models.workloads import WorkloadScore")

        for s in scores:
            lines.append(f"    item = WorkloadScore.query.filter_by(item_name='{s.item_name}').first()")
            lines.append(f"    if item:")
            lines.append(f"        item.score = {s.score}")
            lines.append(f"    else:")
            lines.append(f"        db.session.add(WorkloadScore(item_name='{s.item_name}', score={s.score}))")

        lines.extend(get_footer_lines("seed_workload_scores"))
        generate_file("seed_workload_scores.py", lines)

def generate_workload_records_seed():
    ym_str = input("请输入年月 (例如: 202510): ")
    if len(ym_str) != 6 or not ym_str.isdigit():
        print("格式无效。请输入 YYYYMM 格式。")
        return
    
    year = int(ym_str[:4])
    month = int(ym_str[4:])
    month_filter = f"{year}-{month:02d}"

    print(f"正在导出 {month_filter} 的工作量记录...")
    
    app = create_app()
    with app.app_context():
        records = WorkloadRecord.query.filter(
            func.strftime('%Y-%m', WorkloadRecord.report_date) == month_filter
        ).order_by(WorkloadRecord.report_date).all()
        
        func_name = f"seed_workload_records_{year}{month:02d}"
        lines = get_header_lines(func_name)
        lines.insert(6, "from app.models.workloads import WorkloadRecord")
        lines.insert(7, "from sqlalchemy import func")

        # Add month-level check
        lines.append(f"    # Safety check: Ensure {month_filter} has no existing data")
        lines.append(f"    existing_count = WorkloadRecord.query.filter(func.strftime('%Y-%m', WorkloadRecord.report_date) == '{month_filter}').count()")
        lines.append("    if existing_count > 0:")
        lines.append(f"        print('警告: {month_filter} 已包含数据 (' + str(existing_count) + ' 条). 导入已终止以防止数据重复。')")
        lines.append("        return")


        if not records:
            print("未找到记录。")
            return

        for r in records:
            args = []
            args.append(f"item_name='{r.item_name}'")
            date_val = f"datetime.strptime('{r.report_date.strftime('%Y-%m-%d')}', '%Y-%m-%d').date()"
            args.append(f"report_date={date_val}")
            
            def safe_str(val): return f"'{val}'" if val is not None else "None"
            args.append(f"doctor_name={safe_str(r.doctor_name)}")
            
            if r.doctor_id: args.append(f"doctor_id={r.doctor_id}")
            else: args.append("doctor_id=None")

            lines.append(f"    record = WorkloadRecord({', '.join(args)})")
            # Removed de-duplication check: Directly add
            lines.append("    db.session.add(record)")

        lines.extend(get_footer_lines(func_name))
        generate_file(f"seed_workload_records_{year}{month:02d}.py", lines)

def main_menu():
    while True:
        print("\n=== 备份与种子生成器 ===")
        print("1. 基础数据模块 (用户, 医生, 节假日)")
        print("2. 工作量模块 (分值, 记录)")
        print("0. 退出")
        choice = input("请选择一个模块: ")

        if choice == '1':
            export_basic_module()
        elif choice == '2':
            export_workload_module()
        elif choice == '0':
            print("正在退出...")
            break
        else:
            print("无效选项。")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n正在退出...")
