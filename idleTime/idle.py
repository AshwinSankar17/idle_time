import platform
import os

if (platform.system() == 'Windows'):
    from ctypes import Structure, windll, c_uint, sizeof, byref
    
    class LASTINPUTINFO(Structure):
        _fields_ = [
            ('cbSize', c_uint),
            ('dwTime', c_uint),
        ]
 
    def get_idle_duration():
        lastInputInfo = LASTINPUTINFO()
        lastInputInfo.cbSize = sizeof(lastInputInfo)
        windll.user32.GetLastInputInfo(byref(lastInputInfo))
        millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
        return millis / 1000.0

else:
    def exec_cmd(cmd_string):
        r = os.popen(cmd_string)
        result_string = r.read()
        r.close
        return result_string

    def get_idle_duration():
        #         millis = os.system('sudo -u whoami xprintidle')
        millis = int(exec_cmd("xprintidle"))
        os.system('clear')
        return millis / 1000.0
