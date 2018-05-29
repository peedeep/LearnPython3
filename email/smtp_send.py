#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr


import smtplib


def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))


#from_addr = input('From: ')
#password = input('Password: ')
#to_addr = input('To: ')
#smtp_server = input('SMTP server: ')
from_addr = 'haoping624@163.com'
password = 'Xmima624'
to_addr = '603140660@qq.com, 61836473@qq.com, 56639624@qq.com'
smtp_server = 'smtp.163.com'

#msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg = MIMEText('<html><body><h1>Hello</h1>' +'<p>send by <a href="http://www.python.org">Python</a>...</p>' +'</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr('Rick, Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自STMP的问候.......', 'utf-8').encode()


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr.split(','), msg.as_string())
print('邮件发送成功')
server.quit()
