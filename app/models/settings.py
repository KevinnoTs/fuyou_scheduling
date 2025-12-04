from app import db

class SystemSetting(db.Model):
    __tablename__ = 'system_settings'
    
    key = db.Column(db.String(64), primary_key=True)
    value = db.Column(db.String(128))
    
    def __repr__(self):
        return f'<SystemSetting {self.key}={self.value}>'
