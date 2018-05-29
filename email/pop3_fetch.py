#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


email = 'haoping624@163.com'
password = 'Xmima624'
pop3_server = 'pop.163.com'


server = poplib.POP3(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))


server.user(email)
server.pass_(password)


print('Messages: %s. Size: %s' % server.stat())
resp, mails, octets = server.list()
print(mails)


index = len(mails)
resp, lines, octets = server.retr(index)


msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)


# server.dele(index)
server.quit()


def print_info(msg, indent=0):
	if indent == 0:

