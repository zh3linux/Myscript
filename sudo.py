#!/usr/bin/env python
#coding:utf-8
import requests,os
import cPickle as pickle
import smtplib,time,datetime
from email.Message import Message
from pyquery import PyQuery as pq

mygmail = 'example@gmail.com'
passwd = '123'
url = 'http://www.sodu.tv/'
novelurl = 'http://www.sodu.tv/mulu_536384.html'
def sendgmail(mess):
    try:
        server = smtplib.SMTP('smtp.gmail.com')
        server.starttls()
        server.login(mygmail,passwd)
        message = Message()
        message['Subject'] = 'Sudo小说更新'    #邮件标题
        message['From'] = mygmail
        message['To'] = mygmail
        message.set_payload(mess.encode('utf-8'))
        msg = message.as_string()
        server.sendmail(mygmail,mygmail,msg)
        time.sleep(3)
        server.quit()
    except:
        print "Error"


def main():
    f = open('cook.data','r')
    cook = pickle.load(f)
    f.close()
    while 1:
        print 'Start'
        r = requests.get(url, cookies=cook)
        stutas = u'有更新'
        if stutas in r.text:
            print 'Have Update'
            d = pq(r.text)
            mess =  d('form#form1 table tr').eq(1).text()
            mess = mess + novelurl
            sendgmail(mess)
            r = requests.get(novelurl,cookies=r.cookies)
            cook = r.cookies
            f = open('cook.data','w')
            pickle.dump(cook,f)
            f.close()

        print "Now:",datetime.datetime.now().hour,'h'
        if datetime.datetime.now().hour>21 or datetime.datetime.now().hour<3:
            time.sleep(300)
        else:
            time.sleep(1800)



if __name__ == '__main__':
    if not os.path.isfile('cook.data'):
        f = open('cook.data','w')
        cook = dict(ra='2|0bhvk0v4')
        pickle.dump(cook,f)
        f.close()
    main()
