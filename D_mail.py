#!/Usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.Utils import formatdate
import time
from datetime import datetime as dt
import argparse


if __name__ == '__main__':
    psr = argparse.ArgumentParser()
    psr.add_argument('--user', required=True)
    psr.add_argument('--password', required=True)
    psr.add_argument('--to', default="None")
    psr.add_argument('--frm', default="None")
    psr.add_argument('--hour', required=True)
    psr.add_argument('--body', required=True)
    args = psr.parse_args()

    username, password = args.user, args.password

    if args.to == "None":
        to = args.user
    else:
        to = args.to
    if args.frm == "None":
        frm = args.user
    else:
        frm = args.to

    sub = ''
    body = args.body
    ubody = unicode(body, 'utf-8')

    for b in [ubody[i:i + 5] for i in range(0, len(ubody), 5)]:
        host, port = 'smtp.gmail.com', 465
        msg = MIMEText(b.encode('utf-8'))
        msg['Subject'] = sub
        msg['From'] = frm
        msg['To'] = to
        n = dt.now()
        msg['Date'] = formatdate(time.mktime((n.year, n.month,
                                              n.day, n.hour + int(args.hour), n.minute, n.second, n.weekday(), 0, 0)))
        smtp = smtplib.SMTP_SSL(host, port)
        smtp.ehlo()
        smtp.login(username, password)
        smtp.mail(username)
        smtp.rcpt(to)
        smtp.data(msg.as_string())
        smtp.quit()
