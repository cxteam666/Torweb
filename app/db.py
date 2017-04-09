#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

import MySQLdb
import redis as PyRedis


# Wrapper MySQL
class DB:

    def __init__(self,host,port,user,passwd,dbname,charset="utf8"):
        self._conn = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=dbname, charset=charset)
        self._cur = self._conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    def close(self):
        self._cur.close()
        self._conn.close()

    def select(self,sql):
        self._cur.execute(sql)
        return self._cur.fetchall()

    def get(self,sql):
        self._cur.execute(sql)
        return self._cur.fetchone()

    def update(self,sql):
        pass

    def delete(self,sql):
        pass

    def insert(self,sql):
        pass

# Wrapper Redis
class Redis():

    def __init__(self,host,port=6379,db=0,password=''):
        self._host = host
        self._port = port
        self._db = db
        self._password = password

    def Connect(self):
        return PyRedis.Redis(self._host, self._port, self._db, self._password)