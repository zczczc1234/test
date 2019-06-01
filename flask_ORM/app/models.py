from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    s_name = db.Column(db.String(10),unique=True,nullable=False)
    s_age = db.Column(db.Integer,default=20)
    s_gender = db.Column(db.Boolean,default=1)
    create_time = db.Column(db.DateTime,default=datetime.now)
    g_id = db.Column(db.Integer,db.ForeignKey('grade.id'),nullable=True)
    icon = db.Column(db.String(100),nullable=True)
    __tablename__ = 'student'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


