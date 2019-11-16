import os

import pymongo
from flask import g


def get_db():
    if 'db' not in g:
        host = os.environ.get('DATABASE_HOST', 'localhost')
        port = os.environ.get('DATABASE_PORT', '27017')

        g.db = pymongo.MongoClient(host, int(port))

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
        print('Database closed!')
