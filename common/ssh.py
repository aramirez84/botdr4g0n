#The MIT License (MIT)
#Version 1.1
#Copyright (c) 2014 Marcos Nesster (mh4x0f)
#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in
#the Software without restriction, including without limitation the rights to
#use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
#the Software, and to permit persons to whom the Software is furnished to do so,
#subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import pxssh
from helpers.color import setcolor
class ssh(object):
    def __init__(self, host,port, user, password,checkconnect=True):
        self.host = host
        self.user = user
        self.port = port
        self.connection = checkconnect
        self.password = password
        self.status = None
        self.on     = False
        self.session = self.connect()
    def connect(self):
        try:
            self.s = pxssh.pxssh()
            self.s.login(self.host, self.user, self.password,port=self.port)
            if self.connection:
                self.status = '[{}]'.format(setcolor('ON',color='green'))
                self.on = True
            return self.s
        except Exception, e:
            Hostfaled = str(self.host)
            self.status = '[{}]'.format(setcolor('OFF',color='red'))
            self.on = False
    def logout(self):
        self.s.terminate(True)
    def info(self):
        kernelversion = self.send_command('uname -r')
        print('PID      :: {}'.format(self.session.pid))
        print('timeout  :: {}'.format(self.session.timeout))
        print('Shell    :: {}'.format(self.session.name))
        print('Kernel   :: {}\n'.format(kernelversion.split()))
    def send_command(self,cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return str(self.session.before).replace(cmd,'')