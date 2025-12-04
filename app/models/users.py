from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    real_name = db.Column(db.String(64))
    role = db.Column(db.String(20), default='user') # super_admin, admin, user
    is_active_user = db.Column(db.Boolean, default=True) # 重命名为 is_active_user 避免与 UserMixin.is_active 冲突/混淆，或者直接用 is_active
    
    # 主题设置
    theme_mode = db.Column(db.String(20), default='light') # light, dark
    theme_color = db.Column(db.String(20), default='orange') # orange, blue, green, purple

    # 关联医生
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=True)
    doctor = db.relationship('Doctor', backref='user', uselist=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @property
    def is_active(self):
        return self.is_active_user

    def __repr__(self):
        return f'<User {self.username}>'

@login_manager.user_loader
def load_user(id):
    return db.session.get(User, int(id))
