from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'index'
login_manager.login_message = '请先登录以访问该页面'

def create_app(config_class=Config):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)

    # 注册 Blueprint 或导入模型
    from app.models import users, doctors, holidays, schedules
    
    from app.routes import register_routes
    register_routes(app)
    
    from app.routes_workload import register_workload_routes
    register_workload_routes(app)

    return app
