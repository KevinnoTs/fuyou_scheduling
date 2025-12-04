import os
import time
import re
from datetime import datetime, date, timedelta
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.utils import secure_filename
from app import db
from app.models.users import User
from app.models.doctors import Doctor
from app.models.holidays import Holiday
from app.models.settings import SystemSetting

def register_routes(app):
    
    @app.before_request
    def check_annual_leave_reset():
        try:
            current_year = datetime.now().year
            # 检查是否已经重置过
            setting = SystemSetting.query.get('last_leave_reset_year')
            
            if not setting or int(setting.value) < current_year:
                # 需要重置
                # 将所有医生的已休年假重置为 0
                doctors = Doctor.query.all()
                for doctor in doctors:
                    doctor.used_annual_leave_days = 0
                
                # 更新设置
                if not setting:
                    setting = SystemSetting(key='last_leave_reset_year', value=str(current_year))
                    db.session.add(setting)
                else:
                    setting.value = str(current_year)
                
                db.session.commit()
                print(f"Annual leave reset for year {current_year}")
        except Exception as e:
            # 防止数据库未初始化时的错误
            print(f"Error in annual leave reset check: {e}")

    
    @app.route('/')
    @app.route('/index')
    def index():
        if current_user.is_authenticated:
            return redirect(url_for('schedule'))
        return render_template('index.html', title='登录')

    @app.route('/login', methods=['POST'])
    def login():
        if current_user.is_authenticated:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'success': True, 'redirect_url': url_for('schedule')})
            return redirect(url_for('schedule'))
        
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'success': False, 'message': '用户名或密码错误'})
            flash('用户名或密码错误')
            return redirect(url_for('index'))
        
        if not user.is_active:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'success': False, 'message': '该账户已被禁用，请联系管理员'})
            flash('该账户已被禁用，请联系管理员')
            return redirect(url_for('index'))
            
        login_user(user)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'success': True, 'redirect_url': url_for('schedule')})
        return redirect(url_for('schedule'))


    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))

    @app.route('/schedule')
    @login_required
    def schedule():
        return render_template('schedule.html', title='排班表')

    @app.route('/doctors')
    @login_required
    def doctors_list():
        # 按显示顺序升序排列
        search_query = request.args.get('q', '')
        if search_query:
            doctors = Doctor.query.filter(
                (Doctor.name.contains(search_query)) | 
                (Doctor.specialty.contains(search_query))
            ).order_by(Doctor.display_order.asc()).all()
        else:
            doctors = Doctor.query.order_by(Doctor.display_order.asc()).all()
            
        return render_template('doctors_list.html', title='医生列表', doctors=doctors)

    @app.route('/users')
    @login_required
    def users_list():
        if current_user.role not in ['admin', 'super_admin']:
            flash('您没有权限访问该页面')
            return redirect(url_for('index'))
        
        search_query = request.args.get('q', '')
        if search_query:
            users = User.query.filter(
                (User.username.contains(search_query)) | 
                (User.real_name.contains(search_query))
            ).all()
        else:
            users = User.query.all()
            
        return render_template('users_list.html', title='用户列表', users=users)

    @app.route('/users/add', methods=['GET', 'POST'])
    @login_required
    def add_user():
        if current_user.role not in ['admin', 'super_admin']:
            flash('您没有权限执行此操作')
            return redirect(url_for('users_list'))
            
        if request.method == 'POST':
            username = request.form.get('username')
            real_name = request.form.get('real_name')
            role = request.form.get('role')
            password = request.form.get('password')
            
            # 权限检查：普通管理员只能创建普通用户
            if current_user.role == 'admin' and role != 'user':
                flash('管理员只能创建普通用户')
                doctors = Doctor.query.order_by(Doctor.display_order.asc()).all()
                return render_template('user_form.html', title='添加用户', doctors=doctors)

            if User.query.filter_by(username=username).first():
                flash('用户名已存在')
                doctors = Doctor.query.order_by(Doctor.display_order.asc()).all()
                return render_template('user_form.html', title='添加用户', doctors=doctors)
            
            user = User(username=username, real_name=real_name, role=role)
            
            # 处理关联医生
            doctor_id = request.form.get('doctor_id')
            if doctor_id:
                user.doctor_id = int(doctor_id)
                
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            
            flash('用户添加成功')
            return redirect(url_for('users_list'))
            
        doctors = Doctor.query.order_by(Doctor.display_order.asc()).all()
        return render_template('user_form.html', title='添加用户', doctors=doctors)

    @app.route('/users/edit/<int:id>', methods=['GET', 'POST'])
    @login_required
    def edit_user(id):
        if current_user.role not in ['admin', 'super_admin']:
            flash('您没有权限执行此操作')
            return redirect(url_for('users_list'))
            
        user = db.session.get(User, id)
        if not user:
            flash('用户不存在')
            return redirect(url_for('users_list'))
            
        # 权限检查：管理员只能编辑普通用户
        # 权限检查：管理员只能编辑普通用户，或者自己
        if current_user.role == 'admin' and user.role != 'user' and user.id != current_user.id:
            flash('您没有权限编辑此账户')
            return redirect(url_for('users_list'))

        if request.method == 'POST':
            real_name = request.form.get('real_name')
            role = request.form.get('role')
            password = request.form.get('password')
            is_active = request.form.get('is_active') == 'on'
            
            # 防止普通管理员将自己或他人提升为超级管理员
            if role == 'super_admin' and current_user.role != 'super_admin':
                flash('无法设置为超级管理员')
                return render_template('user_form.html', title='编辑用户', user=user)

            user.real_name = real_name
            user.is_active_user = is_active
            
            # 只有超级管理员可以修改角色
            if current_user.role == 'super_admin':
                user.role = role
            
            # 如果提供了密码，则修改密码
            if password and password.strip():
                user.set_password(password)
                flash('密码已修改')
            
            # 关联医生 (仅管理员可操作)
            if current_user.role in ['admin', 'super_admin']:
                doctor_id = request.form.get('doctor_id')
                if doctor_id:
                    user.doctor_id = int(doctor_id)
                else:
                    user.doctor_id = None

            db.session.commit()
            flash('用户信息已更新')
            return redirect(url_for('users_list'))
            
        doctors = Doctor.query.order_by(Doctor.display_order.asc()).all()
        return render_template('user_form.html', title='编辑用户', user=user, doctors=doctors)

    @app.route('/users/delete/<int:id>', methods=['POST'])
    @login_required
    def delete_user(id):
        if current_user.role not in ['admin', 'super_admin']:
            flash('您没有权限执行此操作')
            return redirect(url_for('users_list'))
            
        user = db.session.get(User, id)
        if user:
            # 权限检查
            if current_user.role == 'admin' and user.role != 'user':
                flash('权限不足')
                return redirect(url_for('users_list'))

            if user.role == 'super_admin':
                flash('无法删除超级管理员')
            elif user.id == current_user.id:
                flash('无法删除自己')
            else:
                db.session.delete(user)
                db.session.commit()
                flash('用户已删除')
        else:
            flash('用户不存在')
        return redirect(url_for('users_list'))

    @app.route('/doctors/add', methods=['GET', 'POST'])
    @login_required
    def add_doctor():
        if current_user.role not in ['admin', 'super_admin']:
            flash('您没有权限执行此操作')
            return redirect(url_for('doctors_list'))
        
        if request.method == 'POST':
            name = request.form.get('name')
            gender = request.form.get('gender')
            title = request.form.get('title')
            # 处理多选擅长方向
            specialties = request.form.getlist('specialty')
            specialty = ','.join(specialties) if specialties else ''
            
            status = request.form.get('status')
            annual_leave_days = int(request.form.get('annual_leave_days', 5))
            used_annual_leave_days = int(request.form.get('used_annual_leave_days', 0))
            display_order = int(request.form.get('display_order', 999))
            
            # 验证年假逻辑
            if used_annual_leave_days > annual_leave_days:
                flash('错误：已休年假天数不能大于每年总年假天数')
                # 保留用户输入的数据以便回显
                doctor = Doctor(
                    name=name,
                    gender=gender,
                    title=title,
                    specialty=specialty,
                    status=status,
                    annual_leave_days=annual_leave_days,
                    used_annual_leave_days=used_annual_leave_days,
                    display_order=display_order
                )
                return render_template('doctor_form.html', title='添加医生', doctor=doctor)

            # 处理头像上传
            avatar_path = None
            if 'avatar' in request.files:
                file = request.files['avatar']
                if file and file.filename != '' and file.filename.split('.')[-1].lower() in app.config['ALLOWED_EXTENSIONS']:

                    filename = secure_filename(file.filename)
                    # 使用时间戳防止重名

                    filename = f"{int(time.time())}_{filename}"
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'avatars', filename))
                    avatar_path = f"uploads/avatars/{filename}"

            doctor = Doctor(
                name=name,
                gender=gender,
                title=title,
                specialty=specialty,
                status=status,
                annual_leave_days=annual_leave_days,
                used_annual_leave_days=used_annual_leave_days,
                display_order=display_order,
                avatar_path=avatar_path
            )
            
            if status == 'resigned':
                resignation_date_str = request.form.get('resignation_date')
                if resignation_date_str:

                    try:
                        # input type="month" 返回 YYYY-MM，需要补全为 YYYY-MM-01
                        doctor.resignation_date = datetime.strptime(resignation_date_str + '-01', '%Y-%m-%d').date()
                    except ValueError:
                        pass # 保持默认或处理错误
            
            db.session.add(doctor)
            db.session.commit()
            flash('医生添加成功')
            return redirect(url_for('doctors_list'))
            
        return render_template('doctor_form.html', title='添加医生')

    @app.route('/doctors/edit/<int:id>', methods=['GET', 'POST'])
    @login_required
    def edit_doctor(id):
        if current_user.role not in ['admin', 'super_admin']:
            flash('您没有权限执行此操作')
            return redirect(url_for('doctors_list'))
            
        doctor = db.session.get(Doctor, id)
        if not doctor:
            flash('医生不存在')
            return redirect(url_for('doctors_list'))
            
        if request.method == 'POST':
            # 获取表单数据
            name = request.form.get('name')
            gender = request.form.get('gender')
            title = request.form.get('title')
            specialties = request.form.getlist('specialty')
            specialty = ','.join(specialties) if specialties else ''
            status = request.form.get('status')
            annual_leave_days = int(request.form.get('annual_leave_days', 5))
            used_annual_leave_days = int(request.form.get('used_annual_leave_days', 0))
            display_order = int(request.form.get('display_order', 999))

            # 验证年假逻辑
            if used_annual_leave_days > annual_leave_days:
                flash('错误：已休年假天数不能大于每年总年假天数')
                # 更新对象属性以便回显，但不提交到数据库
                doctor.name = name
                doctor.gender = gender
                doctor.title = title
                doctor.specialty = specialty
                doctor.status = status
                doctor.annual_leave_days = annual_leave_days
                doctor.used_annual_leave_days = used_annual_leave_days
                doctor.display_order = display_order
                return render_template('doctor_form.html', title='编辑医生', doctor=doctor)

            doctor.name = name
            doctor.gender = gender
            doctor.title = title
            doctor.specialty = specialty
            doctor.status = status
            doctor.annual_leave_days = annual_leave_days
            doctor.used_annual_leave_days = used_annual_leave_days
            doctor.display_order = display_order
            
            # 处理头像上传
            if 'avatar' in request.files:
                file = request.files['avatar']
                if file and file.filename != '' and file.filename.split('.')[-1].lower() in app.config['ALLOWED_EXTENSIONS']:

                    filename = secure_filename(file.filename)

                    filename = f"{int(time.time())}_{filename}"
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'avatars', filename))
                    doctor.avatar_path = f"uploads/avatars/{filename}"

            if doctor.status == 'resigned':
                resignation_date_str = request.form.get('resignation_date')
                if resignation_date_str:

                    try:
                        # input type="month" 返回 YYYY-MM，需要补全为 YYYY-MM-01
                        doctor.resignation_date = datetime.strptime(resignation_date_str + '-01', '%Y-%m-%d').date()
                    except ValueError:
                        pass
            else:
                 # 如果改回在职，重置离职时间为默认

                 doctor.resignation_date = date(2099, 12, 31)

            db.session.commit()
            flash('医生信息已更新')
            return redirect(url_for('doctors_list'))
            
        return render_template('doctor_form.html', title='编辑医生', doctor=doctor)

    @app.route('/doctors/delete/<int:id>', methods=['POST'])
    @login_required
    def delete_doctor(id):
        if current_user.role not in ['admin', 'super_admin']:
            flash('您没有权限执行此操作')
            return redirect(url_for('doctors_list'))
            
        doctor = db.session.get(Doctor, id)
        if doctor:
            db.session.delete(doctor)
            db.session.commit()
            flash('医生已删除')
        else:
            flash('医生不存在')
        return redirect(url_for('doctors_list'))
        return redirect(url_for('doctors_list'))

    @app.route('/doctors/upload_avatar/<int:id>', methods=['POST'])
    @login_required
    def upload_doctor_avatar(id):
        doctor = db.session.get(Doctor, id)
        if not doctor:
            flash('医生不存在')
            return redirect(url_for('doctors_list'))
            
        # 权限检查：只有管理员或关联的用户可以修改头像
        if current_user.role not in ['admin', 'super_admin'] and current_user.doctor_id != doctor.id:
            flash('您没有权限修改此医生的头像')
            return redirect(url_for('doctors_list'))
            
        if 'avatar' in request.files:
            file = request.files['avatar']
            if file and file.filename != '' and file.filename.split('.')[-1].lower() in app.config['ALLOWED_EXTENSIONS']:

                filename = secure_filename(file.filename)

                filename = f"{int(time.time())}_{filename}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'avatars', filename))
                doctor.avatar_path = f"uploads/avatars/{filename}"
                db.session.commit()
                flash('头像已更新')
            else:
                flash('上传失败：无效的文件或格式')
        
        return redirect(url_for('doctors_list'))

    # -------------------------------------------------------------------------
    # 节假日管理模块
    # -------------------------------------------------------------------------
    @app.route('/holidays')
    @login_required
    def holidays_list():
        year = request.args.get('year', datetime.now().year, type=int)
        holidays = Holiday.query.filter(
            db.extract('year', Holiday.date) == year
        ).order_by(Holiday.date.asc()).all()
        
        # Calculate total records count
        total_count = len(holidays)
        
        return render_template('holidays_list.html', 
                             title='节假日管理', 
                             holidays=holidays, 
                             current_year=year,
                             total_count=total_count)

    @app.route('/holidays/add', methods=['GET', 'POST'])
    @login_required
    def add_holiday():
        if current_user.role not in ['admin', 'super_admin']:
            flash('您没有权限执行此操作')
            return redirect(url_for('holidays_list'))
            
        if request.method == 'POST':
            start_date_str = request.form.get('start_date')
            end_date_str = request.form.get('end_date')
            name = request.form.get('name')
            type = request.form.get('type')
            
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                end_date = start_date # Default to single day
                
                if end_date_str:
                    end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                
                if end_date < start_date:
                    flash('结束日期不能早于开始日期')
                    return render_template('holiday_form.html', title='添加节假日')

                # Iterate and add
                curr = start_date

                added_count = 0
                
                while curr <= end_date:
                    if not Holiday.query.filter_by(date=curr).first():
                        holiday = Holiday(date=curr, name=name, type=type, source='manual')
                        db.session.add(holiday)
                        added_count += 1
                    curr += timedelta(days=1)
                
                db.session.commit()
                flash(f'成功添加 {added_count} 天节假日')
                return redirect(url_for('holidays_list', year=start_date.year))
                
            except ValueError:
                flash('无效的日期格式')
                
        return render_template('holiday_form.html', title='添加节假日')

    @app.route('/holidays/edit/<int:id>', methods=['GET', 'POST'])
    @login_required
    def edit_holiday(id):
        if current_user.role not in ['admin', 'super_admin']:
            flash('您没有权限执行此操作')
            return redirect(url_for('holidays_list'))
            
        holiday = db.session.get(Holiday, id)
        if not holiday:
            flash('节假日不存在')
            return redirect(url_for('holidays_list'))
            
        if request.method == 'POST':
            name = request.form.get('name')
            type = request.form.get('type')
            # Date is usually not editable to avoid conflicts, but if needed we can add it.
            # For now, let's allow editing name and type.
            
            holiday.name = name
            holiday.type = type
            db.session.commit()
            flash('节假日已更新')
            return redirect(url_for('holidays_list', year=holiday.date.year))
            
        return render_template('holiday_form.html', title='编辑节假日', holiday=holiday)

    @app.route('/holidays/delete/<int:id>', methods=['POST'])
    @login_required
    def delete_holiday(id):
        if current_user.role not in ['admin', 'super_admin']:
            flash('您没有权限执行此操作')
            return redirect(url_for('holidays_list'))
            
        holiday = db.session.get(Holiday, id)
        if holiday:
            year = holiday.date.year
            db.session.delete(holiday)
            db.session.commit()
            flash('节假日已删除')
            return redirect(url_for('holidays_list', year=year))
        
        flash('节假日不存在')
        return redirect(url_for('holidays_list'))

    @app.route('/holidays/import_text', methods=['POST'])
    @login_required
    def import_holidays_text():
        if current_user.role not in ['admin', 'super_admin']:
            return jsonify({'success': False, 'message': '权限不足'})
            
        text = request.form.get('text', '')
        # year param is optional now, we try to detect it
        year_param = request.form.get('year', type=int)
        
        if not text:
            return jsonify({'success': False, 'message': '缺少文本内容'})
            
        try:

            
            # 1. Detect Year
            year_match = re.search(r'(\d{4})年', text)
            if year_match:
                year = int(year_match.group(1))
            elif year_param:
                year = year_param
            else:
                return jsonify({'success': False, 'message': '无法识别年份，请确保文本包含年份（如“2025年”）'})

            # Normalize newlines
            text = text.replace('\r\n', '\n').replace('\r', '\n')
            
            # Split by segments using a more robust method
            # We insert a special separator before "Number + 、" at the start of lines or after whitespace
            processed_text = re.sub(r'(?:^|\s)([一二三四五六七八九十]+、)', r'__SEGMENT__\1', text)
            segments = processed_text.split('__SEGMENT__')
            
            added_count = 0
            
            # Regex for dates
            date_pattern = re.compile(r'(\d{1,2})月(\d{1,2})日')
            
            for segment in segments:
                if not segment.strip():
                    continue
                
                # Remove the numbering "一、"
                segment = re.sub(r'^[一二三四五六七八九十]+、', '', segment.strip())
                
                # Remove newlines within segment to ensure regex works across lines
                segment = segment.replace('\n', '').strip()
                
                # Preprocess text within segment
                segment = segment.replace('：', ':').replace('，', ',').replace('。', '.').replace('、', ',')
                
                if ':' not in segment:
                    continue
                    
                # Extract Name
                name_part, content_part = segment.split(':', 1)
                holiday_name = name_part.strip()
                
                # Separate "Holiday" and "Workday" parts
                work_keyword_index = content_part.find('上班')
                
                holiday_part = content_part
                workday_part = ""
                
                if work_keyword_index != -1:
                    parts = re.split(r'[.;]', content_part)
                    h_parts = []
                    w_parts = []
                    for p in parts:
                        if '上班' in p:
                            w_parts.append(p)
                        else:
                            h_parts.append(p)
                    holiday_part = " ".join(h_parts)
                    workday_part = " ".join(w_parts)
                
                # --- Parse Holiday Dates ---
                
                # 1. Range with Month change: "1月28日...至2月4日"
                ranges_full = re.findall(r'(\d{1,2})月(\d{1,2})日(?:(?!\d{1,2}月\d{1,2}日).)*?至(?:(?!\d{1,2}月\d{1,2}日).)*?(\d{1,2})月(\d{1,2})日', holiday_part, re.DOTALL)
                for m1, d1, m2, d2 in ranges_full:
                    start = date(year, int(m1), int(d1))
                    end = date(year, int(m2), int(d2))
                    curr = start
                    while curr <= end:
                        if not Holiday.query.filter_by(date=curr).first():
                            db.session.add(Holiday(date=curr, name=holiday_name, type='holiday', source='manual'))
                            added_count += 1
                        curr += timedelta(days=1)

                # 2. Range within same month: "4月4日...至6日"
                # Strict regex to avoid matching across months or other numbers
                ranges_short_strict = re.findall(r'(\d{1,2})月(\d{1,2})日(?:(?!\d{1,2}月\d{1,2}日).)*?至(?:(?!\d{1,2}月\d{1,2}日).)*?(\d{1,2})日', holiday_part, re.DOTALL)
                for m, d1, d2 in ranges_short_strict:
                    start = date(year, int(m), int(d1))
                    end = date(year, int(m), int(d2))
                    curr = start
                    while curr <= end:
                        if not Holiday.query.filter_by(date=curr).first():
                            db.session.add(Holiday(date=curr, name=holiday_name, type='holiday', source='manual'))
                            added_count += 1
                        curr += timedelta(days=1)

                # 3. Single Days
                singles = date_pattern.findall(holiday_part)
                for m, d in singles:
                    curr = date(year, int(m), int(d))
                    # Only add if not exists (and thus not added by range logic above)
                    if not Holiday.query.filter_by(date=curr).first():
                        db.session.add(Holiday(date=curr, name=holiday_name, type='holiday', source='manual'))
                        added_count += 1

                # --- Parse Workdays ---
                if workday_part:
                    workdays = date_pattern.findall(workday_part)
                    for m, d in workdays:
                        curr = date(year, int(m), int(d))
                        # Check if exists
                        existing = Holiday.query.filter_by(date=curr).first()
                        if existing:
                            if existing.type == 'holiday':
                                existing.type = 'workday'
                                existing.name = f"{holiday_name}调休"
                        else:
                            db.session.add(Holiday(date=curr, name=f"{holiday_name}调休", type='workday', source='manual'))
                            added_count += 1
                            
            db.session.commit()
            return jsonify({'success': True, 'message': f'成功导入 {added_count} 条数据 (年份: {year})'})
            
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})

    @app.route('/api/update_theme', methods=['POST'])
    @login_required
    def update_theme():
        data = request.get_json()
        mode = data.get('mode')
        color = data.get('color')

        if mode:
            current_user.theme_mode = mode
        if color:
            current_user.theme_color = color
        
        try:
            db.session.commit()
            return jsonify({'success': True})
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'error': str(e)}), 500
