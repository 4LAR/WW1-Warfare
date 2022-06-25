
import cpuinfo
import psutil
import platform

from console import *

class machine_info(console_term):
    def __init__(self):
        super().__init__()

        self.error_promt = 'MACHINE_INFO: '

        self.info = {}

        self.generated = False

    def get(self, log=False):
        self.info = {}
        try:
            self.info['platform']=platform.system()
            self.info['platform-release']=platform.release()
            self.info['platform-version']=platform.version()
            self.info['architecture']=platform.machine()
            self.info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
            self.info['cpu']=cpuinfo.get_cpu_info()['brand_raw']
            self.generated = True

            if log:
                self.to_str(True)

            return self.info

        except Exception as e:
            self.print(str(self.error_promt) + str(e), 3)
            return False

    def to_str(self, log=False):
        self.str = ''
        if self.generated:
            for info in self.info:
                self.str += '%s: %s\n' % (info, self.info[info])

            if log:
                self.print(self.str, 1, no_time_bool=True)

            return self.str

        else:
            self.print(str(self.error_promt) + 'The configuration was not collected.', 3)
            return ""
