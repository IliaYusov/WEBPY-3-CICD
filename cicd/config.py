import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRE_URI') \
        or 'postgresql://Ouster:1234@localhost:5432/flask_test_api'
    SALT = os.environ.get('SALT') or 'my_sJHLHLHKLаваыпuper_s!alt_#4$4344'
