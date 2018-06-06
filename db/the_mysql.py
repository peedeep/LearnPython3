#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import mysql.connector


conn = mysql.connector.connect(user='root', password='Xmima624!', database='test')
cursor = conn.cursor()
cursor.execute('drop table user')
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
usersvalues = []
for i in range(5):
	usersvalues.append((str(i), 'name' + str(i)))
print(usersvalues)
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Rick'])
#cursor.execute('insert into user (id, name) values (%s, %s)', usersvalues)
print(cursor.rowcount)
conn.commit()
cursor.close()


cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
