#!/usr/bin/env python
import sys
import os
class Grep():
    def __init__(self, argvs):
        self.v = False
        self.argvs = argvs
        self.select = argvs[1]
        self.cmd = 'grep -n -r "%s" .' % self.select

    def buildcmd(self):
        for arg in self.argvs[2:]:
            if self.v:
                sh = 'grep -v "%s"' % arg
                self.cmd = "%s | %s" % (self.cmd, sh)
                self.v = False

            elif arg == '-v':
                self.v = True
            else:
                sh = 'grep "%s"' % arg
                self.cmd = "%s | %s" % (self.cmd, sh)
        self.cmd = '%s | grep --color=auto "%s"' % (self.cmd, self.select)
        return self.cmd

    def run(self):
        cmd = self.buildcmd()
        os.system(cmd)

grep = Grep(sys.argv)
grep.run()
