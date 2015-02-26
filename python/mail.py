#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © lanrenzhoumo.com
# Date  : 2015-02-26
# Author: yumi
# Email : <yumi@lanrenzhoumo.com>
#
# Distributed under terms of the MIT license.

'''
    发送一个文本邮件
    参考网址:http://www.cnblogs.com/xiaowuyi/archive/2012/03/17/2404015.html
'''

import logging
import smtplib
from email.mime.text import MIMEText

# 腾讯企业邮箱
tc_exmail_host="smtp.exmail.qq.com"

class MailSender():
    """这个类的职责就是发送邮件"""
    def __init__(self):
        pass
    
    def send_mail(self, sender, passwd, receiver_list, title, content, mail_host=tc_exmail_host):
        """发送邮件"""
        assert isinstance(receiver_list, (list, tuple))
        me = "hello" + "<" + sender + ">"
        msg = MIMEText(content, _subtype="plain", _charset="utf8")
        msg["Subject"] = title
        msg["From"] = me
        msg["To"] = ";".join(receiver_list)
        try:
            server = smtplib.SMTP()
            server.connect(mail_host)
            server.login(sender, passwd)
            server.sendmail(me, receiver_list, msg.as_string())
            server.close()
            return True
        except Exception as e:
            logging.error(str(e))
            return False

mail_sender = MailSender()
send_mail = mail_sender.send_mail

if __name__ == '__main__':
    if send_mail("yumi@lanrenzhoumo.com", "Fuck U Man", ["yumi@lanrenzhoumo.com"], "code complete", "code complete is a cool book"):
        print "发送成功"
    else:
        print "发送失败"
