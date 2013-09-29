#!/usr/bin/env python
import sys
import os
import cPickle as pickle
HOME = os.environ['HOME']
cmdListPath = '%s/bin/data/cmdList.pickle' % HOME
line = "*" * 25, "result", "*" * 25

def color(str):
    return '\033[1;31;40m %s \033[0m' % str

class Cmd():
    def __init__(self, argv):
        self.mark = argv[1]
        self.cmd = ' '.join(argv[2:])
        self.loadCmdList()
        if len(self.cmd) == 0:
            self.runflag = True
        else:
            self.runflag = False
        
    def loadCmdList(self):
        try:
            with open(cmdListPath, 'rb') as f:
                cmdList = pickle.load(f)
                self.cmdList =  cmdList
        except Exception, ex:
            print color(ex)
            self.cmdList =  {}

    def addCmd(self):
        self.cmdList[self.mark] = self.cmd
  
    def getCmd(self):
        cmd = self.cmdList.get(self.mark)
        return cmd

    def save(self):
        self.cmdList[self.mark] = self.cmd
        print color(self.cmd)
        with open(cmdListPath, 'wb') as f:
            pickle.dump(self.cmdList, f)
        
    def run(self):
        if self.runflag:
            cmd = self.getCmd()
            if cmd:
                print color('run cmd: %s' %cmd)
                print '|', line, '|'
                os.system(cmd)
                print '^', line, '^'
        else:
            self.save()
            

if __name__ == "__main__":
    cmd = Cmd(sys.argv)
    print color('cmdList: ')
    for k,v in cmd.cmdList.iteritems():
        print color(k), v
    cmd.run()

