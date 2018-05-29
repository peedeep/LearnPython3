#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests


r = requests.post('https://accounts.douban.com/login', data={'form_email':'56639624@qq.com', 'form_password':'Xmima624'})
print(r.status_code)
print(r.url)
print(r.headers)
print(r.cookies)

