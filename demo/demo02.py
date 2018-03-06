# from email.mime.text import MIMEText
# msg = MIMEText("hello,send by python..","plain","utf-8")
#
#
# # 输入邮箱地址和口令
# from_addr = input("314782553@qq.com")
# password = input("Wohuai85849188")
#
# # 输入收件人地址
# to_addr = input("jxjt_1990@163.com")
#
# # 输入SMTP服务器地址
# stmp_server = input("smtp@qq.com")


# import smtplib
# server = smtplib.SMTP(stmp_server,25)
# server.set_debuglevel(1)
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# from_addr = input('From: ')
# password = input('Password: ')
# to_addr = input('To: ')
# smtp_server = input('SMTP server: ')

# 输入邮箱地址和口令
from_addr = input("jxjt_1990@qq.com")
password = input("xxxxxxxx")

# 输入收件人地址
to_addr = input("314782553@qq.com")

# 输入SMTP服务器地址
stmp_server = input('smtp.163.com')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(stmp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()