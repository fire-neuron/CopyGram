import interface
import wx
import os
import sys
import sshconnect
path_to_my_components = os.path.join(os.path.dirname(__file__), 'handlers')


sys.path.append(path_to_my_components)


ssh = None
frame = None
app = wx.App()
frame = interface.MyFrame(None, "CopyGram")



def h_connect():
    import auth
    auth.tab_init(frame)
    import tab_one
    tab_one.tab_init(frame)
    import tab_two
    tab_two.tab_init(frame)
    import tab_three
    tab_three.tab_init(frame)


h_connect()

def stop_ssh(event):
    ssh = sshconnect.ssh
    ssh.close()
    frame.Destroy()

def cleaner():
    frame.Bind(wx.EVT_CLOSE,stop_ssh)

cleaner()




app.MainLoop()
