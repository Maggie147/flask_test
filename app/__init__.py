# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

config_name = 'development'

# 创建项目对象
app = Flask(__name__)

# 加载配置文件内容
app.config.from_object(config[config_name])

db = SQLAlchemy(app)
from app.models import User, Category
from app.views import views
db.init_app(app)


