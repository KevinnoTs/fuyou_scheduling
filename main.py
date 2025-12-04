from app import create_app, db
from app.models.users import User

app = create_app()

def init_db():
    """初始化数据库并创建默认超级管理员"""
    with app.app_context():
        db.create_all()
        # 检查是否存在超级管理员
        if not User.query.filter_by(username='kevinnots').first():
            print("正在创建超级管理员 (kevinnots)...")
            u = User(username='kevinnots', real_name='超级管理员', role='super_admin')
            u.set_password('123456') # 默认密码
            db.session.add(u)
            db.session.commit()
            print("超级管理员创建成功。")

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
