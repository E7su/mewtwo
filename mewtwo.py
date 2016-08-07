import win32api, win32con, win32gui, time, win32com.client
import subprocess

def enumerate_children(parent):
    prev = None
    while True:
        cur = win32gui.FindWindowEx(parent, prev, None, None)
        if not cur:
            return
        yield cur
        prev = cur

f = subprocess.Popen([r'K:\path'])
time.sleep(1)
Shell = win32com.client.Dispatch('WScript.Shell')
Shell.SendKeys('Text Test')
Shell.SendKeys('{TAB}')

br = '0000'
n = 5
time.sleep(10)

while len(str(br)) < n:
    print(br)
    br = int(br) + 1
    
    time.sleep(10)
    
    for i in range(n):
        Shell.SendKeys('{BKSP}')
        
    Shell.SendKeys(br)
    Shell.SendKeys('~')

    wnd = win32gui.FindWindow(None, 'Text Form')
    a = [win32gui.GetWindowText(item) for item in enumerate_children(wnd)]
    
    #if a[4] == 'Text End':
    #    pass
    #else:
    #   break

#Name=win32gui.GetWindowText(win32gui.GetForegroundWindow())

#win32gui.GetForegroundWindow()
#HWND
#or Shell.find_element_by_name('Text End') == 0

#Name=win32gui.GetWindowText(win32gui.GetForegroundWindow())
#print(Name)

#al1 = 'abcdefghijklmnopqrstuvwxyz'
#al2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#your_list = '0123456789 '
#complete_list = []
#for current in xrange(10):
#    a = [i for i in your_list]
#    for y in xrange(current):
#        a = [x+i for i in your_list for x in a]
#    complete_list = complete_list+a

#print(Shell.find('Text End'))
