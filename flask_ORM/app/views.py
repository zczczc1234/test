import os
import uuid

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import and_,or_,not_


from app.models import Student, db, Grade, Course

blue = Blueprint('app',__name__)






@blue.route('/del_stu/<int:id>/',methods=['GET'])
def del_stu(id):
    if request.method == 'GET':
        stu = Student.query.filter(Student.id==id).first()
        stu.delete()
        return '删除数据成功'



@blue.route('/sel_stu/',methods=['GET'])
def sel_stu():
    if request.method == 'GET':
        stu = Student.query.filter(Student.s_name=='张三')
        stu = Student.query.filter_by(s_name='张三')

       
        stu = Student.query.all()[0]
        stu = Student.query.first()

      
        stu = Student.query.get(2)
        stu = Student.query.filter_by(id=2).first()
        stu = Student.query.filter(Student.id==2).first()
        print(stu)

        # 排序
        stus = Student.query.order_by('-id').all()
        stus = Student.query.order_by('id').all()
        # print(stus)

        # 分页,limit 1,3
        page = 3
        stus = Student.query.all()[(page-1)*3:page*3]
        # offset():跳过几个参数 limit()：查询几个参数
        stus = Student.query.offset((page-1)*3).limit(3).all()
        print(stus)

        #gt ge lt le
        stus = Student.query.filter(Student.s_age.__gt__(20)).all()
        stus = Student.query.filter(Student.s_age>(20)).all()
        print(stus)


        # 模糊查询
        stus = Student.query.filter(Student.s_name.contains('隔壁')).all()
        print(stus)
        stus = Student.query.filter(Student.s_name.startswith('张')).all()
        print(stus)
        stus = Student.query.filter(Student.s_name.endswith('4')).all()
        print(stus)
        stus = Student.query.filter(Student.s_name.like('__老%')).all()
        print(stus)


        # 组合查询，查询姓名中包含‘哥’且年龄大于22
        stus = Student.query.filter(Student.s_name.contains('哥')).filter(Student.s_age>22).all()
        stus = Student.query.filter(Student.s_name.contains('哥'),Student.s_age>22).all()

        stus = Student.query.filter(and_(Student.s_name.contains('哥') , Student.s_age>22)).all()
        print(stus)

        # 或 or_
        stus = Student.query.filter(or_(Student.s_name.contains('哥'),Student.s_age>22)).all()
        print(stus)

        # 非 not_
        stus = Student.query.filter(not_(Student.s_name.contains('哥')), Student.s_age > 22).all()
        print(stus)
        return '查询成功'


@blue.route('/all_stu/',methods=['GET'])
def all_stu():
    if request.method == 'GET':
        # 从url中获取page参数
        page = int(request.args.get('page',1))
        pg = Student.query.paginate(page,3)
        # 获取当前页的数据
        stus = pg.items
        return render_template('stus.html',stus=stus,pg=pg)


@blue.route('/edit_stu/<int:id>/',methods=['GET','POST'])
def edit_stu(id):
    if request.method == 'GET':
        stu = Student.query.get(id)
        return render_template('edit.html',stu=stu)
    if request.method == 'POST':
        # 接受图片，并保存图片
        icon = request.files.get('images')
        # 找到当前路径的上两层路径，然后拼接想要的路径
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # 获取媒体文件的路劲
        STATIC_DIR = os.path.join(BASE_DIR,'static')
        MEDIA_DIR = os.path.join(STATIC_DIR,'media')
        # 生成图片的名称
        filename = str(uuid.uuid4())
        a = icon.mimetype.split('/')[-1:][0]
        name = filename + '.'+ a
        # 拼接图片的保存地址
        path = os.path.join(MEDIA_DIR,name)
        # 保存
        icon.save(path)

        # 修改用户的头像icon字段
        stu = Student.query.get(id)
        stu.icon = name
        stu.save()

	# 修改用户姓名
        stu_name = request.args.get('up_name')
        print(stu_name)
        stu = Student.query.get(id)
        stu.s_name = stu_nam
        stu.save()

        # 重定向到列表页面
        return redirect(url_for('app.all_stu'))