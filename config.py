import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'enrollment.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'database_repo')
