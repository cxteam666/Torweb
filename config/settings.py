#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

from tornado.options import define, options

define("host", default='0.0.0.0', help="Listen on the given IP", type=str)
define("port", default=8889, help="Run on the given port", type=int)

config = {
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'db': 'test',
        'user': 'test',
        'pass': 'test',
        'charset': 'utf8'
    },
    'redis': {
        'host': '127.0.0.1',
        'port': 6379,
        'password': '',
        'db': '0'
    },
    'host': options.host,
    'port': options.port,
    'app_settings': dict(
        template_path = 'view',
        static_path = 'static',
        static_url_prefix = '/static/',
        xsrf_cookies = False,
        cookie_secret = "db884468559f4c432bf1c1775f3dc9da",
        cookie_name = '_ksid',
        session_key = "_k_session_",
        session_expires = 7200,
        login_url = "/user/login",
        debug = True,
        autoreload = True
    )
}