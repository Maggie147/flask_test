# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    SECRET_KEY = os.urandom(24)  # session必须要设置key
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # config mysql

    @staticmethod
    def init_app(app):
        pass


# 开发环境
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:4869@127.0.0.1:3306/test"


# 测试环境
class TestingConfig(Config):
    TESTING = True


# 生产环境
class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}