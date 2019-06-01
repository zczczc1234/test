

from flask import Flask
from flask_script import Manager
from flask_mail import Mail

from app.models import db
from app.views import blue

app = Flask(__name__)

app.register_blueprint(blueprint=blue,url_prefix='/app')
# 初始化数据库的配置
# mysql + pymysql://root:123456@127.0.0.1:3306/flask8
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 初始化数据库的连接信息
db.init_app(app)





manage = Manager(app=app)

if __name__ == '__main__':
    # app.run()
    manage.run()