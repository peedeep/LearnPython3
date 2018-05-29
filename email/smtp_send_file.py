#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase


import smtplib


def _format_addr(s):
	name, addr = parseaddr(s)
	formataddr_str = formataddr((Header(name, 'utf-8').encode(), addr))
	print('formataddr_str: ', formataddr_str)
	return formataddr_str


from_addr = 'haoping624@163.com'
password = 'Xmima624'
to_addr = '56639624@qq.com, 603140660@qq.com, 61836473@qq.com'
smtp_server = 'smtp.163.com'
smtp_port = 25

msg = MIMEMultipart()
msg['From'] = _format_addr('Rick <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自Rick的问候...', 'utf-8').encode()


msg.attach(MIMEText('I love you...', 'plain', 'utf-8'))


with open('test.jpg', 'rb') as f:
	mime = MIMEBase('image', 'jpg', filename='test.jpg')
	mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-Id', '0')
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)


server = smtplib.SMTP(smtp_server, smtp_port)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr.split(','), msg.as_string())
server.quit()


