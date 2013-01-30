#!/usr/bin/env python
#coding:utf-8
import os,sys
import time,pexpect
ssh_newkey = 'Are you sure you want to continue connecting'
server1 = ['abc','example.com','123','7070','22']
server2 = ['bcd','example.com','456','7071','22']

def sshcon(args):
    username , sshserver ,  password , localport,port =args
    if os.popen('lsof -t -i:%s'%localport).read():
        #print sshserver,localport,'Connecting'
        #time.sleep(60)
        pass
    else:
        try:
            comm = 'ssh -p %s -qTfnN -g -D %s %s@%s'%(port,localport,username,sshserver)
            print comm
            s = pexpect.spawn(comm)
            i=s.expect([ssh_newkey,'password:',pexpect.EOF])
            if i==1:
                print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()), "--- connect to it"
                s.sendline(password)
                s.expect(pexpect.EOF)
                #print s
        except:
            print "Error"
        time.sleep(5)
    pass

def main(*server):
    while 1:
        for serv in server:
            #print serv
            sshcon(serv)
        time.sleep(60)
if __name__ == "__main__":
    main(server1,server2)
