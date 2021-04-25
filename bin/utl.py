# -*- coding: utf-8 -*-

import os, imaplib, time, datetime, tarfile, shutil
from cStringIO import StringIO
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders, message_from_string
from email.base64MIME import encode as encode_base64

def dt_now():
    return datetime.datetime.now()

def time_n(dl):
    return dl - datetime.timedelta(microseconds=dl.microseconds)

def time_stamp(spr=':'):
    return datetime.datetime.utcnow().strftime(spr.join(['%Y-%m-%d' + (' ' if spr == ':' else '-') + '%H', '%M', '%S']))    

def msg_time():
    return imaplib.Time2Internaldate(time.time())

def cls(d):
    shutil.rmtree(d)

def log(s):
    print s

def untar(tf, dst):
    t = tarfile.open(tf, 'r:gz')
    t.extractall(dst)
    t.close()

def tar(tf, fl):
    # fl ex.: [('c:/usr/src/py/test1.py', 'files/1.py'), 
    #          ('c:/usr/src/cpp/test2.cpp', 'files/2.cpp'), 
    #          ('c:/usr/doc/comp/test.pdf', 'files/3.pdf')]
    t = tarfile.open(tf, 'w:gz')
    try:
        for f in fl:
            f1, f2 = f
            data = open(f1, 'rb').read()
            info = tarfile.TarInfo(f2)
            info.size = len(data)
            t.addfile(info, StringIO(data))
    finally:
        t.close()

def message(send_from, send_to, subject, text, files=None):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    
    if files is not None:
        for f in files:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(f, 'rb').read())
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
            msg.attach(part)
    return msg

def channel(user='cwtu320313', pwd='320313'):
    c = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    c.login(user, pwd)
    return c

def fetch(query, tag='[Google Mail]/All Mail', last_only=True, 
          user='cwtu320313', pwd='320313'):
    ans = []
    ch = channel(user, pwd)
    ch.select(tag)
    r, [ids] = ch.search(None, query)
    
    if not ids.split():
        return [] 
    
    all_ = [ids.split()[-1]] if last_only else ids.split()
    for id in all_:
        r, d = ch.fetch(id, '(RFC822)')
        for part in d:
            if isinstance(part, tuple):
                msg = message_from_string(part[1]) 
                sbj = msg['subject']
                files = []
                for w in msg.walk():
                    mt = w.get_content_maintype()
                    if mt == 'multipart':  # multipart/* are just containers.
                        continue
                    
                    elif mt == 'text':
                        text = w.get_payload(decode=True) 
                    
                    else:
                        fn = w.get_filename()
                        fc = w.get_payload(decode=True)
                        files.append((fn, fc))
        ans.append(dict(id=id, text=text, files=files, sbj=sbj))
    return ans

def send(send_from='', send_to=('',), sbj='', txt='', att=None, 
         user='cwtu.clinic', pwd='cwtu320313'):
    msg = message(send_from, send_to, sbj , txt, att)
    ch = channel(user, pwd)
    ch.append('[Google Mail]/All Mail', '', msg_time(), str(msg))
